import requests
import json
import os
from dotenv import load_dotenv
from app.schemas import Backlog

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("OLLAMA_MODEL")

SYSTEM_PROMPT = """
You are a Senior Product Owner.

Your task:
Convert the PRD into a STRICT JSON agile backlog.

ABSOLUTE RULES (must follow):
- Output ONLY valid JSON
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include ``` fences
- Do NOT include text before or after JSON

Hierarchy:
Epic → User Story → Task → Subtask

User stories MUST use:
"As a <user>, I want <goal>, so that <value>"

IDs:
Epic: E-1, E-2
Story: US-1, US-2
Task: T-1, T-2
Subtask: ST-1, ST-2

JSON FORMAT (EXACT):
{
  "epics": [
    {
      "id": "E-1",
      "name": "Epic name",
      "stories": [
        {
          "id": "US-1",
          "name": "As a ...",
          "tasks": [
            {
              "id": "T-1",
              "name": "Task name",
              "subtasks": [
                {
                  "id": "ST-1",
                  "name": "Subtask name"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
"""

def generate_backlog(prd_text: str) -> Backlog:
    payload = {
        "model": MODEL,
        "prompt": SYSTEM_PROMPT + "\n\nPRD:\n" + prd_text,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    raw_output = response.json().get("response", "").strip()

    print("\n===== RAW LLaMA OUTPUT =====")
    print(raw_output)
    print("===== END OUTPUT =====\n")

    if not raw_output:
        raise ValueError("LLaMA returned empty output")

    # ✅ STEP 1: Remove markdown code fences if present
    if raw_output.startswith("```"):
        raw_output = raw_output.replace("```json", "").replace("```", "").strip()

    # ✅ STEP 2: Extract JSON block safely
    start = raw_output.find("{")
    end = raw_output.rfind("}") + 1

    if start == -1 or end == -1:
        raise ValueError(f"Could not find JSON object in output:\n{raw_output}")

    json_str = raw_output[start:end]

    # ✅ STEP 3: Parse JSON
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON from LLaMA.\nError: {e}\nJSON:\n{json_str}"
        )

    # ✅ STEP 4: Auto-fix empty subtasks (LLM guardrail)
    for epic in data.get("epics", []):
        for story in epic.get("stories", []):
            for task in story.get("tasks", []):
                if not task.get("subtasks"):
                    task["subtasks"] = [
                        {
                            "id": "ST-1",
                            "name": "Define and implement required subtask"
                        }
                    ]

    return Backlog(**data)

