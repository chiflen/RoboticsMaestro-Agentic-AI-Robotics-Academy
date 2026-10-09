# Lab I2 — Lead Qualification Workflow
States: `RECEIVED → VALIDATED → QUALIFIED / NEEDS_INFO / DISQUALIFIED → DRAFTED → HUMAN_REVIEW → APPROVED_TO_SEND / REJECTED`.

Use synthetic leads; validate required fields; document criteria; make processing idempotent by lead ID; draft but do not automatically send outreach; log reason codes and timestamps; escalate uncertainty. Test duplicate event, missing email, contradictory details, disqualified lead, timeout and reviewer rejection.
