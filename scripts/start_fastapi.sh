#!/bin/bash

# chmod +x start_fastapi.sh # this to make the script executable

echo "Starting FastAPI application with Uvicorn..."
uvicorn server:app --reload --port 8000
