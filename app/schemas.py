from pydantic import BaseModel
from typing import List

class Subtask(BaseModel):
    id: str
    name: str

class Task(BaseModel):
    id: str
    name: str
    subtasks: List[Subtask]

class UserStory(BaseModel):
    id: str
    name: str
    tasks: List[Task]

class Epic(BaseModel):
    id: str
    name: str
    stories: List[UserStory]

class Backlog(BaseModel):
    epics: List[Epic]
