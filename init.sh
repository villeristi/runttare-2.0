#!/bin/bash

set -ex

# Build docker-compose
docker compose build --no-cache

# Move runttare.service to system-folder
sudo cp ./service/runttare.service /etc/systemd/system/runttare.service

# Enable systemctl-service for runttare
sudo systemctl enable runttare

# Start runttare as service
sudo systemctl start runttare
