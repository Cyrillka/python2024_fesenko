from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "192.168.100.101",
    "username": "admin",
    "password": "passw0rd",
}


def get_output(device: dict[str, str], command: str) -> str:
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
    return output

if __name__ == "__main__":
    print(get_output(device, "show clock"))