def add_option(command, user_data, single_key, list_key, single_flag, list_flag):
    if user_data[single_key] != None:
        command.extend([single_flag, user_data[single_key]])
    else:
        command.extend([list_flag, user_data[list_key]])

def build_command(user_data):
    command = ['hydra']
    add_option(
        command,
        user_data,
        "login",
        "login_wordlist",
        "-l",
        "-L"
    )

    add_option(
        command,
        user_data,
        "password",
        "password_wordlist",
        "-p",
        "-P"
    )
    command.extend(['-t', str(user_data["threads"])])
    
    if user_data["port"]:
        command.extend(["-s", str(user_data["port"])])
    if user_data["verbose"]:
        command.append('-v')
    
    if user_data["stop_on_success"]:
        command.append('-f')   
        
    
    if user_data["service"].startswith("http-"):
        http = user_data['http_data']
        module = f"{user_data['service']}-form"
        command.extend([user_data["target"], module, f"{http['path']}:{http['user_field']}=^USER^&{http['pass_field']}=^PASS^:F={http['failure_string']}"])
        
    else:
        command.append(f'{user_data["service"]}://{user_data["target"]}')
    return command
    
    

