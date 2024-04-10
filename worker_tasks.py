import cv2 # Is this import really causing the issue?


from models import FeedbackTask
# from typing import Dict, Any

def process_A_Task(task: FeedbackTask) -> FeedbackTask:
    # Accessing properties directly with types enforced by Pydantic
    user_id = task.user_id

    import time
    time.sleep(5)  # Simulate a delay to mimic a long-running task
    return task

def process_B_Task(task: FeedbackTask) -> None:
    # Accessing properties directly with types enforced by Pydantic
    user_id = task.user_id

    import time
    time.sleep(5)  # Simulate a delay to mimic a long-running task
