"""UG Assist AI - Prompt + FAQ-based IT helpdesk chatbot for University of Ghana."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class FAQItem:
    source: str
    source_url: str
    category: str
    question: str
    answer: str
    keywords: List[str]
    escalation: str


class UGHelpdeskBot:
    """Simple retrieval + guardrail chatbot for UG support scenarios."""

    def __init__(self, faq_path: str = "data/ug_faqs.json", min_score: int = 2) -> None:
        with Path(faq_path).open("r", encoding="utf-8") as file:
            payload = json.load(file)
        self.faqs = [FAQItem(**item) for item in payload["faqs"]]
        self.security_notices = payload["security_notices"]
        self.min_score = min_score

    def _tokenize(self, text: str) -> set[str]:
        tokens = re.findall(r"[a-zA-Z0-9']+", text.lower())
        return {token for token in tokens if len(token) > 2}

    def _score(self, query: str, item: FAQItem) -> int:
        query_tokens = self._tokenize(query)
        item_tokens = self._tokenize(item.question + " " + " ".join(item.keywords))
        overlap = len(query_tokens & item_tokens)
        keyword_boost = sum(2 for kw in item.keywords if kw.lower() in query.lower())
        return overlap + keyword_boost

    def _detect_sensitive_data(self, query: str) -> Optional[str]:
        patterns = {
            "password": r"\b(password|otp|pin)\b",
            "student_id": r"\b(10\d{6,8}|\d{8,10})\b",
            "payment": r"\b(card|cvv|bank account|momo pin)\b",
        }
        for label, pattern in patterns.items():
            if re.search(pattern, query.lower()):
                return label
        return None

    def _privacy_guardrail(self, query: str) -> Optional[str]:
        found = self._detect_sensitive_data(query)
        if not found:
            return None
        return (
            "⚠️ For your privacy, please do not share sensitive credentials or payment details in chat. "
            "Use official UG portals and redact personal identifiers before continuing."
        )

    def ask(self, query: str) -> dict:
        privacy_message = self._privacy_guardrail(query)
        scored = [(item, self._score(query, item)) for item in self.faqs]
        scored.sort(key=lambda pair: pair[1], reverse=True)

        if not scored or scored[0][1] < self.min_score:
            return {
                "answer": (
                    "I could not find a confident answer in the current UG knowledge base. "
                    "Please contact the Academic Affairs Directorate (AAD) or UG Admissions directly."
                ),
                "source": "No confident match",
                "source_url": "https://www.ug.edu.gh/aad/faqs",
                "privacy_warning": privacy_message,
                "escalation": "Raise a ticket to UG ICT helpdesk or AAD front desk.",
                "confidence": 0.0,
            }

        primary, best_score = scored[0]
        max_possible = max(1, len(self._tokenize(primary.question + " " + " ".join(primary.keywords))))
        confidence = min(1.0, best_score / max_possible)

        return {
            "answer": primary.answer,
            "source": primary.source,
            "source_url": primary.source_url,
            "privacy_warning": privacy_message,
            "escalation": primary.escalation,
            "category": primary.category,
            "matched_question": primary.question,
            "confidence": round(confidence, 2),
        }


def print_response(result: dict) -> None:
    if result.get("privacy_warning"):
        print(f"Bot: {result['privacy_warning']}")
    print(f"Bot: {result['answer']}")
    print(f"Source: {result['source']}")
    print(f"Reference: {result['source_url']}")
    print(f"Confidence: {result.get('confidence', 0.0):.2f}")
    print(f"Escalation: {result['escalation']}\n")


def run_demo() -> None:
    bot = UGHelpdeskBot()
    demo_queries = [
        "How do I apply for UG undergraduate admission?",
        "My name is missing from graduation list.",
        "I forgot my portal password and OTP.",
        "How can I request transcript?",
        "Can you help me with hostel room issue?",
    ]

    print("UG Assist AI - Demo Session (University of Ghana, Legon)")
    print("=" * 60)
    for query in demo_queries:
        print(f"You: {query}")
        print_response(bot.ask(query))


def run_cli() -> None:
    bot = UGHelpdeskBot()
    print("UG Assist AI - IT Helpdesk Chatbot (University of Ghana, Legon)")
    print("Type 'exit' to quit.\n")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"exit", "quit"}:
            print("Bot: Goodbye.")
            break
        print_response(bot.ask(query))


def main() -> None:
    parser = argparse.ArgumentParser(description="UG Assist AI chatbot")
    parser.add_argument("--demo", action="store_true", help="Run a scripted demo session")
    args = parser.parse_args()

    if args.demo:
        run_demo()
        return
    run_cli()


if __name__ == "__main__":
    main()
