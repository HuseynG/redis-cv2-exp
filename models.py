from typing import List, Optional
from pydantic import BaseModel
from fastapi import UploadFile

class FeedbackTask(BaseModel):
    user_id: str
