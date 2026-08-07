.PHONY: help status backup update logs ps restart stop start git

help:
	@echo ""
	@echo "===== Home Server ====="
	@echo ""
	@echo "make status     Systemstatus anzeigen"
	@echo "make backup     Backup erstellen"
	@echo "make update     System aktualisieren"
	@echo "make ps         Docker Container"
	@echo "make logs       Enshrouded Logs"
	@echo "make start      Enshrouded starten"
	@echo "make stop       Enshrouded stoppen"
	@echo "make restart    Enshrouded neu starten"
	@echo ""

status:
	./scripts/status.sh

backup:
	./scripts/backup.sh

update:
	./scripts/update.sh

ps:
	docker ps

logs:
	docker logs -f enshrouded

start:
	docker start enshrouded

stop:
	docker stop enshrouded

restart:
	docker restart enshrouded

health:
	./scripts/health.sh
