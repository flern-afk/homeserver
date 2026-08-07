#!/bin/bash

echo "System aktualisieren..."

sudo apt update
sudo apt upgrade -y

echo
echo "Docker Images aktualisieren..."

docker compose -f /srv/docker/compose/portainer/compose.yaml pull
docker compose -f /srv/docker/compose/portainer/compose.yaml up -d

docker compose -f /srv/docker/compose/enshrouded/compose.yaml pull
docker compose -f /srv/docker/compose/enshrouded/compose.yaml up -d

echo
echo "Fertig."
