import re
from textwrap import dedent

from jinja2 import Template
from netmiko import (ConnectHandler, NetmikoAuthenticationException,
                     NetmikoTimeoutException, ReadTimeout)
from netmiko.utilities import structured_data_converter

#В темплейте поменял имя переменной чтобы совпадало с результатом textfsm, а не генерить новый словарь
template = Template(
    dedent(
        """
        interface {{ intf }} 
         no ip redirects
         no ip unreachables
         no ip proxy-arp
        exit        
        """
    ).strip()
)
device = {
    "device_type": "cisco_xe",
    "host": "192.168.100.101",
    "username": "admin",
    "password": "passw0rd",
    "secret": "enpass",
}
regex = "% (?P<error>.+)"

def device_connect(device: dict[str, str], command, *, mode: str):
    """
    Отдельная функция для подключения к оборудованию и обработки исключений
    """
    if mode is None:
        raise ValueError("Не задан режим работы с оборудованием")
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            if mode == "post":
                output = ssh.send_config_set(command, error_pattern="%")
                return True
            #Сначала так сделал, потом понял что с error pattern проще
            #    error_in_output = re.search(regex, output)
            #    if error_in_output:
            #        print(f"Ошибка при настройке устройства {device['host']}\n команда: {command}\n ошибка: {error_in_output.group(1)}")
            #        return False
            #    else:
            #        return True
            if mode == "get":
                output = ssh.send_command(command, read_timeout=5)
                return output
    except NetmikoAuthenticationException:
        print(f"Неправильные логин/пароль для устройства {device['host']}>" )
    except NetmikoTimeoutException:
        print(f"Таймаут подключения к устройству {device['host']}")
    except ReadTimeout:
        print(f"Таймаут чтения с устройства {device['host']}")
    except Exception as some_except:
        print(f"Неизвестное исключение при работе с устройством {device['host']} : {str(some_except)}")
    return False

def patch_interfaces(device: dict[str, str]) -> bool:
    command = "show ip int bri"
    raw_data = device_connect(device, command, mode = "get")
    parsed_data = structured_data_converter(
        raw_data=raw_data,
        command=command,
        platform=device["device_type"],
        use_textfsm=True,
    )
    intf_with_ip = [intf for intf in parsed_data if intf["ipaddr"] != "unassigned"]
    config = ""
    for intf in intf_with_ip:
        config += template.render(intf) + "\n"
    config = config.strip().split("\n")
    config_result = device_connect(device, config, mode = "post")
    return True if config_result else False

if __name__ == "__main__":
    print(patch_interfaces(device))
    config = "router posf 1"
    print(device_connect(device, config, mode = "post"))