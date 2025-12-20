import os
import datetime
import re
import argparse
from pathlib import Path

# Define the root of the project
PROJECT_ROOT = Path(__file__).parent.resolve()
PHR_TEMPLATE_PATH = PROJECT_ROOT / ".specify" / "templates" / "phr-template.prompt.md"
HISTORY_DIR = PROJECT_ROOT / "history" / "prompts"

def get_template_content():
    """Reads the content of the PHR template."""
    try:
        with open(PHR_TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {PHR_TEMPLATE_PATH}")
        return None

def get_next_phr_id(directory):
    """Finds the next available PHR ID in a given directory."""
    max_id = 0
    for filename in os.listdir(directory):
        if match := re.match(r"(\d+)-.*\.md", filename):
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1

def read_content_from_file(filepath):
    """Reads content from a given file path."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Content file not found at {filepath}")
        return ""

def create_phr_entry(stage, title, user_prompt_path, agent_response_path, feature=None, files_yaml="- none", tests_yaml="- none"):
    """Creates a new PHR entry."""
    template = get_template_content()
    if not template:
        return None

    user_prompt = read_content_from_file(user_prompt_path)
    agent_response = read_content_from_file(agent_response_path)

    slug = re.sub(r"[^\w-]", "", title.lower().replace(" ", "-"))
    
    if stage == "constitution":
        target_dir = HISTORY_DIR / "constitution"
    elif feature and stage != "general":
        target_dir = HISTORY_DIR / feature
    else:
        stage = "general"
        target_dir = HISTORY_DIR / "general"
        
    os.makedirs(target_dir, exist_ok=True)
    
    phr_id = get_next_phr_id(target_dir)
    
    filename = f"{phr_id:03d}-{slug}.{stage}.prompt.md"
    filepath = target_dir / filename

    # Replace placeholders
    content = template
    content = content.replace("{{ID}}", str(phr_id))
    content = content.replace("{{TITLE}}", title)
    content = content.replace("{{STAGE}}", stage)
    content = content.replace("{{DATE_ISO}}", datetime.datetime.now().strftime("%Y-%m-%d"))
    content = content.replace("{{SURFACE}}", "agent")
    content = content.replace("{{MODEL}}", "gemini-cli") # Placeholder
    content = content.replace("{{FEATURE}}", feature or "none")
    content = content.replace("{{BRANCH}}", "main") # Placeholder
    content = content.replace("{{USER}}", "user") # Placeholder
    content = content.replace("{{COMMAND}}", "user_prompt") # Placeholder - this needs to be fixed to reflect the actual command/prompt
    content = content.replace("{{LABELS}}", '["history-mechanism"]') # Placeholder
    content = content.replace("{{LINKS}}", "null")
    content = content.replace("{{FILES_YAML}}", files_yaml)
    content = content.replace("{{TESTS_YAML}}", tests_yaml)
    content = content.replace("{{PROMPT_TEXT}}", user_prompt)
    content = content.replace("{{RESPONSE_TEXT}}", agent_response)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully created PHR entry: {filepath}")
        return str(filepath)
    except IOError as e:
        print(f"Error writing PHR file: {e}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a new Prompt History Record (PHR) entry.")
    parser.add_argument("--stage", required=True, help="The stage of the prompt (e.g., general, constitution).")
    parser.add_argument("--title", required=True, help="The title of the PHR entry.")
    parser.add_argument("--user_prompt_path", required=True, help="Path to a file containing the full text of the user's prompt.")
    parser.add_argument("--agent_response_path", required=True, help="Path to a file containing the key output or response from the agent.")
    parser.add_argument("--feature", help="The feature name if applicable.")
    parser.add_argument("--files_yaml", default="- none", help="YAML formatted list of created/modified files.")
    parser.add_argument("--tests_yaml", default="- none", help="YAML formatted list of tests run/added.")

    args = parser.parse_args()

    create_phr_entry(
        stage=args.stage,
        title=args.title,
        user_prompt_path=args.user_prompt_path,
        agent_response_path=args.agent_response_path,
        feature=args.feature,
        files_yaml=args.files_yaml,
        tests_yaml=args.tests_yaml
    )
