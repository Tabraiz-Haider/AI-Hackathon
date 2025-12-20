---
id: 002
title: Clarify Ambiguous 'Yes' Response for Init Purpose
stage: constitution
date: 2025-12-07
surface: agent
model: gemini-cli-agent
feature: none
branch: main
user: user
command: sp init
labels: ["clarification", "constitution"]
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

Your response "yes" is ambiguous. Could you please specify which of the following you intend:

1.  **Initiate a new project and define its constitution.**
2.  **Parse an existing `constitution.md` to understand project principles.**

## Outcome

- ✅ Impact: PHR for clarification created; agent is awaiting a clear, specific response from the user.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: User to provide a specific choice (1 or 2).
- 🧠 Reflection: User's repeated ambiguous "yes" requires further simplification of options.

## Evaluation notes (flywheel)

- Failure modes observed: Ambiguous user input.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Present options as numbered choices.
