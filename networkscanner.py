from scapy.all import *

#use pretty table module to output IPs


#to be modified . also make sure the network mask is correct

if len(sys.argv) < 2:
    print("Usage: python port2.py ip_addr_arg")
    sys.exit(1)

interface = sys.argv[1]
ip_range = sys.argv[2]

# ip_range="192.168.0.0/24"


def network_scanner(ip_range):
	list_arp=[]
	bm="ff:ff:ff:ff:ff:ff"
	packet=Ether(dst=bm)/ARP(pdst=ip_range)

	qa, nonans=srp(packet, timeout=1,iface=interface,verbose=False)

	for querie, answer in qa:
		list_arp.append(f"[+]     {answer[1].psrc}         {answer[1].hwsrc} [+]")

	return list_arp


def show_list(list_arp):
	print("\t IP\t\t|| \t MAC \t\t \n ------------------------------------------------------")
	for result in list_arp:
		print(result)

list_arp= network_scanner(ip_range)
show_list(list_arp)