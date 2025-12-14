from fastapi import FastAPI
from app.llm import generate_backlog
from app.validator import validate_backlog
from app.sheets import write_to_sheet
from app.utils import load_prd

app = FastAPI(title="BacklogAI")

@app.post("/generate")
def generate_backlog_endpoint():
    prd = load_prd()
    backlog = generate_backlog(prd)
    validate_backlog(backlog)
    write_to_sheet(backlog)

    return {"status": "Backlog generated and written to Google Sheets"}
