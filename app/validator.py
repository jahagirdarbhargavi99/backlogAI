from app.schemas import Backlog

def validate_backlog(backlog: Backlog):
    if not backlog.epics:
        raise ValueError("No epics generated")

    for epic in backlog.epics:
        if not epic.stories:
            raise ValueError(f"{epic.id} has no stories")

        for story in epic.stories:
            if not story.tasks:
                raise ValueError(f"{story.id} has no tasks")

            for task in story.tasks:
                if not task.subtasks:
                    raise ValueError(f"{task.id} has no subtasks")
