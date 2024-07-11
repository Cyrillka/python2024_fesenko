import re
from collections import namedtuple
from typing import Generator

output = """
rt# show ip interface brief
Interface             IP-Address      OK?    Method Status                   Protocol
GigabitEthernet0/1    192.168.100.1   YES    unset  up                          up
GigabitEthernet0/2    192.168.190.235 YES    unset  up                          up
GigabitEthernet0/3    unassigned      YES    unset  up                          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up                          up
TenGigabitEthernet2/1 unassigned      YES    unset  up                          up
TenGigabitEthernet2/2 10.255.1.3      YES    unset  up                          up
TenGigabitEthernet2/3 unassigned      YES    unset  up                          up
TenGigabitEthernet2/4 unassigned      YES    unset  up                          down
GigabitEthernet3/1    unassigned      YES    unset  administratively down       down
GigabitEthernet3/2    unassigned      YES    unset  down                        down
GigabitEthernet3/3    unassigned      YES    unset  administratively down       down
GigabitEthernet3/4    unassigned      YES    unset  down                        down
Loopback1             unassigned      YES    unset  up                          up
Loopback2             10.255.255.100  YES    unset  administratively down       down
""".strip()

#regex = r"^(?P<name>\S+)\s+(?P<ip>\S+)\s+\w+\s+\w+\s+(?P<status>(\w+\s\w+|\w+))\s+(?P<protocol>\w+)$" #непонятно почему не заработал, на regex101 все ок
regex = r'(\S+)\s+(\S+)\s+\w+\s+\w+\s+(\w+\s\w+|\w+) +(up|down)'
fields = ["name", "ip", "status", "protocol"]
IPInterface = namedtuple("IPInterface", fields)
def parse_show_ip_int_br(output: str) -> Generator[IPInterface, None, None]:
    match_interface = re.finditer(regex, output, flags=re.DOTALL,)
    for i in match_interface:
        #print(i.groups())
        yield (IPInterface(*i.groups()))

for interface in parse_show_ip_int_br(output):
    print(interface)