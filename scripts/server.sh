#!/bin/bash

SERVER="$1"
ACTION="$2"

if [ -z "$SERVER" ] || [ -z "$ACTION" ]; then
    echo "Verwendung:"
    echo "./server.sh <server> <up|down|restart|logs>"
    exit 1
fi

COMPOSE="/srv/docker/compose/games/$SERVER/compose.yaml"

case "$ACTION" in
    up)
        docker compose -f "$COMPOSE" up -d
        ;;
    down)
        docker compose -f "$COMPOSE" down
        ;;
    restart)
        docker compose -f "$COMPOSE" restart
        ;;
    logs)
        docker compose -f "$COMPOSE" logs -f
        ;;
    *)
        echo "Unbekannte Aktion"
        ;;
esac
