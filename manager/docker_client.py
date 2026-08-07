import docker

client = docker.from_env()


def get_containers():
    return client.containers.list(all=True)


def get_gameservers():
    return [
        c for c in client.containers.list(all=True)
        if c.labels.get("homeserver.type") == "game"
    ]

def start(name):
    client.containers.get(name).start()


def stop(name):
    client.containers.get(name).stop()


def restart(name):
    client.containers.get(name).restart()


def get_info(container):

    return {
        "name": container.name,
        "game": container.labels.get("homeserver.game", container.name),
        "status": container.status,
        "image": container.image.tags[0] if container.image.tags else "Unbekannt"
    }
