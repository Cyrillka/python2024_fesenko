#Task 1
keys = ["hostname", "ip", "username", "password", "platform", "enable"]
params_dev_1 = ["r1.abcd.net", "192.168.1.1", "cisco", "secret", "cisco_ios", True]
params_dev_2 = ["sw1.abcd.net", "192.168.1.2", "admin", "secret", "huawei_vrp", False]

device1 = dict(zip(keys, params_dev_1))
device2 = dict(zip(keys, params_dev_2))

#Task 2
devices_list = []
devices_list.append(device1)
devices_list.append(device2)

#Task 3
dev_name = {}
for dev in devices_list:
    dev_name[dev.get("hostname")] = dev

#Task 4
from copy import deepcopy

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

params_device_1 = SCRAPLI_TEMPLATE | {"hostname" : "sw1.abcd.net"}
scrpali_device_2 = {
    "hostname" : "sw1.abcd.net",
    "transport" : "telnet",
    "port" : 23
}
params_device_2 = deepcopy(SCRAPLI_TEMPLATE)
params_device_2.update(scrpali_device_2)
