class IPAddress:
    # ip in format - "address/prefix_len"
    def __init__(self, ip: str) -> None:
        self.address = ip.split("/")[0]
        self.prefix_len = ip.split("/")[1]
        self.ip = ip

if __name__ == "__main__":
    ip_for_test = [
        "192.168.1.1/24",
    ]
    for raw_ip in ip_for_test:
        ip = IPAddress(raw_ip)
        assert ip.address == raw_ip.split("/")[0], f"неверный адрес для {raw_ip=}"
        assert ip.prefix_len == raw_ip.split("/")[1], f"неверная длина маски для {raw_ip=}"
        assert ip.ip == raw_ip, f"неверный ip адрес для {raw_ip=}"