# UG Assist AI Use-Case Documentation

## System goal
UG Assist AI is an AI-based IT helpdesk/chatbot prototype for University of Ghana, Legon. It automates first-line responses for admissions, graduation, records, registration, and account-access issues.

## Primary users
- Prospective undergraduate applicants
- Continuing students
- Final-year students preparing for graduation
- AAD/ICT frontline support teams

## Supported use-cases
1. **Admissions support**
   - Application process guidance
   - Admission status checks
   - Payment confirmation delays
2. **Graduation support**
   - Eligibility questions
   - Missing names on graduation list
3. **Academic records support**
   - Transcript requests
   - Biodata/name correction workflow
4. **Portal/IT support**
   - Course registration blockage
   - Password reset guidance

## Response logic
- User query is tokenized and matched against an FAQ knowledge base.
- Best match is returned with:
  - answer,
  - source label,
  - escalation route.
- If sensitive terms are detected (password/PIN/card details), privacy warning is injected.
- Low-confidence queries are escalated to UG Admissions, AAD, or UG ICT helpdesk.

## Data privacy and security controls
- No password or OTP collection.
- Payment/security data sharing discouraged via real-time warning.
- Escalation to official institutional channels for account-specific operations.
- Local FAQ mode avoids external transfer of personal data.

## Operational workflow
1. Student asks question.
2. Bot provides FAQ-aligned answer.
3. Bot provides official escalation path.
4. Human support resolves complex or account-level cases.

## Assumptions and constraints
- FAQ records were designed from official UG FAQ themes and need periodic validation against official pages.
- Live web extraction was not available in this environment due network restrictions.
