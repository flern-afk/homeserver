import docker

from config import LABEL_TYPE, LABEL_GAME, TYPE_GAME

client = docker.from_env()


def get_containers():
    return client.containers.list(all=True)


def get_gameservers():
    return [
        c for c in get_containers()
        if c.labels.get(LABEL_TYPE) == TYPE_GAME
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
        "game": container.labels.get(LABEL_GAME, container.name),
        "status": container.status,
        "image": container.image.tags[0] if container.image.tags else "Unbekannt",
    }


def logs(name, lines=50):
    container = client.containers.get(name)
    return container.logs(tail=lines).decode("utf-8")
