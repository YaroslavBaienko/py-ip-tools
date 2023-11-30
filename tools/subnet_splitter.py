import ipaddress
import math


def calculate_subnets(network: str, num_subnets: int):
    try:
        # Validate the input data
        network = ipaddress.ip_network(network)
        num_subnets = int(num_subnets)

        # Calculate the necessary increase in prefix length
        prefix_increase = math.ceil(math.log(num_subnets, 2))
        new_prefix = network.prefixlen + prefix_increase

        # Check if the new prefix length exceeds the maximum allowed for IPv4/IPv6
        if (network.version == 4 and new_prefix > 32) or (network.version == 6 and new_prefix > 128):
            raise ValueError("Too many subnets requested")

        # Generate the subnets
        subnets = list(network.subnets(new_prefix=new_prefix))

    except ValueError as e:
        return {"error": str(e)}

    subnet_hosts = {}  # Dictionary to store lists of hosts by subnet
    for num, subnet in enumerate(subnets, start=1):
        # Create a list of hosts for each subnet
        hosts = list(map(str, subnet.hosts()))
        subnet_hosts[f"Subnet {num}"] = hosts

    # Output lists of hosts
    subnet_num = 0
    for subnet, hosts in subnet_hosts.items():
        subnet_num += 1
        result = {"subnet_num": subnet_num, "number of hosts": len(hosts), "hosts": hosts}
        yield result


def calculate_subnets_by_hosts(network: str, hosts_per_subnet: int):
    try:
        # Validate the input data
        network = ipaddress.ip_network(network)

        # Calculate the necessary decrease in host bits to accommodate the desired number of hosts
        # +2 for network and broadcast addresses in each subnet
        required_host_bits = math.ceil(math.log(hosts_per_subnet + 2, 2))
        new_prefix = 32 - required_host_bits

        # Check if the new prefix length is valid
        if new_prefix < network.prefixlen:
            raise ValueError("Too many hosts requested for the given network size")

        # Generate the subnets
        subnets = list(network.subnets(new_prefix=new_prefix))

    except ValueError as e:
        return {"error": str(e)}

    results = []
    for num, subnet in enumerate(subnets, start=1):
        # Create a list of hosts for each subnet
        hosts = list(map(str, subnet.hosts()))

        result = {
            "subnet_num": num,
            "subnet": str(subnet),
            "number of hosts": len(hosts),
            "hosts": hosts
        }
        results.append(result)

    return {"total_subnets": len(subnets), "subnets": results}
