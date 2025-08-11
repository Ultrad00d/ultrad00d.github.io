from ipaddress import *

counter = 0
# создаем сеть из условия
net = ip_network('203.68.128.0/255.255.192.0', 0)
# проходимся по каждому узлу 
for ip in net:
    # берем его двоичное представление
    ip_bin = f'{ip:b}'
    # если кол-во единиц не кратно 7, то считаем
    if ip_bin.count('1') % 7 != 0: counter += 1
print(counter)