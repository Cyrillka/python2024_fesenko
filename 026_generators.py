#Task 1
from typing import Generator

config = """
ip forward-protocol nd
no ip http server
!
interface Vlan1
 ip address 192.168.1.1 255.255.255.0
 no shutdown
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
line vty 0 4
 password cisco
!
""".strip()


def config_generator(config: str) -> Generator[str, None, None]:
    for line in config.split("\n"):
        if not line.strip().startswith("!") and "exit-address-family" not in line:
            yield line

#for line in config_generator(config):
#    print(line)

#Task2
def config_generator(config: str) -> Generator[str, None, None]:
    num_space_prev = 0
    for line in config.split("\n"):
        if not line.strip().startswith("!") and "exit-address-family" not in line:
            num_space = len(line) - len(line.lstrip())
            if num_space >= num_space_prev:
                num_space_prev = num_space
                yield line.strip()
            else:
               multip = num_space_prev - num_space
               num_space_prev -= multip
               exit = "exit\n"*multip
               yield exit+line.strip()
            

for line in config_generator(config):
    print(line)