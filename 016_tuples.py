# Task1
intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]
intf_list.remove("gi0/22")
intf_list.remove("gi0/23")
intf_list.append("gi0/2")
intf_list.sort()
# print(intf_list)

# Task2
from collections import deque

intf_list_2 = deque(["gi0/1"])
intf_list_2.appendleft("gi0/0")
intf_list_2.append("gi0/2")
print(list(intf_list_2))

# Task3
mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
diag1 = []
for num, array_ in enumerate(mtx):
    diag1.append(array_[num])
print(diag1)

diag2 = []
for num, array_ in enumerate(mtx):
    diag2.append(array_[::-1][num])
print(diag2)

# Task 4
vlans = []
output = "switchport trunk allowed vlan 2,101,104"
output_list = output.split()
vlan_list_str = output_list[-1].split(",")
for i in vlan_list_str:
    vlans.append(int(i))
print(vlans)

# Task 5
from collections import namedtuple

output = """
Interface             IP-Address      OK?    Method Status      Protocol
GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
TenGigabitEthernet2/1 unassigned      YES    unset  up          up
Te36/45               unassigned      YES    unset  down        down
""".strip()
_, *interfaces = output.split("\n")
InterfaceStatus = namedtuple(
    "InterfaceStatus", ["name", "ip", "ok", "method", "status", "protocol"]
)

intf_brief = [InterfaceStatus(*x.split()) for x in interfaces]
print(len(intf_brief))
