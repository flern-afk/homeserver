# Installation

## Betriebssystem

- Kubuntu

## Docker

Installation:

```bash
sudo apt install docker.io docker-compose-v2
```

Docker starten:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Benutzer zur Docker-Gruppe:

```bash
sudo usermod -aG docker $USER
```

Abmelden und wieder anmelden.

## Portainer

Läuft auf:

http://localhost:9000
