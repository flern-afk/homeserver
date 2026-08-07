# 🖥️ Home Server

## Hardware

| Komponente | Wert |
|------------|------|
| Notebook | Samsung Galaxy Book 5 Pro |
| OS | Kubuntu |
| RAM | 16 GB |

---

## Dienste

| Dienst | Port | Status |
|---------|------|--------|
| Portainer | 9000 | ✅ |
| Cockpit | 9090 | ✅ |
| Enshrouded | 15637 UDP | ✅ |

---

## Verzeichnisstruktur

compose/
data/
docs/
scripts/
backups/

---

## Wartung

Backup

```bash
make backup
```

Status

```bash
make status
```

Update

```bash
make update
```
