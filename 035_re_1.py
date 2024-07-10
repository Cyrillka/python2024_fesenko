# TASK 1
import re
from collections import namedtuple

sw1_output = """
sw1# show switch
                                            H/W   Current
 Switch#  Role   Mac Address     Priority Version  State
 ----------------------------------------------------------
 *1       Master 0018.ba60.de00     15       1     Ready
  2       Member 0018.ba60.ce00     14       1     Ready
  3       Member 0016.9d0c.7500     1        2     Version Mismatch
""".strip()

sw2_output = """
sw2> show switch
                                               Current
Switch#  Role      Mac Address     Priority     State
--------------------------------------------------------
 1       Slave     0016.4748.dc80     5         Ready
*2       Master    0016.9d59.db00     1         Ready
""".strip()


def _norm_data(somedata: list):
    norm_list = []
    for data in somedata:
        if data.isdigit():
            norm_list.append(int(data))
        elif not data:
            norm_list.append(0)
        else:
            norm_list.append(data)
    return norm_list


regex = r"(?P<id>\d)\s+(?P<role>\w+)\s+(?P<mac>(?:[a-f0-9]{4}\.?){3})\s+(?P<priority>\d+)\s+(?P<revision>\d+)*\s+(?P<state>\w+.?\w+)"
fields = ("id", "role", "mac", "priority", "revision", "state")
StackMember = namedtuple("StackMember", fields)


def parse_show_switch(output: str) -> list:
    match_data = re.findall(regex, output)
    parsed_data = [StackMember(*_norm_data(list(data))) for data in match_data]
    return parsed_data


sw1_parse = parse_show_switch(sw1_output)
sw2_parse = parse_show_switch(sw2_output)
print(sw1_parse, sw1_parse)


