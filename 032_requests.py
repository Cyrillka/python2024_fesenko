import os
from functools import lru_cache
from typing import Any
from urllib.parse import urlencode

import requests
import urllib3

urllib3.disable_warnings()

@lru_cache
def get_netbox_item(path: str, query: str = "") -> list[dict[str, Any]]:
    """получение данных из netbox, в ENV необходимы переменные NB_URL и NB_TOKEN
    например:
      - export NB_URL=http://10.211.55.7:8000
      - export NB_TOKEN=d6f4e314a5b5fefd164995169f28ae32d987704f

    Args:
        path (str): ресурс вида '/api/dcim/devices/'
        query (str, optional): параметры запроса

    Returns:
        list[dict[str, Any]]: список словарей с результатами
    """
    result = []
    url = os.environ.get("NB_URL", "")
    token = os.environ.get("NB_TOKEN", "")
    if not all([url, token]):
        raise ValueError("Insufficient data")

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(
        url=url + path,
        params=query,
        headers=headers,
        verify=False
    )
    if response.status_code != 200:
        raise ValueError("Connection error")
    print(response.json()) 
    if "results" not in response.json():
        return [response.json()]
    else:
        result = response.json().get("results", [])
        url_next = response.json().get("next")
        while url_next is not None:
                response = requests.get(
                    url=url_next,
                    params=query,
                    headers=headers,
                    verify=False
                )
                result = result + response.json().get("results", [])
                url_next = response.json().get("next")
    return result


q = [
    ("name__isw", "rt"),
    ("name__isw", "sw"),
    ("limit", 2),
    ("brief", True),
]

nb_devices = get_netbox_item(
    path="/api/dcim/devices/",
    query=urlencode(q),
)

print(nb_devices)
print(len(nb_devices))