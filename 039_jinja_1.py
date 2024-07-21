from jinja2 import Environment, FileSystemLoader, Template

interfaces = {
    "GigabitEthernet0/0/0": {
        "mtu": 1600,
        "description": "-= pe2.klg =-",
        "ip": "192.168.1.1",
        "mask": "255.255.255.252",
        "type": "internal",
        "bfd": True,
        "shutdown": False,
    },
    "GigabitEthernet0/0/1": {
        "shutdown": True,
        "ip": "192.168.2.1"
    },
    "GigabitEthernet0/0/2": {
        "description": "-= pe1.klg =-",
        "ip": "192.168.2.1",
        "mask": "255.255.255.252",
        "type": "external",
        "bfd": True,
        "shutdown": False,
        "mtu": 1500,
    },
}

env = Environment(loader=FileSystemLoader("./039_templates"))

def create_intf_cfg(intf_data:dict):
    template = env.get_template("task_1.j2")
    config = template.render(interfaces=intf_data)
    print(config)
create_intf_cfg(interfaces)
