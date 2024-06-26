import csv
import ipaddress

output = """
AP Name     AP IP             Neighbor Name        Neighbor IP      Neighbor Port
---------   ---------------   ------------------   --------------   -------------
SB_RAP1     192.168.102.154   sjc14-41a-sw1        192.168.102.2    GigabitEthernet1/0/13
SB_RAP1     192.168.102.154   SB_MAP1              192.168.102.137  Virtual-Dot11Radio0
SB_MAP1     192.168.102.137   SB_RAP1              192.168.102.154  Virtual-Dot11Radio0
SB_MAP1     192.168.102.137   SB_MAP2              192.168.102.138  Virtual-Dot11Radio0
SB_MAP2     192.168.102.138   SB_MAP1              192.168.102.137  Virtual-Dot11Radio1
SB_MAP2     192.168.102.138   SB_MAP3              192.168.102.139  Virtual-Dot11Radio0
SB_MAP3     192.168.102.139   SB_MAP2              192.168.102.138  Virtual-Dot11Radio1
""".strip()


def create_csv(data: str):
    headers = ["ap_name", "ap_ip"]
    device_dict = {}
    for line in data.split("\n"):
        try: #убираем лишнее
            ipaddress.ip_address(line.split()[1])
            device_dict[line.split()[0]] = line.split()[1]
        except ValueError:
            continue

    if device_dict:  # или как правильнее проверить что он не пустой?
        data_list = [
            {"ap_name": key, "ap_ip": value} for key, value in device_dict.items()
        ]
        with open("ap.csv", "w", newline="") as f:
            writter = csv.DictWriter(f=f, fieldnames=headers)
            writter.writeheader()
            for line in data_list:
                writter.writerow(line)


create_csv(output)
