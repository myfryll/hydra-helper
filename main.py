import wizard
import builder
import runner
import ui
from rich.prompt import Confirm
ui.show_banner()
data = wizard.wizard_main()
command = builder.build_command(data)
ui.show_summary(data)
confirmation = Confirm.ask('Конфигурация верна?')
if confirmation == True:
    runner.run(command)