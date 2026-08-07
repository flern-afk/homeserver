import docker

client = docker.from_env()


def get_containers():
    """Alle Docker-Container zurückgeben."""
    return client.containers.list(all=True)


def get_gameservers():
    """Alle Container mit dem Label homeserver.type=game."""
    return [
        c for c in get_containers()
        if c.labels.get("homeserver.type") == "game"
    ]


def get_info(container):
    """Informationen eines Containers als Dictionary zurückgeben."""
    return {
        "name": container.name,
        "game": container.labels.get("homeserver.game", container.name),
        "status": container.status,
        "image": container.image.tags[0] if container.image.tags else "Unbekannt",
    }


def start(name):
    """Container starten."""
    client.containers.get(name).start()


def stop(name):
    """Container stoppen."""
    client.containers.get(name).stop()


def restart(name):
    """Container neu starten."""
    client.containers.get(name).restart()


def logs(name, lines=50):
    """Die letzten Logzeilen eines Containers zurückgeben."""
    container = client.containers.get(name)
    return container.logs(tail=lines).decode("utf-8")


def is_running(name):
    """Prüfen, ob ein Container läuft."""
    container = client.containers.get(name)
    container.reload()
    return container.status == "running"
