import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def write_to_sheet(backlog):
    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE"),
        scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=creds)
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    rows = [
        ["Epic ID", "Epic Name", "Story ID", "User Story",
         "Task ID", "Task", "Subtask ID", "Subtask"]
    ]

    for epic in backlog.epics:
        for story in epic.stories:
            for task in story.tasks:
                for subtask in task.subtasks:
                    rows.append([
                        epic.id,
                        epic.name,
                        story.id,
                        story.name,
                        task.id,
                        task.name,
                        subtask.id,
                        subtask.name
                    ])

    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range="Sheet1!A1",
        valueInputOption="RAW",
        body={"values": rows}
    ).execute()
