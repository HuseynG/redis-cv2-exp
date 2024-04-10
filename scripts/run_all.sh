#!/bin/bash

# Define the base directory as the directory where this script resides
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Navigate to the base directory of your project
cd $BASE_DIR/..
# Assuming the Python script and supervisord.conf are in the base directory

# Set executable permissions for the scripts (now using absolute paths)
chmod +x "$BASE_DIR/start_redis.sh"
chmod +x "$BASE_DIR/start_fastapi.sh"

# Start the Redis-related tasks and move to the background
"$BASE_DIR/start_redis.sh" &

# Wait a bit for the first script to properly start up services
sleep 10

# Now start the FastAPI application
"$BASE_DIR/start_fastapi.sh"
