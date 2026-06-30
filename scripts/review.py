from pathlib import Path
import requests

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

java_file = PROJECT_ROOT / "sample-project" / "Calculator.java"
prompt_file = PROJECT_ROOT / "prompts" / "review_prompt.txt"
report_file = PROJECT_ROOT / "reports" / "review.md"

# Read Java code
with open(java_file, "r", encoding="utf-8") as f:
    code = f.read()

# Read Prompt
with open(prompt_file, "r", encoding="utf-8") as f:
    prompt = f.read()

prompt = prompt.replace("{{CODE}}", code)

payload = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(
    "http://localhost:11434/api/generate",
    json=payload
)

response.raise_for_status()

result = response.json()["response"]

print(result)

with open(report_file, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\n✅ Review saved to {report_file}")