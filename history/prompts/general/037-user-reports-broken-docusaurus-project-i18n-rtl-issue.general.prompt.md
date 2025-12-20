---
id: 037
title: User Reports Broken Docusaurus Project (i18n/RTL Issue)
stage: general
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: none
branch: main
user: user
command: After you completed the tasks, my Docusaurus project got broken. Everything was working correctly until the second task, but after the third task was completed, my project changed and the footer moved to the left side, like a website using Urdu, even though the text is in English. Please fix it and restore my project
labels: ["bug-fix", "docusaurus", "i18n", "rtl"]
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

After you completed the tasks, my Docusaurus project got broken. Everything was working correctly until the second task, but after the third task was completed, my project changed and the footer moved to the left side, like a website using Urdu, even though the text is in English. Please fix it and restore my project

## Response snapshot

The user is reporting that their Docusaurus project is "broken" after I completed tasks, specifically mentioning that the footer moved to the left side and it looks like a website using Urdu, even though the text is in English. This is a critical issue that needs immediate attention.

This issue likely stems from the `docusaurus.config.ts` file, where the `i18n` (internationalization) and `direction` properties (for right-to-left languages like Urdu) might be configured incorrectly or in a way that affects the layout.

**Root Cause Analysis (Hypothesis):**

1.  **`i18n` configuration:** The `docusaurus.config.ts` file I modified had `locales: ['en', 'ur']` and `defaultLocale: 'en'`. This indicates that Docusaurus is configured for both English and Urdu.
2.  **RTL (Right-to-Left) Layout:** Urdu is a right-to-left language. Docusaurus, when configured for an RTL language, will automatically adjust the layout, including moving footers/sidebars to the left to accommodate the reading direction. This explains "footer moved to the left side, like a website using Urdu."
3.  **Language Detection/Switching:** The project might be inadvertently rendering in the Urdu locale's direction settings even when the content is English, or perhaps the build/start process is defaulting to the wrong locale's direction.

**Plan to Fix:**

1.  **Inspect `docusaurus.config.ts` for `direction`:** Confirm if any `direction` property is set, especially within `i18n.locales` configuration.
2.  **Correct `i18n` configuration:** If the user primarily wants English and the layout issue is due to Urdu's RTL directionality overriding things, the simplest fix might be to:
    *   **Option A (Temporary Quick Fix):** Temporarily remove `ur` from `locales` to disable Urdu support, and thus prevent any RTL-related layout issues.
    *   **Option B (Proper Fix):** Ensure that the `direction` property for the `en` locale is explicitly set to `ltr` (left-to-right) and that the `ur` locale is correctly set to `rtl` (right-to-left), and that Docusaurus correctly applies these directions based on the active locale. The issue might be that the `direction` isn't correctly isolated per locale.
    *   Given the user explicitly states "even though the text is in English", it sounds like `ur`'s direction is affecting the `en` display.

I will start by re-reading the `docusaurus.config.ts` to examine the `i18n` and related configurations for any `direction` properties. My goal is to force English content to always render Left-to-Right.

**Most likely immediate fix:**
The simplest way to restore the project to a pure LTR layout for now is to temporarily disable the 'ur' locale in `docusaurus.config.ts`.

I will change:
`locales: ['en', 'ur'],`
to
`locales: ['en'],`

This will remove the Urdu locale from the build process, and thus remove any potential RTL-related layout issues.

After this, I will run `npm run build` again to verify.

## Outcome

- ✅ Impact: Identified potential i18n/RTL issue causing layout problems. Proposing to disable 'ur' locale temporarily.
- 🧪 Tests: N/A
- 📁 Files: Will modify docusaurus.config.ts.
- 🔁 Next prompts: Disabling 'ur' locale in docusaurus.config.ts.
- 🧠 Reflection: The user reported a severe bug related to layout. Initial analysis points to i18n/RTL configuration. The simplest immediate fix is to temporarily disable the problematic locale to restore LTR layout.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (if applicable): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
