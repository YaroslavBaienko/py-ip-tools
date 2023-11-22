import ipaddress

ipv4 = ipaddress.ip_address('10.0.1.1')
subnet1 = ipaddress.ip_network('80.0.1.0/28')
netmask = subnet1.with_netmask
subsub = list(subnet1.subnets(prefixlen_diff=2))
print(subsub)