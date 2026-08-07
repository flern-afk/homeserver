#!/bin/bash

set -e

BACKUP_DIR="/srv/docker/backups"
DATE=$(date +"%Y-%m-%d_%H-%M")

mkdir -p "$BACKUP_DIR"

echo "Erstelle Backup..."

tar -czf "$BACKUP_DIR/docker_$DATE.tar.gz" \
    /srv/docker/compose \
    /srv/docker/data \
    /srv/docker/docs

echo "Backup gespeichert unter:"
echo "$BACKUP_DIR/docker_$DATE.tar.gz"
