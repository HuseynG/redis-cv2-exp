from fastapi import FastAPI, UploadFile, File, Query

from typing import List, Optional

from models import FeedbackTask
import redis_processes as redis_processes


app = FastAPI()

@app.post("/processfeedback/")
async def process_feedback(
    user_id: str = Query(..., description="User ID submitting the document"),):

    """
    ...func explanation...

    Args:
        user_id (str): User ID submitting the document.
    Returns:
        ...
    """

    # Create an instance of the Pydantic model
    feedback_task = FeedbackTask(
        user_id=user_id,
    )

    return redis_processes.process_feedback(feedback_task)
