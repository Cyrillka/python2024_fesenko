# Task 1
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
    print(f"нотация {mac}: {mac_notation}")


mac_detect("50465d6e8c20")

# Task 2


def ipclass_detect(ip):
    octet1 = int(ip.split(".")[0])
    if octet1 < 127:
        ip_class = "A"
    elif 128 <= octet1 <= 191:
        ip_class = "B"
    elif 192 <= octet1 <= 223:
        ip_class = "C"
    elif 224 <= octet1 <= 239:
        ip_class = "D"
    elif 240 <= octet1 <= 254:
        ip_class = "E"
    print(f"класс ip {ip}: {ip_class}")


ipclass_detect("224.3.2.1")

# Task 3
access = """
interface {if_name}
   switchport mode access
   switchport access vlan {vlan}
!
""".strip()

trunk = """
interface {if_name}
   switchport mode trunk
   switchport trunk allowed vlan {vlan}
!
""".strip()

intf1 = {
    "if_name": "gi0/1",
    "vlan": 102,
    "mode": "access",
}

intf2 = {
    "if_name": "gi0/2",
    "vlan": 103,
    "mode": "trunk",
}

intf1_config = (
    intf1.get("mode") is "access"
    and access.format(**intf1)
    or intf1.get("mode") is "trunk"
    and trunk.format(**intf1)
)
if intf2.get("mode") == "access":
    intf2_config = access.format(**intf2)
elif intf2.get("mode") == "trunk":
    intf2_config = trunk.format(**intf2)
print(intf1_config)
print(intf2_config)
