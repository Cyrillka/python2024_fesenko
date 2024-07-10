import re

output = """
spanning-tree mode rapid-pvst
spanning-tree logging
spanning-tree extend system-id
spanning-tree pathcost method long
!
lldp run
!
ntp source-interface Loopback0
!
interface Loopback0
 description -= rid =-
 ip address 192.168.1.1 255.255.255.255
!
interface FastEthernet0/1
 switchport access vlan 10
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
 ip address 4.3.2.1 255.255.255.0
 ip access-group acl_tmp_in in
 ip access-group acl_mgmt_out out
!
interface GigabitEthernet0/4
 description mgmt4.core - FastEthernet0/32
 ip address 1.2.3.4 255.255.255.0
 ip access-group acl_mgmt_in in
 ip access-group acl_mgmt_out out
!
line vty 0 4
 password cisco
!
""".strip()

regex = r"""
    (?<=\n)
    interface\s+(?P<name>\S+)
    (?:
        ip\s+address\s+(?P<ip>\S+)\s+(?P<mask>\S+)
        |ip\s+access-group\s+(?P<acl_in>\S+)\s+in\n
        |ip\s+access-group\s+(?P<acl_out>\S+)\s+out\n
        |.
    )*?\n
    (?!\s)
    """

for interface in re.finditer(regex, output, flags=re.DOTALL | re.VERBOSE,):
    if interface.group("acl_in") != "acl_mgmt_in" and interface.group("ip"):
        print(f"{interface.group('name')}: некорректный ACL - {interface.group('acl_in')} вместо acl_mgmt_in")
    if interface.group("acl_out") != "acl_mgmt_out" and interface.group("ip"):
        print(f"{interface.group('name')}: некорректный ACL - {interface.group('acl_out')} вместо acl_mgmt_out")

#match_int = re.findall(regex, output, flags=re.DOTALL | re.VERBOSE,)
#l3_intf_list = [intf for intf in match_int if intf[1]]
#print(l3_intf_list)
