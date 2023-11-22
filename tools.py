import ipaddress
<<<<<<< HEAD

ipv4 = ipaddress.ip_address('10.0.1.1')
subnet1 = ipaddress.ip_network('80.0.1.0/28')
netmask = subnet1.with_netmask
subsub = list(subnet1.subnets(prefixlen_diff=2))
print(subsub)
=======
import math


def subnet_network(network, num_subnets):
    # Вычисляем необходимое увеличение длины префикса
    prefix_increase = math.ceil(math.log(num_subnets, 2))
    new_prefix = network.prefixlen + prefix_increase

    if new_prefix > 32:  # Для IPv4
        raise ValueError("Слишком много подсетей запрошено")

    return list(network.subnets(new_prefix=new_prefix))


# Пример использования
network = ipaddress.ip_network('192.168.88.0/24')
num_subnets = int(input("Enter the number of subnets: "))
subnets = subnet_network(network, num_subnets)

subnet_hosts = {}  # Словарь для хранения списков хостов по подсетям

for num, subnet in enumerate(subnets, start=1):
    print(f"Subnet {num}: {subnet}")
    hosts = list(map(str, subnet.hosts()))  # Создаем список хостов для подсети
    subnet_hosts[f"Subnet {num}"] = hosts

# Выводим списки хостов
for subnet, hosts in subnet_hosts.items():
    print(f"{subnet} hosts:")
    print(f"Всего хостов {len(hosts)}: {hosts}")
    print()  # Добавляем пустую строку для разделения подсетей

