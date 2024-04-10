#!/bin/bash

# chmod +x start_services.sh # this to make the script executable
# Start Redis server
redis-server &
# Store the process ID of Redis server
REDIS_PID=$!

# Wait for Redis to initialize (customize based on your needs)
sleep 5

# Generate worker configuration only if Redis started successfully
python3 gen_worker_conf.py && echo "Worker config generated successfully."

# The exit status of the previous command (python3 gen_worker_conf.py) is checked. If it's successful (exit status 0),
# then supervisord is started with the specified configuration.
# If the python script fails, the script exits with an error.
if [ $? -eq 0 ]; then
    supervisord -c supervisord.conf
    echo "Supervisord started successfully."
else
    echo "Failed to generate worker config. Supervisord not started."
    # Optional: stop Redis server if needed
    kill $REDIS_PID
    exit 1
fi
