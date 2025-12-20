---
id: 003
title: User Repeatedly Says 'Yes' to Numbered Options for Init Purpose
stage: constitution
date: 2025-12-07
surface: agent
model: gemini-cli-agent
feature: none
branch: main
user: user
command: sp init
labels: ["clarification", "blocker", "constitution"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

yes

## Response snapshot

I understand you're responding with "yes," but I need you to choose specifically between option 1 or option 2 to proceed. I cannot interpret "yes" as a definitive choice in this context.

## Outcome

- ✅ Impact: PHR for repeated ambiguous "yes" created; agent is blocked awaiting a clear, specific choice from the user.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: User to provide a specific choice (1 or 2), or a different command.
- 🧠 Reflection: User continues to provide ambiguous input ("yes"). The agent cannot proceed with `sp init` without a clear choice.

## Evaluation notes (flywheel)

- Failure modes observed: Ambiguous user input, inability to follow numbered choices.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): State inability to proceed without a clear choice.
