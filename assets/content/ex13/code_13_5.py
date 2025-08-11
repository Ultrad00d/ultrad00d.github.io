from ipaddress import *

# узлы сети из условия
ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
# перебираем маску с конца, чтобы первое найденное было максимальным
for mask in range(32, 0, -1):
    # задаем сети по такой маске
    net1 = ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ip_network(f'200.154.184.0/{mask}', 0)
    # если сети равны и ip1 и ip2 не являеются
    # сетевым и широковещательным адресам
    if net1 == net2 \
        and ip1 not in [net1[0], net1[-1]] \
        and ip2 not in [net1[0], net1[-1]]:
        # то выводим маску
        print(mask)
        break