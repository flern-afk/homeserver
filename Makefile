.PHONY: help ps status backup update start stop restart logs

SERVER ?= enshrouded

help:
	@echo ""
	@echo "Home Server"
	@echo "=============================="
	@echo "make ps"
	@echo "make status"
	@echo "make backup"
	@echo "make update"
	@echo ""
	@echo "make logs SERVER=enshrouded"
	@echo "make restart SERVER=minecraft"
	@echo ""

ps:
	docker ps

status:
	./scripts/status.sh

backup:
	./scripts/backup.sh

update:
	./scripts/update.sh

logs:
	docker logs -f $(SERVER)

start:
	docker start $(SERVER)

stop:
	docker stop $(SERVER)

restart:
	docker restart $(SERVER)
SERVER ?= enshrouded

logs:
	./scripts/server.sh $(SERVER) logs

restart:
	./scripts/server.sh $(SERVER) restart
