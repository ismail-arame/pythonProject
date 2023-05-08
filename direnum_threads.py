import sys
import requests
import threading

if len(sys.argv) < 3:
    print("Usage: python direnum_threads.py wordlist url")
    sys.exit(1)

wordlist = open(f"{sys.argv[1]}").read()
extensions = ".html .php .txt .js .css .cgi .pdf .exe .zip .png"
extensions = extensions.split()
extensions.append("")
dirs = wordlist.splitlines()
c = 0

print("[+] Enumerating Directories...")
def check_dir(dire, exe):
    global c
    url = f"http://{sys.argv[2]}/{dire}{exe}"
    r = requests.get(url)
    try:
        if r.status_code == 404:
            pass
        else:
            print(f"[+] valid directories : {sys.argv[2]}/{dire}{exe} [+]")
            c += 1
    except Exception as e:
        print(f"[+] Exception : {e} [+]")

threads = []
for dire in dirs:
    for exe in extensions:
        t = threading.Thread(target=check_dir, args=(dire, exe))
        t.start()
        threads.append(t)

for t in threads:
    t.join()

if c == 0:
    print("no directories found !")
