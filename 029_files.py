from pathlib import Path


#Task 1
def read_file_value_lines(file):
    f = open(file, "r")
    for line in f.readlines():
        if not line.lstrip().startswith("!"):
            print(line, end="")
    f.close()


#Task 2
rt01_config = """
    !
    interface Vlan1
    ip address 192.168.1.1 255.255.255.0
    no shutdown
    !
    line vty 0 4
    password cisco
    !
    """.strip()

rt02_config = """
    !
    router bgp 64512
    bgp router-id 192.168.1.1
    bgp log-neighbor-changes
    !
    address-family ipv4
    redistribute connected route-map LAN
    exit-address-family
    !
    address-family vpnv4 unicast
    neighbor 1.2.3.4 activate
    exit-address-family
    !
    """.strip()

configs = {
    "rt01": rt01_config,
    "rt02": rt02_config,
}

def save_configs(config: dict[str, str], folder: Path = Path("configs")) -> None:
    if Path(folder).is_absolute():
        Path(folder).parent.mkdir(parents=True, exist_ok=True)
        filepath = Path(folder)
    else:
        filepath = Path(Path.cwd(), folder)
        filepath.mkdir(parents=True, exist_ok=True)
    for hostname, configuration in config.items():
        filename = Path(filepath, f"{hostname}.txt")
        with open(filename, "w") as f:
            f.write(configuration)
    



if __name__ == "__main__":
    read_file_value_lines("029.config.txt")
    save_configs(configs)