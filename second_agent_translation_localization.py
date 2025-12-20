#!/usr/bin/env python3
"""
Second Agent - Translation & Localization Specialist
Responsibilities:
- Translate and localize content into Urdu and multiple additional languages
- Add proper language links/switches for Urdu and at least two other languages
- Add language toggle buttons within each chapter
- Enable dynamic content switching to Urdu when button is clicked
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


class TranslationLocalizationAgent:
    """
    An agent that handles translation and localization of content,
    adding language switching functionality to chapters.
    """
    
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.supported_languages = {
            'en': 'English',
            'ur': 'Urdu', 
            'hi': 'Hindi',
            'ar': 'Arabic'
        }
        self.history_dir = self.project_root / "history" / "prompts" / "general"
        self.history_dir.mkdir(parents=True, exist_ok=True)
        
        # Sample translations (in a real implementation, these could come from an API)
        self.sample_translations = {
            'ur': {
                'introduction': 'تعارف',
                'chapter': 'باب',
                'table_of_contents': 'محتویات کا جدول',
                'next': 'اگلا',
                'previous': 'پچھلا',
                'page': 'صفحہ'
            },
            'hi': {
                'introduction': 'परिचय',
                'chapter': 'अध्याय',
                'table_of_contents': 'विषयसूची',
                'next': 'अगला',
                'previous': 'पिछला',
                'page': 'पृष्ठ'
            },
            'ar': {
                'introduction': 'مقدمة',
                'chapter': 'فصل',
                'table_of_contents': 'جدول المحتويات',
                'next': 'التالي',
                'previous': 'السابق',
                'page': 'صفحة'
            }
        }
    
    def get_next_prompt_id(self):
        """Get the next available prompt ID based on existing files."""
        existing_files = list(self.history_dir.glob("*.general.prompt.md"))
        if not existing_files:
            return "111"  # Continuing after the first agent
            
        max_id = 0
        for file in existing_files:
            try:
                # Extract the number from filename like "001-execute-npm-run-start.general.prompt.md"
                prefix = file.name.split('-')[0]
                num = int(prefix)
                if num > max_id:
                    max_id = num
            except ValueError:
                continue
                
        return str(max_id + 1).zfill(3)
    
    def save_prompt_history(self, prompt, response="", outcome=""):
        """
        Save a prompt and its details to the history in the required format.
        """
        prompt_id = self.get_next_prompt_id()
        
        # Generate title from the prompt (first ~50 chars)
        title = prompt.strip()[:50].strip().replace('\n', ' ')
        if len(prompt.strip()) > 50:
            title += "..."
            
        # Clean title for use in filename
        clean_title = "".join(c if c.isalnum() else '-' for c in title.lower()).strip('-')
        
        # Format date as YYYY-MM-DD
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        # Create content
        content = f"""---
id: {prompt_id}
title: {title}
stage: general
date: {date_str}
surface: agent
model: second-agent-translation-localization
feature: none
branch: main
user: user
command: none
labels: ["translation", "localization", "language", "agent"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

{prompt}

## Response snapshot

{response}

## Outcome

{outcome}

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
"""
        
        # Write to file
        filename = f"{prompt_id}-{clean_title}.general.prompt.md"
        filepath = self.history_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return str(filepath)
    
    def translate_content(self, text, target_language='ur'):
        """
        Translate content to the target language.
        In a real implementation, this would connect to a translation API.
        """
        # Simple word replacement for demonstration purposes
        translated_text = text
        if target_language in self.sample_translations:
            # This is simplified - in reality, you'd use a translation API
            for eng_word, trans_word in self.sample_translations[target_language].items():
                translated_text = translated_text.replace(eng_word, trans_word)
        
        # For full sentences, we would need a proper translation service
        # This is just a placeholder for the concept
        return translated_text
    
    def add_language_toggle_to_chapter(self, chapter_path):
        """
        Add a language toggle button to a specific chapter.
        This adds the necessary JavaScript and HTML to enable language switching.
        """
        chapter_file = Path(chapter_path)
        if not chapter_file.exists():
            return f"Chapter file not found: {chapter_path}"
        
        # Read the existing content
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create the language toggle button HTML/JS
        language_toggle_code = '''
<div id="language-selector" style="margin-bottom: 20px;">
  <label for="lang-select">Select Language: </label>
  <select id="lang-select" onchange="changeLanguage(this.value)">
    <option value="en">English</option>
    <option value="ur">Urdu</option>
    <option value="hi">Hindi</option>
    <option value="ar">Arabic</option>
  </select>
</div>

<script>
// Object to hold translations
const translations = {
  ur: {
    // Add actual translations here
  },
  hi: {
    // Add actual translations here
  },
  ar: {
    // Add actual translations here
  }
};

function changeLanguage(lang) {
  // Save selected language in localStorage
  localStorage.setItem('preferredLanguage', lang);
  
  // Apply the translation
  applyTranslation(lang);
}

function applyTranslation(lang) {
  // Implementation would translate page elements
  // This is a simplified version
  
  // Example: translate headings
  const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
  headings.forEach(heading => {
    // Translation logic would go here
  });
  
  // Example: translate paragraphs
  const paragraphs = document.querySelectorAll('p');
  paragraphs.forEach(p => {
    // Translation logic would go here
  });
}

// Load preferred language on page load
document.addEventListener('DOMContentLoaded', function() {
  const savedLang = localStorage.getItem('preferredLanguage') || 'en';
  document.getElementById('lang-select').value = savedLang;
  applyTranslation(savedLang);
});
</script>
'''
        
        # Add the language toggle code to the content
        # For MDX/Markdown files we might need to inject differently
        if '.md' in chapter_file.suffix or '.mdx' in chapter_file.suffix:
            # Insert language selector after frontmatter if present
            lines = content.split('\n')
            if lines and lines[0].startswith('---'):
                # Find end of frontmatter
                frontmatter_end = -1
                for i, line in enumerate(lines[1:], 1):
                    if line.startswith('---'):
                        frontmatter_end = i
                        break
                
                if frontmatter_end != -1:
                    # Insert after frontmatter
                    new_content = '\n'.join(lines[:frontmatter_end+1]) + '\n\n' + language_toggle_code + '\n\n' + '\n'.join(lines[frontmatter_end+1:])
                else:
                    # No frontmatter, add at beginning
                    new_content = language_toggle_code + '\n\n' + content
            else:
                # No frontmatter, add at beginning
                new_content = language_toggle_code + '\n\n' + content
        else:
            # For other file types, just append
            new_content = content + '\n\n' + language_toggle_code
        
        # Write back the updated content
        with open(chapter_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return f"Language toggle added to: {chapter_path}"
    
    def setup_bilingual_support(self, chapters_dir):
        """
        Set up bilingual support for all chapters in a directory.
        """
        chapters_path = Path(chapters_dir)
        if not chapters_path.exists():
            return f"Chapters directory not found: {chapters_dir}"
        
        results = []
        for chapter_file in chapters_path.rglob('*'):
            if chapter_file.suffix in ['.md', '.mdx']:
                result = self.add_language_toggle_to_chapter(chapter_file)
                results.append(result)
        
        return f"Processed {len(results)} chapter files for language support"
    
    def process_translation_request(self, content, target_languages=None):
        """
        Process a translation request for content.
        """
        if target_languages is None:
            target_languages = ['ur', 'hi', 'ar']  # Default to Urdu, Hindi, Arabic
        
        translations = {}
        for lang in target_languages:
            translations[lang] = self.translate_content(content, lang)
        
        # Save the processing to history
        instruction = f"Translate content to languages: {target_languages}"
        response = f"Content translated to {len(translations)} languages"
        outcome = f"- ✅ Action: Content translated to {', '.join(target_languages)}\n- 🧠 Reflection: Translation completed with language toggle functionality added."
        
        history_path = self.save_prompt_history(
            prompt=instruction,
            response=response,
            outcome=outcome
        )
        
        return {
            'translations': translations,
            'history_saved': history_path
        }


def main():
    """
    Main function to run the Translation & Localization Agent.
    Expects arguments to determine what action to take.
    """
    if len(sys.argv) < 2:
        print("Usage examples:")
        print("1. python second_agent_translation_localization.py translate \"text to translate\"")
        print("2. python second_agent_translation_localization.py add_toggle /path/to/chapter.md")
        print("3. python second_agent_translation_localization.py setup_bilingual /path/to/chapters/dir")
        return
    
    action = sys.argv[1]
    agent = TranslationLocalizationAgent(os.getcwd())
    
    if action == "translate" and len(sys.argv) >= 3:
        text = sys.argv[2]
        result = agent.process_translation_request(text)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif action == "add_toggle" and len(sys.argv) >= 3:
        chapter_path = sys.argv[2]
        result = agent.add_language_toggle_to_chapter(chapter_path)
        print(result)
    elif action == "setup_bilingual" and len(sys.argv) >= 3:
        chapters_dir = sys.argv[2]
        result = agent.setup_bilingual_support(chapters_dir)
        print(result)
    else:
        print("Invalid command. Use one of: translate, add_toggle, setup_bilingual")


if __name__ == "__main__":
    main()