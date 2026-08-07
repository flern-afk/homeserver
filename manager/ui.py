from rich.console import Console
from rich.table import Table

console = Console()


def print_servers(servers, get_info):

    table = Table(title="🎮 Home Server Manager")

    table.add_column("#", justify="right", style="cyan")
    table.add_column("Spiel", style="bold")
    table.add_column("Status")
    table.add_column("Image")

    for i, server in enumerate(servers, start=1):

        info = get_info(server)

        status = (
            "[green]🟢 Running[/green]"
            if info["status"] == "running"
            else "[red]⚫ Stopped[/red]"
        )

        table.add_row(
            str(i),
            info["game"],
            status,
            info["image"]
        )

    console.print(table)
