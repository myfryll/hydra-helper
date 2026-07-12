from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.prompt import IntPrompt
def wizard_main():
    target = Prompt.ask('Введите [bold green]IP-адрес[/bold green] цели или [bold green]доменное имя[/bold green] ',)
    service = Prompt.ask('Укажите сервис для атаки ([bold green]ssh, ftp, http-get, http-post[/bold green]) ').strip().lower()
    http_data = {}
    if service in ("http-get","http-post"):
        http_data = ask_http_options()
    login_mode = Prompt.ask('Как вы хотите указать логины?\n1)Один логин\n2)Wordlist логинов\nВыберите',choices=['1','2'])
    login = None
    login_wordlist = None
    password = None
    password_wordlist = None
    if login_mode == '1':
        login = Prompt.ask('Введите логин ')
    else:
        login_wordlist = Prompt.ask('Введите путь до wordlist с логинами ')
    
    password_mode = Prompt.ask('Как вы хотите указать пароли?\n1)Один пароль\n2)Wordlist паролей\nВыберите',choices=['1','2'])    
    if password_mode == '1':
        password = Prompt.ask('Введите пароль ')
    
    else:
        password_wordlist = Prompt.ask('Введите путь до wordlist с паролями ')
        
    port = IntPrompt.ask('Введите порт (Enter = порт по умолчанию)',default='')
    threads = IntPrompt.ask('Введите количество потоков ')
    verbose = Confirm.ask("Показывать каждую попытку?")
    stop_on_success = Confirm.ask('Остановиться после первой найденной пары?')
    return {    
        "target":target,
        "service":service,
        "http_data":http_data,
        "login":login,
        "login_wordlist":login_wordlist,
        "password":password,
        "password_wordlist":password_wordlist,
        "port":port,
        "threads":threads,
        "verbose":verbose,
        "stop_on_success":stop_on_success
    }

def ask_http_options():
    path = Prompt.ask('Введите путь до формы авторизации (включая /) ')
    user_field = Prompt.ask('Как называется поле логина? ')
    pass_field = Prompt.ask('Как называется поле пароля? ')
    failure_string = Prompt.ask('Строка ошибки ')
    return {
        "path":path,
        "user_field":user_field,
        "pass_field":pass_field,
        "failure_string":failure_string
    }
        

