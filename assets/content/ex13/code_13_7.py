from ipaddress import *

ip1 = ip_address('123.20.103.136')
ip2 = ip_address('123.20.103.151')
for mask in range(0, 33):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)
    if net1 != net2 \
        and ip1 not in [net1[0], net1[-1]] \
        and ip2 not in [net2[0], net2[-1]]:
        print(mask)
        # 28
print(int('11110000', 2))
# 240