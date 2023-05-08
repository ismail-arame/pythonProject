
import requests 
import sys 
import threading

if len(sys.argv) < 3:
    print("Usage: python subdomainenum_threads.py wordlist url")
    sys.exit(1)

sub_list = open(f"{sys.argv[1]}").read() 
subdoms = sub_list.splitlines()
url=sys.argv[2]

print('[+] Enumerating Subdomins...')
def subenum(sub,url):
    sub_domains = f"http://{sub}.{url}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    except Exception as e:
        pass
    else:
        print("Valid domain: ",sub_domains)

threads=[]

for sub in subdoms:
    t=threading.Thread(target=subenum , args=(sub,url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()