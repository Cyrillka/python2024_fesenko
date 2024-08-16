from netmiko import (ConnectHandler, NetmikoAuthenticationException,
                     NetmikoTimeoutException, ReadTimeout)

device = {
    "device_type": "cisco_xe",
    "host": "192.168.100.101",
    "username": "admin",
    "password": "passw0rd",
    "secret": "enpass",
}

def clear_logging(device: dict[str, str]) -> bool:
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command("clear logging", expect_string=rf"(?:\[confirm\])", read_timeout=5)
            output += ssh.send_command("\n")
        return True
    except NetmikoAuthenticationException:
        print(f"Неправильные логин/пароль для устройства {device['host']}>" )
    except NetmikoTimeoutException:
        print(f"Таймаут подключения к устройству {device['host']}")
    except ReadTimeout:
        return False
    except Exception as some_except:
        print(f"Неизвестное исключение при работе с устройством {device['host']} : {str(some_except)}")
if __name__ == "__main__":
    print(clear_logging(device))