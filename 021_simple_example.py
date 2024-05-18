# Task1
def vlan_range(vlans: str) -> str:
    seq_list = []
    result_list = []
    vlan_list = list(map(int, vlans.split(",")))
    for num in range(len(vlan_list)):  # проверка что числа последовательные
        if vlan_list[num - 1] + 1 == vlan_list[num]:
            seq_list.append( # если да, добавляем в промежуточный список
                vlan_list[num - 1]
            )  
        else:  # Последовательность прервалась, но надо добавить последний элемент, и диапзон заменить на "-"
            if seq_list:
                seq_list.append(vlan_list[num - 1])
                result_list.append(f"{seq_list[0]}-{seq_list[-1]}")
            seq_list = []  # Обнулим промежуточный список.
            result_list.append(str(vlan_list[num]))  # Добавим не послед-й элемент
        if (num + 1 == len(vlan_list) and seq_list):  # чтобы включить в результат, если кончается на последовательность
            seq_list.append(vlan_list[num])  # выглядит как костыль конечно, но другого не придумалось
            result_list.append(f"{seq_list[0]}-{seq_list[-1]}")
    return ",".join(result_list)


a = vlan_range("10,20,30,31,32,33,34,35,39,40,41")
print(a)

# Task2
lldp_output = """
GE1/0/1          br1.hq            GE0/0/5             107
GE1/0/2          br2.hq            GE0/0/5             92
GE1/0/3          sw1.hq            GE1/0/47            98
XGE1/0/1         sw2.hq            GE1/0/51            93
GE2/0/2          br2.hq            GE0/0/6             112
GE2/0/3          sw12.hq           GE1/0/48            98
XGE2/0/1         sw2.hq            GE1/0/52            93
""".strip()
description_output = """
GigabitEthernet1/0/1        up      up       br1.hq.net.ru
GigabitEthernet1/0/2        up      up       br2.hq.net.ru
GigabitEthernet1/0/3        up      up       sw1.hq.net.ru
GigabitEthernet2/0/1        up      up       br1.hq.net.ru
GigabitEthernet2/0/2        up      up       br2.hq.net.ru
GigabitEthernet2/0/3        up      up       sw1.hq.net.ru
XGigabitEthernet1/0/1       up      up       sw2.hq.net.ru
XGigabitEthernet2/0/1       up      up       sw2.hq.net.ru
""".strip()


def intf_name_convert(intf_short): #Вспомогательная ф-я
    intf_dict = {"GE": "GigabitEthernet", "XGE": "XGigabitEthernet"}
    intf_name = intf_short.rstrip("0123456789/.")
    intf_name_long = intf_dict.get(intf_name)
    intf_name_full = intf_short.replace(intf_name, intf_name_long)
    return intf_name_full


def compare_lldp_desc(lldp, desc):
    desc_dict = {}
    lldp_dict = {}
    for i in desc.split("\n"): #Вот тут не получилось через dict comprehensions сделать
        intf_name, *_, description = i.split()
        desc_dict[intf_name] = description.rstrip(".net.ru")

    for i in lldp.split("\n"):
        intf_short, neighbor, *_ = i.split()
        intf_name = intf_name_convert(intf_short)
        lldp_dict[intf_name] = neighbor

    for k, v in desc_dict.items(): #перебор словаря описаний
        if k in lldp_dict.keys(): #избегаем искл-я KeyError
            if not v == lldp_dict.get(k):
                print(
                    f"For interface {k} description '{v}' is wrong, should be '{lldp_dict.get(k)}'"
                )

compare_lldp_desc(lldp_output, description_output)