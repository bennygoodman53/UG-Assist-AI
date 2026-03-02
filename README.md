# UG Assist AI - University of Ghana IT Helpdesk Chatbot

A working AI-based helpdesk chatbot/demo designed for **University of Ghana, Legon**.

## What is included
- Prompt/rule-based chatbot for UG support FAQs.
- Knowledge base aligned to requested sources:
  - https://admissions.ug.edu.gh/undergraduate/faq
  - https://www.ug.edu.gh/aad/resources/graduation/faq
  - https://www.ug.edu.gh/aad/faqs
- Simulated real IT support scenarios.
- Privacy and security guardrails.
- Evaluation script and risk assessment documentation.

## Project structure
- `app/chatbot.py` - chatbot engine, CLI, and scripted demo mode.
- `data/ug_faqs.json` - FAQ knowledge base.
- `tests/evaluate_chatbot.py` - scenario-based accuracy evaluation.
- `docs/use_cases.md` - use-case documentation.
- `docs/evaluation.md` - effectiveness and risk evaluation.

## Run the interactive chatbot
```bash
python app/chatbot.py
```

## Display the scripted demo
```bash
python app/chatbot.py --demo
```

## Run evaluation
```bash
python tests/evaluate_chatbot.py
```

## Security posture
- Prevents sensitive data sharing prompts.
- Redirects account-level operations to official UG channels.
- Works fully offline in local mode.

## Notes
Due to restricted network access in this execution environment, live scraping from UG URLs could not be completed. The current FAQ set is structured from the topics and support intents associated with the specified UG FAQ sources and should be validated against official pages before production use.
