.PHONY: help ps status backup update start stop restart logs web cli

SERVER ?= enshrouded

help:
	@echo ""
	@echo "===== Home Server ====="
	@echo ""
	@echo "make status"
	@echo "make ps"
	@echo "make backup"
	@echo "make update"
	@echo ""
	@echo "make logs SERVER=enshrouded"
	@echo "make restart SERVER=enshrouded"
	@echo "make stop SERVER=enshrouded"
	@echo "make start SERVER=enshrouded"
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
	./scripts/server.sh $(SERVER) logs

start:
	./scripts/server.sh $(SERVER) up

stop:
	./scripts/server.sh $(SERVER) down

restart:
	./scripts/server.sh $(SERVER) restart

web:
	cd manager && . .venv/bin/activate && python -m uvicorn web:app --reload

cli:
	cd manager && . .venv/bin/activate && python cli.py
