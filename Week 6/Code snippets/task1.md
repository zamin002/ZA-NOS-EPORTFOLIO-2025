```
import ipaddress

def analyse_ip(ip_str):
    # Create an IP interface object
    ip = ipaddress.ip_interface(ip_str)

    print(f"Address: {ip.ip}")
    print(f"Network: {ip.network}")
    print(f"Netmask: {ip.netmask}")
    print(f"Number of Usable Hosts: {ip.network.num_addresses - 2}")  # Excluding network and broadcast
    print(f"Is private: {ip.ip.is_private}")
    print(f"Is global: {ip.ip.is_global}")
    print(f"Broadcast Address: {ip.network.broadcast_address}") #task 1
    print(f"First Usable Host: {list(ip.network.hosts())[0]}")
    print(f"Last Usable Host: {list(ip.network.hosts())[-1]}")    

    # List all hosts in the network (for small networks)
    if ip.network.num_addresses < 256:
        print("\nHosts in network:")
        for host in ip.network.hosts():
            print(host)

print("Analysing 192.168.1.1/24")
analyse_ip('192.168.1.1/24')

print("\nAnalysing 10.0.0.1/16")
analyse_ip('10.0.0.1/16')

print("\nAnalysing private home IP") #private IP
analyse_ip("192.168.56.1")
```