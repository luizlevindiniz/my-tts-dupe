#!/bin/bash

# Stop and remove any old container with the same name
echo "--- Stopping and removing old container (if any) ---"
docker stop kokoro-api-container 2>/dev/null
docker rm kokoro-api-container 2>/dev/null

# Build the new image
echo "--- Building Docker image ---"
docker build -t kokoro-api .

# Run the new container in detached mode
echo "--- Starting new container in background ---"
docker run -d -p 8000:8000 --name kokoro-api-container kokoro-api

echo "--- Container is running! ---"
echo "Test it at: http://localhost:8000/"
echo "To see logs, run: docker logs -f kokoro-api-container"