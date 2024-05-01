# Task1

"""
почему то не смог импортировать функцию, из-за того что начинается на число? 
from 019_conditionals import mac_detect
если переименовать то все ок 
from conditionals import mac_detect
"""


mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]


def mac_detect(mac: str):
    if "-" in mac and mac.isupper():
        mac_notation = "IEEE EUI-48"
    elif "-" in mac and mac.islower():
        mac_notation = "IEEE EUI-48 lowercase"
    elif mac.count(":") == 5:
        mac_notation = "UNIX"
    elif mac.count(":") == 3:
        mac_notation = "cisco"
    elif len(mac) == 12 and mac.isalnum():
        mac_notation = "bare"
    else:
        mac_notation = "uknown"
    print(f"нотация {mac}: {mac_notation}")


for mac_addr in mac_list:
    mac_detect(mac_addr)

# Task 2
devices = [
    "rt1.lan.hq.net",
    "p1.mpls.hq.net",
    "p2.mpls.hq.net",
    "sw1.lan.hq.net",
    "dsw1.lan.hq.net",
]
hq_devices = [device for device in devices if "lan.hq.net" in device]
print(hq_devices)

# Task3
SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}
hostnames = ["rt1", "rt2", "sw1", "sw2"]

# Task3.1
devices = {}
for device in hostnames:
    devices[device] = SCRAPLI_TEMPLATE

# Task3.2
devices = {device: SCRAPLI_TEMPLATE for device in devices}


# Task4

line = "switchport trunk allowed vlan 100,200,300-500,600"


def check_vlan(vlan):
    if isinstance(vlan, str):
        vlan = int(vlan)
    non_vlan_len = len(line.rstrip("0123456789-,")) #отрезаем цифры и тире
    vlans = line[non_vlan_len:] #срез конца строки
    vl_list = vlans.split(",") #список vlan
    vlans = []
    for v in vl_list:
        if "-" in v:  #убираем диапазон
            start, end = v.split("-")
            for i in range(int(start), int(end) + 1):
                vlans.append(i) 
        else:
            vlans.append(int(v))
    if vlan in vlans:
        print(f"VLAN {vlan} в списке разрешенных")
    else:
        print(f"VLAN {vlan} отсутствует в списке разрешенных")


check_vlan(400)
check_vlan("800")
