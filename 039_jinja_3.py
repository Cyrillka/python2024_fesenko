import ipaddress

from jinja2 import Environment, FileSystemLoader


def mask_to_preflen(mask):
  return(sum([ bin(int(bits)).count("1") for bits in mask.split(".") ]))
def get_net_ip(ip, mask):
    prefix_len = mask_to_preflen(mask)
    return ipaddress.ip_interface(f"{ip}/{prefix_len}").network.network_address
def get_wildcard(mask, ip):
    prefix_len = mask_to_preflen(mask)
    return ipaddress.ip_interface(f"{ip}/{prefix_len}").network.hostmask

interfaces = {
    "GigabitEthernet0/0/0": {
        "mtu": 1600,
        "ip": "192.168.0.1",
        "mask": "255.255.255.252",
        "type": "internal",
        "bfd": True,
        "area": 0,
    },
    "GigabitEthernet0/0/1": {
        "mtu": 1600,
        "ip": "192.168.1.1",
        "mask": "255.255.255.252",
        "type": "external",
        "bfd": True,
        "shutdown": False,
    },
}

env = Environment(loader=FileSystemLoader("./039_templates"))
env.filters["ip_network"] = get_net_ip
env.filters["ip_wildcard"] = get_wildcard

def create_intf_cfg(intf_data:dict):
    template = env.get_template("task_3_main.j2")
    config = template.render(interfaces=intf_data)
    print(config)
create_intf_cfg(interfaces)
