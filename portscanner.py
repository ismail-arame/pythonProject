import socket
import threading
import time
import sys
import concurrent.futures
import re

if len(sys.argv) < 2:
    print("Usage: python port2.py ip_addr_arg")
    sys.exit(1)

ip = sys.argv[1]

ip_address_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
def is_valid_ip_address(ip):
    if re.match(ip_address_pattern, ip):
        return True
    else:
      print("this ip address is not valid try again.")
      return False

isIpValid = is_valid_ip_address(ip)
 
if isIpValid:
	print(f"[+] Scanning the ip address {ip}")
else:
	print("next time input a correct ip address format")
	sys.exit(1)
	
def scan_port(port):
    try:
        # host = "localhost"
        # ip = socket.gethostbyname(host)
        status = False
  
        # create instance of socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
        # connecting the host ip address and port
        s.connect((ip, port))
        try:
            banner = s.recv(1024).decode()
            if(banner == ""):
              print("port {} is open".format(port))
            else:
              print("port {} is open with banner {}".format(port, banner))
  
        except:
            print("port {} is open ".format(port))
  
    except:
        pass
  
  
def start_scanning():
    start_time = time.time()
    for i in range(0, 100000):
        thread = threading.Thread(target=scan_port, args=[i])
        thread.start()
        end_time = time.time()
    print("To scan all ports it took {} seconds".format(end_time-start_time))

start_scanning()
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     for i in range(0, 100000):
#         executor.submit(scan_port, i)

# for i in range(0, 100000):
#     thread = threading.Thread(target=scan_port, args=[i])
#     thread.start()