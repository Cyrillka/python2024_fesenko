from netmiko import (ConnectHandler, NetmikoAuthenticationException,
                     NetmikoTimeoutException)

devices = [
{
    "device_type": "cisco_xe", #timeout
    "host": "192.168.100.151",
    "username": "admin",
    "password": "passw0r",
},
{
    "device_type": "cisco_xe", #invalid creds
    "host": "192.168.100.101",
    "username": "admin",
    "password": "pass",
},
{
    "device_type": "cisco_xe", #invalid param - misstyped
    "host": "192.168.100.101",
    "username": "admin",
    "password": "passw0rd",
    "trnsport": "telnet"
},
]


def get_output(device: dict[str, str], command: str) -> str:
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
        return output
    except NetmikoAuthenticationException:
        print(f"Неправильные логин/пароль для устройства {device['host']}>" )
    except NetmikoTimeoutException:
        print(f"Таймаут подключения к устройству {device['host']}")
    except Exception as some_except:
        print(f"Неизвестное исключение при работе с устройством {device['host']} : {str(some_except)}")
if __name__ == "__main__":
    for device in devices:
        print(get_output(device, "show clock"))