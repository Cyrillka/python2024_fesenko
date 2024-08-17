from copy import deepcopy

from scrapli import Scrapli
from scrapli.driver import GenericDriver
from scrapli.exceptions import (ScrapliAuthenticationFailed,
                                ScrapliConnectionError, ScrapliException,
                                ScrapliTransportPluginError)

device = {
    "platform": "cisco_iosxe",
    "host": "192.168.100.111",
    "auth_username": "admin",
    "auth_password": "passw0rd",
    "auth_secondary": "enpass",
    "auth_strict_key": False,
    "transport": "telnet",
    
}
def check_priviledge(device: dict[str, str]) -> str:
    params = deepcopy(device)
    for i in ["platform", "auth_secondary"]:
        del params[i]
    with GenericDriver(**params,) as conn:
        prompt = conn.get_prompt()
        if prompt.endswith(">"):
            return {"default_desired_privilege_level" : "exec"}
        else:
            return {"default_desired_privilege_level" : "privilege_exec"}

def get_output(device: dict[str, str], command: str) -> str:
    priveledge = check_priviledge(device)
    device |= priveledge
    try:
        with Scrapli(**device, privilege_levels=None) as conn:
            output = conn.send_command(command, failed_when_contains="%")
        if output.failed:
            print(f"Ошибка в сборе команды:\n{output.channel_input}\n{output.result}")
            return ''
        else:
            return output
    except ScrapliAuthenticationFailed:
        print(f"Неправильные логин/пароль для устройства {device['host']}" )
    except (ScrapliConnectionError, ScrapliTransportPluginError):
        print(f"Таймаут подключения к устройству {device['host']}")
    except ScrapliException as some_except:
        print(f"Неизвестное исключение при работе с устройством {device['host']} : {str(some_except)}")
    return ''
   

if __name__ == "__main__":
    command = "show runn"
    print(get_output(device, command))