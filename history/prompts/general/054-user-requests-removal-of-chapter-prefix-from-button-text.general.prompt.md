---
id: 054
title: User Requests Removal of "Chapter" Prefix from Button Text
stage: general
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: none
branch: main
user: user
command: For the text inside the buttons, remove the word ‘Chapter’ at the start of the number.
labels: ["ui-update", "docusaurus", "hero-section", "styling"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - c:\Users\SHAYAN\OneDrive\Desktop\New folder (4)\AI-Spec-Driven-Hackathon\src\components\HomepageFeatures\index.tsx (modified)
tests:

---

## Prompt

For the text inside the buttons, remove the word ‘Chapter’ at the start of the number.

## Response snapshot

The user wants to remove the word "Chapter" from the start of the chapter names inside the buttons.
For example, "Chapter 1: Basics of Physical AI" should become "1: Basics of Physical AI".

This applies to all 10 chapter buttons in the hero section cards.

I need to modify `src/components/HomepageFeatures/index.tsx` again, specifically the `FeatureList` array.

**Plan:**
1.  **Modify `FeatureList`:** Iterate through the `Link` components within the `description` of the first two cards and adjust the text.

I will perform a single `replace` operation targeting the entire `FeatureList` to ensure consistency and atomicity of the change.

## Outcome

- ✅ Impact: Will remove "Chapter" prefix from hero section chapter button labels.
- 🧪 Tests: N/A
- 📁 Files: Will modify src/components/HomepageFeatures/index.tsx.
- 🔁 Next prompts: Executing replace operation.
- 🧠 Reflection: The user requested to remove the "Chapter" prefix from button labels. This will be achieved by modifying the text within the Translate components for each chapter button.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (if applicable): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
