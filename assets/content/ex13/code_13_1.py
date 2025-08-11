from ipaddress import *

net = ip_network('73.148.145.65/255.224.0.0', 0)
print(net[-2])
# 73.159.255.254