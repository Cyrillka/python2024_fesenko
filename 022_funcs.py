# Task 1


def mac_detect(mac: str):
    if "-" in mac and mac.isupper():
        mac_notation = "IEEE EUI-48"
    elif "-" in mac and mac.islower():
        mac_notation = "IEEE EUI-48 lowercase"
    elif mac.count(":") == 5:
        mac_notation = "UNIX"
    elif mac.count(":") == 2:
        mac_notation = "cisco"
    elif len(mac) == 12 and mac.isalnum():
        mac_notation = "bare"
    else:
        mac_notation = "uknown"
    print(f"нотация MAC {mac}: {mac_notation}")
    return mac_notation


mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]
for mac in mac_list:
    mac_detect(mac)

print("##" * 50)


# Task2
def intf_name_convert(intf_short):  # Вспомогательная ф-я
    intf_dict = {
        "Eth": "Ethernet",
        "Fa": "FastEthernet",
        "Gig": "GigabitEthernet",
        "GE": "GigabitEthernet",
        "Ten": "TenGigabitEthernet",
        "TE": "TenGigabitEthernet",
        "XGE": "TenGigabitEthernet",
    }
    intf_name = intf_short.rstrip("0123456789/.")
    intf_name_long = intf_dict.get(intf_name)
    if not intf_name_long:
        return intf_short
    intf_name_full = intf_short.replace(intf_name, intf_name_long)
    return intf_name_full


interfaces = [
    "Eth0/0",
    "Gig0/4/3",
    "GE4/4",
    "Po3",
    "Ten5/4",
    "XGE4/1",
    "Eth-Trunk4",
]
for intf in interfaces:
    print(intf_name_convert(intf))

print("##" * 50)
# Task3
from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        nonlocal start #меняем переменную внешней ф-и
        print(f"{perf_counter() - start:.2f}")
        start = perf_counter()

    return inner


t = timer()
t()

config = """
spanning-tree mode rapid-pvst
spanning-tree logging
spanning-tree extend system-id
spanning-tree pathcost method long
!
lldp run
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/2
 switchport access vlan 11
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/3
 switchport access vlan 51
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/4
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface GigabitEthernet0/1
 description mgmt1.core - FastEthernet0/32
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50-70,80,90
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/2
 description mgmt2.core - FastEthernet0/32
 switchport mode trunk
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/3
  description mgmt3.core - FastEthernet0/32
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30,40,50-70,80,90
  switchport trunk allowed vlan add 150,151
  mls qos trust cos
  ip dhcp snooping trust
!
interface GigabitEthernet0/4
 description mgmt4.core - FastEthernet0/32
 ip address 1.2.3.4 255.255.255.0
!
line vty 0 4
 password cisco
!
"""


def parse_config(config: str):
    result = {}
    sub_config = []
    for line in config.strip().split("\n"):
        if line.startswith(
            "!"
        ):  # если строка ! значит новый блок конфига, сбрасываем саб данные
            sub_config = []
        elif not line[0].isspace():  # Записываем global команду в ключи
            result[line] = sub_config
        elif line[0].isspace():  # заполняем список присвоенный ключу
            sub_config.append(line)
    return result


parsed = parse_config(config)
print(parsed)
