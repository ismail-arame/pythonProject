import random
import os
import time
import threading
import sys
import concurrent.futures

def clearScr():
    os.system('cls' if os.name == 'nt' else 'clear')

class color:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    BLUE = '\33[34m'

color_random=[color.PURPLE,color.GREEN,color.RED,color.BLUE]
random.shuffle(color_random)
darkarmylogo = color_random[0] + '''
     _       __     __  ______            __    
    | |     / /__  / /_/_  __/___  ____  / /____
    | | /| / / _ \/ __ \/ / / __ \/ __ \/ / ___/
    | |/ |/ /  __/ /_/ / / / /_/ / /_/ / (__  ) 
    |__/|__/\___/_.___/_/  \____/\____/_/____/ 
      
                        A Collection Of Web and Enumeration Testing Tools 
                                                                                                                                                                                                                   
'''
def menu():
    print (darkarmylogo + """\033[1m
   [!] Coded By Ismail, Yassin, Driss
\033[0m
   {1}--Port Scanner
   {2}--Network Scanner
   {3}--Subdomain Enumeration
   {4}--Directory Enumeration
   {5}--SSH BruteForcing
   {99}-Exit
 """)
    choice = input("Y0urInput >> ")
    # os.system('clear')
    if choice == "1":
        ip = input("ip address >> ")
        os.system(f'python portscanner.py {ip}')
    elif choice == "2":
        interface = input("interface >> ")
        ip_range = input("ip range >> ")
        os.system(f'python networkscanner.py {interface} {ip_range}')
    elif choice == "3":
        wordlist = input("wordlist path >> ")
        url = input("url >> ")
        os.system(f'python subdomainenum_threads.py {wordlist} {url}')
    elif choice == "4":
        wordlist = input("wordlist path >> ")
        url = input("url >> ")
        os.system(f'python direnum_threads.py {wordlist} {url}')
    elif choice == "5":
        target = str(input('Please enter target IP address >> '))
        username = str(input('Please enter username to bruteforce >> '))
        password_file = str(input('Please enter location of the password file >> '))
        os.system(f"python sshbrute.py {target} {username} {password_file}")
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()

menu()