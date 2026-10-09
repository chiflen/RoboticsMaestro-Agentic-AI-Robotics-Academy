# Responsible AI and Robotics
1. Treat model output as a hypothesis until verified.
2. Never commit keys, credentials, personal data or proprietary customer data.
3. Use synthetic/public data by default.
4. Tools need narrow schemas, least privilege, validation, timeouts and logs.
5. Consequential actions require human review.
6. Untrusted retrieved text cannot override security policy.
7. Use rate limits, cost budgets, retry limits and a kill switch.
8. Respect copyright, licenses, privacy and terms.
9. Label synthetic content and disclose AI assistance when relevant.
10. Simulation is not a robot safety certification.

## Robotics-specific
Use simulation first. Document operating envelope, speed/force limits, workspace and stop behavior. Physical robots require qualified supervision, risk assessment, emergency stop and manufacturer guidance. Safety-rated functions must be independent of an ordinary LLM. Record test conditions, failures and limitations.

## Threat review
Can untrusted content invoke a privileged tool? Are arguments validated server-side? Can retries duplicate actions? Can logs leak data? What is the maximum impact of one action? What happens if the provider fails? Can a human pause, inspect and reverse actions?
