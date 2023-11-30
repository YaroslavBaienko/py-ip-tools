from tools.subnet_splitter import calculate_subnets, calculate_subnets_by_hosts

if __name__ == '__main__':
    while True:
        print("1. subnet_splitters\n2. another tools")
        choose_tool = input("Choose tool: ")
        if choose_tool == "1":
            network = input("Input network such as '192.168.1.0/24: ")
            num_subnets = int(input("Input number of subnets: "))
            calculated = calculate_subnets(network=network, num_subnets=num_subnets)
            for subnets_info in calculated:
                print(subnets_info)
        if choose_tool == "2":
            network = input("Input network such as '192.168.1.0/24: ")
            hosts_per_subnet = int(input("Input number of hosts per subnet: "))
            calculated = calculate_subnets_by_hosts(network=network, hosts_per_subnet=hosts_per_subnet)
            print(calculated)
        else:
            continue
