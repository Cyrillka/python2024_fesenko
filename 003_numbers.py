ip1 = "192.168.43.54 / 255.255.254.0"
ip2 = "192.168.43.54 / 255.255.255.240"

def dec_to_bin(dec_val:str):
    bin_val = "".join([f"{int(octet):08b}" for octet in dec_val.split(".")])
    return bin_val
def bin_to_dec(bin_val:str):
    dec_val = f"{int(bin_val[0:8], 2)}.{int(bin_val[8:16], 2)}.{int(bin_val[16:24], 2)}.{int(bin_val[24:], 2)}"
    return dec_val
def ip_calc(ipmask:str):
    ip_info = {}
    ip, mask = ipmask.split(" / ")
    ip_bin = dec_to_bin(ip)
    mask_bin = dec_to_bin(mask)
    mask_length = int(mask_bin.count("1"))
    #Адрес сети
    net_ip_bin = ip_bin[0: (mask_length)] + (32-mask_length)*"0"
    ip_info["net_ip"] = bin_to_dec(net_ip_bin)
    #Wildcard
    wildcard_bin = mask_length*"0" + (32-mask_length)*"1"
    ip_info["wildcard"] = bin_to_dec(wildcard_bin)
    #Min Host
    min_host_ip_bin = net_ip_bin = ip_bin[0: (mask_length)] + (32-mask_length - 1)*"0" + "1"
    ip_info["min_host_ip"] = bin_to_dec(min_host_ip_bin)
    #Max Host
    max_host_ip_bin = ip_bin[0: (mask_length)] + (32-mask_length - 1)*"1" + "0"
    ip_info["max_host_ip"] = bin_to_dec(max_host_ip_bin)
    #Broadcast
    broadcast_ip_bin = ip_bin[0: (mask_length)] + (32-mask_length)*"1"
    ip_info["broadcast_ip"] = bin_to_dec(broadcast_ip_bin)

    return ip_info


print(ip_calc(ip1))
print(ip_calc(ip2))