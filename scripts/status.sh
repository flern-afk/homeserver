#!/bin/bash

echo "=============================="
echo " Home Server Status"
echo "=============================="
echo

echo "Docker:"
systemctl is-active docker
echo

echo "Container:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "Speicher:"
free -h

echo
echo "Festplatte:"
df -h /

echo
echo "CPU:"
uptime
