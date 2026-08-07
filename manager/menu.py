from docker_client import (
    get_gameservers,
    get_info,
    start,
    stop,
    restart,
)


def show_servers():
    servers = get_gameservers()

    print()
    print("========================================")
    print("         Home Server Manager")
    print("========================================")

    for i, server in enumerate(servers, start=1):
        info = get_info(server)

        icon = "🟢" if info["status"] == "running" else "⚫"

        print(f"{i}. {info['game']:15} {icon} {info['status']}")

    print()
    print("0. Beenden")
    print()

    return servers


def server_menu(server):
    while True:

        info = get_info(server)

        print()
        print(f"===== {info['game']} =====")
        print(f"Status : {info['status']}")
        print(f"Image  : {info['image']}")
        print()

        print("1. Start")
        print("2. Stop")
        print("3. Restart")
        print("0. Zurück")
        print()

        choice = input("Auswahl: ")

        if choice == "1":
            start(server.name)
            return

        elif choice == "2":
            stop(server.name)
            return

        elif choice == "3":
            restart(server.name)
            return

        elif choice == "0":
            return

        else:
            print("Ungültige Eingabe")


def menu():

    while True:

        servers = show_servers()

        choice = input("Server auswählen: ")

        if choice == "0":
            break

        try:
            server = servers[int(choice) - 1]
        except (ValueError, IndexError):
            print("Ungültige Eingabe")
            continue

        server_menu(server)
