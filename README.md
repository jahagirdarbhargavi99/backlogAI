# BacklogAI — AI-Powered PRD to Agile Backlog Generator

An agentic AI workflow that reads a Product Requirements Document (PRD) and autonomously generates a complete, structured Agile backlog — Epics, User Stories, Tasks, and Subtasks — then publishes it directly to Google Sheets.

**Eliminates manual Agile planning breakdown. What takes a team hours takes BacklogAI seconds.**

---

## The problem it solves

Writing a PRD is the easy part. Breaking it down into a properly structured Agile backlog — with epics, stories, acceptance criteria, tasks, and subtasks — is tedious, inconsistent, and time-consuming. BacklogAI automates that entire breakdown using LLM-powered reasoning, with schema validation to ensure the output is clean and ready to use.

---

## How it works

```
PRD Input → LLaMA Agent → Epics → User Stories → Tasks → Subtasks
                ↓                                              ↓
         JSON Validation                            Google Sheets (auto-populated)
         + Auto-repair
```

1. **PRD ingestion** — paste or upload your product requirements document
2. **LLM reasoning** — LLaMA (via Ollama) decomposes the PRD into structured Agile items
3. **Schema validation** — Pydantic validates the output; malformed responses are auto-repaired
4. **Google Sheets export** — the full backlog is automatically published, ready for sprint planning

---

## Tech stack

| Layer | Tools |
|---|---|
| LLM | LLaMA (via Ollama — runs locally) |
| Backend | Python, FastAPI |
| Validation | Pydantic, defensive JSON parsing |
| Output | Google Sheets API |
| API docs | Swagger UI (/docs) |

---

## Project structure

```
backlogAI/
├── app/
│   └── main.py              # FastAPI app + POST /generate endpoint
├── prd.txt                  # Sample PRD for testing
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup

```bash
git clone https://github.com/jahagirdarbhargavi99/backlogAI
cd backlogAI
python -m venv venv && venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

Configure your environment:
```bash
cp .env.example .env
# Add your Google Sheets service account credentials
```

Make sure Ollama is running locally with LLaMA:
```bash
ollama run llama3
```

Start the server:
```bash
python -m uvicorn app.main:app --reload
```

Open Swagger UI: `http://127.0.0.1:8000/docs`

Use `POST /generate` with your PRD text to generate the full backlog.

---

## Sample output

Given a PRD, BacklogAI generates:

```json
{
  "epics": [
    {
      "title": "User Authentication",
      "stories": [
        {
          "title": "As a user, I can log in with email and password",
          "tasks": ["Build login form", "Implement JWT auth", "Write unit tests"],
          "acceptance_criteria": "User is redirected to dashboard on successful login"
        }
      ]
    }
  ]
}
```

---

## What's next

- Jira and Linear integration for direct ticket creation
- Support for uploading PRDs as PDF or DOCX
- Configurable story point estimation
- Multi-model support (GPT-4, Gemini)

---

*Built by [Bhargavi Jahagirdar](https://www.linkedin.com/in/bhargavi-jahagirdar/) · GPL-3.0 License*
