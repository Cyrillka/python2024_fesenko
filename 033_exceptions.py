#Task 1
import os

import pynetbox

url = os.environ.get("NB_URL")
token = os.environ.get("NB_TOKEN")

nb = pynetbox.api(url=url, token=token)

name = "FM6865_leaf_01"
device = nb.dcim.devices.get(name=name)
try:
    device.description = "some new description_NEW"
    device.save()
except AttributeError:
    print(f"устройства с именем {name} не существует")

#Task 2
import os
import sys

sys.tracebacklimit=0
url = os.environ.get("NB_UR")
token = os.environ.get("NB_TOKEN")

if not all([url, token]):
    raise ValueError("отсутсвуют параметры проключения к серверу")
