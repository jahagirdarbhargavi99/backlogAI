# BacklogAI 🧠📋  
**AI Product Owner for PRD → Agile Backlogs**

BacklogAI is an AI-powered Product Owner that converts Product Requirement Documents (PRDs) into a structured agile backlog consisting of **Epics, User Stories, Tasks, and Subtasks**.  
The generated backlog is validated, normalized, and automatically published to **Google Sheets**.

---

## ✨ Features
- PRD → Epics → Stories → Tasks → Subtasks
- LLaMA-based local inference (via Ollama)
- Defensive JSON parsing & schema validation
- Auto-repair of malformed LLM outputs
- Google Sheets integration
- FastAPI backend

---

## 🛠️ Tech Stack
- Python, FastAPI  
- LLaMA (Ollama)  
- Pydantic  
- Google Sheets API  

---

## ▶️ Run Locally

python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload

## ▶️ Run the Application

Open:
http://127.0.0.1:8000/docs


Run:
- POST /generate

---

## 🔐 Configuration

Create a `.env` file using `.env.example`.  
Service account keys and secrets are excluded from version control.

---

## 👤 Author

**Bhargavi Jahagirdar**  
GitHub: https://github.com/jahagirdarbhargavi99
