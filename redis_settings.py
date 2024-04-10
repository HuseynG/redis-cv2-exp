log_dir = "logs"
workers_settings = [
    {"type": "Task_A_Processor", "amount": 2, "log_dir": log_dir, "q": "Task_A_Processor_Q"},
    {"type": "Task_B_Processor", "amount": 1, "log_dir": log_dir, "q": "Task_A_Processor_Q"},
]