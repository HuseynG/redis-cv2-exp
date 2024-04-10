from pydantic import BaseModel, Field, validator
import os
from redis_settings import workers_settings


class WorkerSetting(BaseModel):
    type: str
    amount: int = Field(ge=1)  # Ensure amount is at least 1
    log_dir: str
    q: str

    # Validate log_dir exists or create it
    @validator('log_dir', pre=True, always=True)
    def validate_log_dir(cls, v):
        if not os.path.exists(v):
            os.makedirs(v)
            print(f"Directory '{v}' was created.")
        else:
            print(f"Directory '{v}' already exists.")
        return v

class SupervisordConfig(BaseModel):
    workers: list[WorkerSetting]
    supervisord_template: str = """
[supervisord]
nodaemon=true
"""

    def generate_config(self):
        config_str = self.supervisord_template
        for worker in self.workers:
            for i in range(worker.amount):
                program = f"{worker.type}_{i}"
                command = f'rq worker {worker.q} --name {worker.type}_{i}'
                config_str += f"""
[program:{program}]
command={command}
stdout_logfile={worker.log_dir}/{program}.log
stderr_logfile={worker.log_dir}/{program}_err.log
autorestart=true
stopasgroup=true
stopsignal=TERM
"""
        return config_str


supervisord_config = SupervisordConfig(workers=[WorkerSetting(**ws) for ws in workers_settings])
config_str = supervisord_config.generate_config()

# Write the filled template to supervisord.conf
with open('supervisord.conf', 'w') as file:
    file.write(config_str)

print("supervisord.conf generated.")
