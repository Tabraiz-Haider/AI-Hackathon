---
id: 064
title: User Requests Replacing "Claude Code" with "Gemini" in Footer
stage: general
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: none
branch: main
user: user
command: footer ma project tool ma calude code ko remove kar ka gemini types kar doo.
labels: ["ui-update", "docusaurus", "footer"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - c:\Users\SHAYAN\OneDrive\Desktop\New folder (4)\AI-Spec-Driven-Hackathon\docusaurus.config.ts (modified)
tests:

---

## Prompt

footer ma project tool ma calude code ko remove kar ka gemini types kar doo.

## Response snapshot

The user wants to modify the footer again. Specifically:
1.  Locate the "Project Tools" section in the footer.
2.  Find the item labeled "Claude Code".
3.  Remove this item.
4.  Add a new item in its place with the label "Gemini".

**Current `footer.links.items` under 'Project Tools':**
```typescript
        {
          title: 'Project Tools',
          items: [
            {
              label: 'Claude Code',
              href: 'https://www.claude.com/product/claude-code',
            },
            {
              label: 'Docusaurus',
              href: 'https://docusaurus.io/',
            },
          ],
        },
```
The user wants to remove `Claude Code` and replace it with `Gemini`. I will need to clarify what the `href` for "Gemini" should be. For now, I'll use a placeholder or remove the `href` if they just want the label. Given the context of the user interacting with a Gemini agent, `https://gemini.google.com/` could be a suitable default for `href`.

**Plan:**
1.  **Modify `docusaurus.config.ts`:**
    *   Locate the "Claude Code" item under "Project Tools".
    *   Replace it with a new item: `{ label: 'Gemini', href: 'https://gemini.google.com/' }`.

## Outcome

- ✅ Impact: Will replace "Claude Code" with "Gemini" in the footer's 'Project Tools' section.
- 🧪 Tests: N/A
- 📁 Files: Will modify docusaurus.config.ts.
- 🔁 Next prompts: Executing replace operation.
- 🧠 Reflection: The user requested to replace a specific item in the footer's 'Project Tools' section. This is a direct modification of docusaurus.config.ts.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (if applicable): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
