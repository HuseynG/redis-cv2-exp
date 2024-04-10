# Redis-CV2-Exp Project

This project is designed to demonstrate specific functionalities using Redis and FastAPI. Follow the instructions below for setup and execution on your local machine.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Python 3.9.18
- Redis server

## Setup Instructions

### Python Virtual Environment

1. **Create a Virtual Environment:** Open a terminal, navigate to the project's root directory, and create a virtual environment by running:

   ```bash
   python -m venv myenv

2. **Activate the Virtual Environment:**

- **On Windows**, run:

  ```bash
  myenv\Scripts\activate

- **On Mac**, run:

  ```bash
    source myenv/bin/activate

3. **Installing Dependencies:**

```pip install -r requirements.txt```

### Running the Application: 
To start both the Redis server and the FastAPI application, execute the script provided in the project:
```
./scripts/run_all.sh
```
This script initializes the necessary components for the application to run.

### Monitoring Workers:

To check the status of the workers, use the rq info command:

   ```bash
   rq info
