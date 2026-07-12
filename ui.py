from rich import box
from rich.console import Console
from rich.table import Table

console = Console()


def show_summary(data):
    
    table = Table(
        title="[bold cyan]⚙️ Конфигурация запуска[/bold cyan]",
        box=box.ROUNDED,
        header_style="bold magenta",
        title_justify="left",
    )

    
    table.add_column("Параметр", style="bold white", width=20)
    table.add_column("Значение", style="green")

    
    table.add_row("Target", f"[bold yellow]{data['target']}[/bold yellow]")
    table.add_row("Service", data["service"])

    
    if data["login"] is not None:
        table.add_row("Login Mode", "Single Login")
        table.add_row("Login", f"[bold green]{data['login']}[/bold green]")
    else:
        table.add_row("Login Mode", "[italic dim]Wordlist[/italic dim]")
        table.add_row(
            "Login list", f"[yellow]{data['login_wordlist']}[/yellow]"
        )

    
    if data["password"] is not None:
        table.add_row("Password Mode", "Single Password")
        table.add_row(
            "Password", f"[italic bold green]{data['password']}[/italic bold green]"
        )
    else:
        table.add_row("Password Mode", "[italic dim]Wordlist[/italic dim]")
        table.add_row(
            "Password list", f"[yellow]{data['password_wordlist']}[/yellow]"
        )

    
    if data["port"]:
        table.add_row("Port", str(data["port"]))
    else:
        table.add_row("Port", "[dim]Default[/dim]")
   
    table.add_row("Threads", f"[bold cyan]{data['threads']}[/bold cyan]") 
    table.add_row("Verbose", str(data["verbose"]))
    table.add_row("Stop on success", str(data["stop_on_success"]))

    
    console.print(table)
    
    
def show_banner():
    banner = r"""
    ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗
    ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗
    ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║
    ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║
    ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    """

    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print(
        "[bold white]           Hydra Helper[/bold white] "
        "[dim]v0.1[/dim]"
    )
    console.print("[dim]                 by myfryll[/dim]\n")