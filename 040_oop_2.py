from __future__ import annotations


class IPAddress:
    # ip in format - "address/prefix_len"
    def __init__(self, ip: str) -> None:
        self.address = ip.split("/")[0]
        self.prefix_len = ip.split("/")[1]
        self.ip = ip
    
    def __str__(self) -> str :
        return str(self.ip)
    
    def __repr__(self) -> str :
        return str(f"IPAddress(ip='{self.ip}')")
    
    def __eq__(self, other : IPAddress) -> bool :
        if self.ip == other:
            return True
        else:
            return False


if __name__ == "__main__":
    ip_for_test = [
        "192.168.1.1/24",
    ]
    for raw_ip in ip_for_test:
        ip = IPAddress(raw_ip)
        assert ip.address == raw_ip.split("/")[0], f"неверный адрес для {raw_ip=}"
        assert ip.prefix_len == raw_ip.split("/")[1], f"неверная длина маски для {raw_ip=}"
        assert ip.ip == raw_ip, f"неверный ip адрес для {raw_ip=}"
        assert str(ip) == raw_ip, f"неверная работа метода __str__ для {raw_ip=}"
        ip_repr: IPAddress = eval(repr(ip))
        assert ip_repr.address == ip.address, f"неправильная работа метода __repr__ для {raw_ip=}"
        assert ip_repr.prefix_len == ip.prefix_len, f"неправильная работа метода __repr__ для {raw_ip=}"
        assert ip_repr == ip, f"неправильная работа метода __eq__ для {raw_ip=}"
        ip_ne = IPAddress("0.0.0.0/0")
        assert ip_ne != ip, f"неправильная работа метода __eq__ для {raw_ip=}"