#!/bin/bash

echo "===== Docker ====="
systemctl is-active docker

echo
echo "===== Container ====="
docker ps --format "table {{.Names}}\t{{.Status}}"

echo
echo "===== Speicher ====="
free -h

echo
echo "===== Festplatte ====="
df -h /
