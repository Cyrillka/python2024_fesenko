from scrapli import Scrapli
from scrapli.driver import NetworkDriver
from scrapli.exceptions import (ScrapliAuthenticationFailed,
                                ScrapliConnectionError, ScrapliTimeout)

device = {
    "platform": "cisco_iosxe",
    "host": "192.168.100.111",
    "auth_username": "admin",
    "auth_password": "passw0rd",
    "auth_secondary": "enpass",
    "auth_strict_key": False,
    "transport": "telnet",
}


def get_output(device: dict[str, str], command: str) -> str:
    def on_open(conn: NetworkDriver) -> None:
        prompt = conn.get_prompt()
        if prompt.endswith(">"):
            conn.default_desired_privilege_level = "exec"
        conn.send_command(command="terminal length 0")
        conn.send_command(command="terminal width 512")

    try:
        with Scrapli(**device, on_open=on_open) as ssh:
            result = ssh.send_command(command)
    except ScrapliAuthenticationFailed:
        print(f"Неправильные логин/пароль для устройства {device.get('host')}")
        return ""
    except (ScrapliTimeout, OSError, ScrapliConnectionError):
        print(f"Таймаут подключения к устройству {device.get('host')}")
        return ""
    except Exception as exc:
        print(f"Неизвестная ошибка при работе с устройством {device.get('host')}: {exc.__class__.__name__}: {exc}")
        return ""
    if result.failed:
        print(f"Ошибка в сборе команды:\n{result.channel_input}\n{result.result}")
        return ""
    else:
        return result.result


if __name__ == "__main__":
    command = "show run"
    print(get_output(device, command))