import docker

client = docker.from_env()


def get_containers():
    return client.containers.list(all=True)


def get_gameservers():
    ignore = {
        "portainer",
        "homepage",
    }

    return [
        c for c in get_containers()
        if c.name not in ignore
    ]


def start(name):
    client.containers.get(name).start()


def stop(name):
    client.containers.get(name).stop()


def restart(name):
    client.containers.get(name).restart()
