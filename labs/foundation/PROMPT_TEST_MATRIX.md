# Lab F1 — Prompt Test Matrix
Goal: make prompt quality measurable.

1. Define a JSON schema with `audience`, `offer`, `channels`, `risks`, `unknowns`.
2. Create 10 cases: normal, missing context, contradictory context, unsupported claim and malicious instruction.
3. Run with an approved model or manually.
4. Score schema validity, factual support, usefulness and uncertainty.
5. Record failure categories and revise one variable at a time.

Acceptance: 10 cases; unsupported claims are not presented as facts; missing details are identified; results committed.
