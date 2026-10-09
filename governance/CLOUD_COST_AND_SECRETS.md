# Cloud Cost and Secrets
- Store credentials in environment variables or approved secret manager; never in source code.
- Commit `.env.example` placeholders only. Rotate exposed keys.
- Separate development and production identities.
- Set per-team budgets, token/request limits, timeouts, retry ceilings and concurrency caps.
- Measure cost per successful task, including retries and failures.
- Shut down cloud resources after labs.
- Use small models and short prompts during early experiments.
- Exclude regulated/sensitive data from standard training.
- Confirm provider account requirements, region, model access, quotas, logging, terms and pricing before class.
