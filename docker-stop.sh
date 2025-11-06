#!/bin/bash

echo "--- Stopping and removing the container ---"
docker stop kokoro-api-container
docker rm kokoro-api-container
echo "--- Container stopped and removed ---"