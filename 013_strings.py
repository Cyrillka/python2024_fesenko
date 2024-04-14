# TASK 1.1
config = """
#
bridge-domain 555
 vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
 vxlan vni 10555
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target 64512:10555 export-extcommunity
  vpn-target 64512:10555 import-extcommunity
 arp broadcast-suppress enable
#"""
# TASK 2.1
if True:
    config = """
#
bridge-domain 555
 vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
 vxlan vni 10555
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target 64512:10555 export-extcommunity
  vpn-target 64512:10555 import-extcommunity
 arp broadcast-suppress enable
#"""
# TASK 2
bd_id = 555

bd_id_str1 = str(bd_id)
bd_id_str2 = f"{bd_id}"
bd_id_str3 = "% s" % bd_id

# TASK 3.1
output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"
output_string = output.decode("utf-8")
# TASK 3.2
output_string_1 = output_string.strip("\r")
# TASK 3.3
output_string_2 = output_string_1.lstrip()
# print(output_string_1.lstrip())

# TASK 4.1
bd_id = "84"
intf_start = "10GE1/0/1"
intf_end = "10GE1/0/48"
rid = "192.168.43.34"
bgp_as = "64512"

template = f"""
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni 1{bd_id.zfill(4)}
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target {bgp_as}:1{bd_id.zfill(4)} export-extcommunity
  vpn-target {bgp_as}:1{bd_id.zfill(4)} import-extcommunity
 arp broadcast-suppress enable
"""
# TASK 4.2
print(f"{int(str(42)):b}")
print(f"{int(str(32)):b}")
print(f"{int(str(255)):b}")

# TASK 4.3
print(f"{int(str(42)):08b}")
print(f"{int(str(32)):08b}")
print(f"{int(str(255)):08b}")

# TASK 4.4
ip = "10.23.43.234"
result = "".join([f"{int(octet):08b}" for octet in ip.split(".")])
print(result)

# TASK 4.5
ip = "77.88.55.242"
octets = ip.split(".")
result = f"{octets[3]}.{octets[2]}.{octets[1]}.{octets[0]}.in-addr.arpa"
print(result)

# TASK 4.6
ip = "192.168.43.54 / 255.255.254.0"


def dec_to_bin(dec_val: str):
    bin_val = "".join([f"{int(octet):08b}" for octet in dec_val.split(".")])
    return bin_val


def bin_to_dec(bin_val: str):
    dec_val = ".".join([f"{int(bin_val[i:i+8], 2)}" for i in range(0, 25, 8)])
    return dec_val


def ip_calc(ipmask: str):
    ip, mask = list(map(str.strip, ipmask.split("/")))
    ip_bin = dec_to_bin(ip)
    mask_bin = dec_to_bin(mask)
    mask_length = int(mask_bin.count("1"))
    # Адрес сети
    net_ip_bin = ip_bin[0:(mask_length)] + (32 - mask_length) * "0"
    network = bin_to_dec(net_ip_bin)
    # Wildcard
    wildcard_bin = mask_length * "0" + (32 - mask_length) * "1"
    wildcard = bin_to_dec(wildcard_bin)
    # Min Host
    min_host_ip_bin = ip_bin[0:(mask_length)] + (32 - mask_length - 1) * "0" + "1"
    min_host_ip = bin_to_dec(min_host_ip_bin)
    # Max Host
    max_host_ip_bin = ip_bin[0:(mask_length)] + (32 - mask_length - 1) * "1" + "0"
    max_host_ip = bin_to_dec(max_host_ip_bin)
    # Broadcast
    broadcast_ip_bin = ip_bin[0:(mask_length)] + (32 - mask_length) * "1"
    broadcast = bin_to_dec(broadcast_ip_bin)
    print(network)
    print(wildcard)
    print(broadcast)
    print(min_host_ip)
    print(max_host_ip)


# TASK 4.7
output = """
Local Interface         Exptime(s) Neighbor Interface            Neighbor Device
-------------------------------------------------------------------------------------
100GE1/0/1                    107  100GE1/0/1                    spine1.pod1.stg
10GE1/0/1                     105  10GE1/0/1                     test-server.stg
""".strip()
output = output.replace("-", "")
print("\n".join(filter(None, output.split("\n"))))

# TASK 4.8
if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Ten4/3"

if_name1 = if_name1.replace("Eth", "Ethernet")
if_name2 = if_name2.replace("GE", "GigabitEthernet")
if_name3 = if_name3.replace("Ten", "TenGigabitEthernet")

print(if_name1)
print(if_name2)
print(if_name3)
