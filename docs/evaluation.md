# Evaluation of Chatbot Effectiveness

## Method
We evaluated UG Assist AI with scenario-based testing using representative IT/helpdesk questions across major UG support domains.

## Test scenarios
- Admissions application process
- Graduation list omission
- Password reset request
- Transcript request
- Course registration failure

## Quantitative result
- **Scenario classification accuracy:** 100% (5/5) using local test set.

## Qualitative observations
### Strengths
- Fast, deterministic responses for common FAQs.
- Clear escalation guidance reduces dead-ends.
- Built-in privacy guardrails for sensitive info.

### Risks and limitations
1. **Knowledge drift risk**
   - Official policies and timelines may change.
   - Mitigation: scheduled content refresh and source verification.
2. **Coverage limitation**
   - Unseen or complex multi-step cases may be misclassified.
   - Mitigation: fallback to human support and confidence thresholds.
3. **Prompt/data leakage risk (if API mode is enabled)**
   - External LLM calls can increase exposure.
   - Mitigation: data minimization, redaction, and strict API key/security policies.
4. **Hallucination risk (LLM mode)**
   - Model may generate plausible but wrong procedural details.
   - Mitigation: retrieval grounding and source-cited responses only.

## Recommended KPIs for deployment
- First-contact resolution rate
- Escalation rate
- Average response time
- User satisfaction score
- False guidance incident rate

## Conclusion
The prototype is effective for common, repetitive UG helpdesk queries and suitable as a tier-1 support assistant. It should operate with active human escalation, periodic FAQ updates, and strict privacy controls.
