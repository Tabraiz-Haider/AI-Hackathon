#!/usr/bin/env python3
"""
First Agent - History Keeper
Responsibilities:
- Continuously maintains project history
- Saves all changes, instructions, and prompts to history/prompts/general/
- Follows the existing history format
- Performs only explicit instructions (reactive, not autonomous)
"""

import os
import sys
from datetime import datetime
from pathlib import Path


class HistoryKeeperAgent:
    """
    An agent that maintains project history by saving all changes, instructions,
    and prompts to the history/prompts/general/ folder in the existing format.
    """
    
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.history_dir = self.project_root / "history" / "prompts" / "general"
        self.history_dir.mkdir(parents=True, exist_ok=True)
        
    def get_next_prompt_id(self):
        """Get the next available prompt ID based on existing files."""
        existing_files = list(self.history_dir.glob("*.general.prompt.md"))
        if not existing_files:
            return "110"  # Starting after the current highest number
            
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
model: first-agent-history-keeper
feature: none
branch: main
user: user
command: none
labels: ["history", "agent"]
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
    
    def process_instruction(self, instruction):
        """
        Process an instruction by saving it to history and returning a response.
        This agent only acts when explicitly instructed.
        """
        # Save the instruction to history
        response = f"First Agent acknowledged instruction: {instruction}"
        outcome = f"- ✅ Action: Saved instruction to history\n- 🧠 Reflection: Instruction processed reactively as required."
        
        history_path = self.save_prompt_history(
            prompt=instruction,
            response=response,
            outcome=outcome
        )
        
        return f"Instruction processed. History saved to: {history_path}"


def main():
    """
    Main function to run the History Keeper Agent.
    Expects a prompt/instruction as command line argument.
    """
    if len(sys.argv) < 2:
        print("Usage: python first_agent_history_keeper.py \"<instruction>\"")
        print("The agent only acts when given explicit instructions.")
        return
    
    instruction = " ".join(sys.argv[1:])
    
    # Initialize the agent
    agent = HistoryKeeperAgent(os.getcwd())
    
    # Process the instruction
    result = agent.process_instruction(instruction)
    print(result)


if __name__ == "__main__":
    main()