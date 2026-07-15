import wizard
import builder
import runner
import ui
import profiles
from rich.prompt import Confirm
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import IntPrompt
def execute_attack():
    confirmation = Confirm.ask('Запустить команду?')
    if confirmation:
        runner.run(command)
    
ui.show_banner()
mode = Prompt.ask('1)Новый запуск\n2)Профили\nВыберите', choices=['1','2'])
if mode == '1':
    data = wizard.wizard_main()
    command = builder.build_command(data)
    ui.show_summary(data)
    save_profile = Confirm.ask('Сохранить профиль?')
    if save_profile:
        profile_name = Prompt.ask('Введите название профиля')
        profiles.save_profile(profile_name,data)
        ui.success_message('Профиль успешно сохранен!')
    execute_attack()
elif mode == '2':
    profiles_list = profiles.get_profiles()
    ui.show_profiles(profiles_list)
    number = IntPrompt.ask('Введите номер профиля для загрузки ')
    profile_name = profiles_list[number - 1]
    data = profiles.load_profile(profile_name)
    ui.success_message('Профиль успешно загружен!')
    command = builder.build_command(data)
    ui.show_summary(data)
    execute_attack()
    
    
    

    

