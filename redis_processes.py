import redis
from rq import Queue
from redis_settings import workers_settings

import threading

import time
from datetime import datetime

from models import FeedbackTask
import worker_tasks as worker_tasks



# Set up Redis connection
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

Task_A_Processor_Q        = Queue(name= workers_settings[0]['q'],connection=redis_conn)
Task_B_Processor_Q        = Queue(name= workers_settings[1]['q'],connection=redis_conn)


def process_feedback(feedback_process_task: FeedbackTask):
    # tasks.process_feedback(feedback_task)
    now = datetime.now()

    job_a = Task_A_Processor_Q.enqueue(worker_tasks.process_A_Task, feedback_process_task, result_ttl=-1)
    job_b   = Task_B_Processor_Q.enqueue(worker_tasks.process_B_Task, feedback_process_task, result_ttl=-1)

    # return {"job_id": job_ai.get_id()}
    return {"AI Feedback Process Job Status": job_a.get_status(),
            "Raw Document Collection Write Status": job_b.get_status()}

def some_update_func(job_result):
    return "some logic"


def monitor_Task_A_Processor_Q():
    while True:

        # enqueue a taks to update db
        print(Task_A_Processor_Q.finished_job_registry.get_job_ids())


        for job_id in Task_A_Processor_Q.finished_job_registry.get_job_ids():
            job = Task_A_Processor_Q.fetch_job(job_id)
            if job is not None and job.is_finished:

                # print("Job result from AI that is being transferred and removed.",job.result)
                some_update_func(job.result)
                # Remove the job from Redis and all registries
                job.delete()
                # print(job.id)  # Return the ID of the removed job

        # Sleep to prevent constant polling
        time.sleep(10)

# Run the monitoring in a separate thread
def start_monitoring():
    t = threading.Thread(target=monitor_Task_A_Processor_Q)
    t.daemon = True  # Daemonize thread
    t.start()

# Call this function at the start of your application
start_monitoring()