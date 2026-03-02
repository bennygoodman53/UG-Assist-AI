from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.chatbot import UGHelpdeskBot


def run_eval() -> None:
    bot = UGHelpdeskBot()
    scenarios = [
        {"query": "How do I apply for UG undergraduate admission?", "expected_category": "Admissions"},
        {"query": "My name is missing from graduation list", "expected_category": "Graduation"},
        {"query": "I forgot my portal password", "expected_category": "IT Security"},
        {"query": "How can I request transcript", "expected_category": "Academic Records"},
        {"query": "I can't register courses on MIS", "expected_category": "Registration"},
    ]

    correct = 0
    for case in scenarios:
        result = bot.ask(case["query"])
        if result.get("category") == case["expected_category"]:
            correct += 1
        assert result.get("source_url", "").startswith("https://"), "source_url missing"
        assert 0.0 <= result.get("confidence", 0.0) <= 1.0, "invalid confidence"

    accuracy = correct / len(scenarios)
    print(f"Scenario accuracy: {accuracy:.2%} ({correct}/{len(scenarios)})")


if __name__ == "__main__":
    run_eval()
