from pyfiglet import Figlet
from rich.console import Console

console = Console()

fig = Figlet(font="slant")
console.print(f"[cyan]{fig.renderText('Hydra Helper')}[/cyan]")
console.print("[bold white]by myfryll[/bold white]")