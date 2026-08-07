from docker_client import get_gameservers, start, stop


def menu():

    while True:

        servers = get_gameservers()

        print()
        print("================================")
        print(" Home Server Manager")
        print("================================")
        print()

        for i, server in enumerate(servers, start=1):

            icon = "🟢" if server.status == "running" else "⚫"

            print(f"{i}. {server.name:20} {icon} {server.status}")

        print()
        print("0. Beenden")
        print()

        choice = input("Server auswählen: ")

        if choice == "0":
            break

        try:

            server = servers[int(choice)-1]

        except (ValueError, IndexError):

            print("Ungültige Eingabe.")
            continue

        print()
        print(f"{server.name}")
        print("----------------------")
        print("1. Start")
        print("2. Stop")
        print("3. Restart")
        print()

        action = input("Aktion: ")

        if action == "1":
            start(server.name)

        elif action == "2":
            stop(server.name)

        elif action == "3":
            restart(server.name)
