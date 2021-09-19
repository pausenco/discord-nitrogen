import requests
from time import sleep
import time
import sys, os
from subprocess import run
import subprocess
from colorama import Fore
import random
import string




if "SUDO_UID" not in os.environ.keys():
    print(Fore.RED + "[+] RUN AS ROOT")
    sys.exit(1)



banner = f"""
{Fore.LIGHTMAGENTA_EX}·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      ▄▄▄▄·       ▄▄▄▄▄
{Fore.LIGHTGREEN_EX}██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀█▪▪     •██  
{Fore.LIGHTMAGENTA_EX}▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
{Fore.LIGHTGREEN_EX}██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ██▄▪▐█▐█▌.▐▌ ▐█▌·
{Fore.LIGHTMAGENTA_EX}▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
"""
print(banner)
print("type options to show the options")


commands = ["exit","boost", "classic", "options", "banner", "whoami"]

cmd = input(f"{Fore.LIGHTGREEN_EX}root{Fore.LIGHTMAGENTA_EX}@{Fore.LIGHTGREEN_EX}user {Fore.WHITE}─{Fore.RED}➤ ")

options = f"""
╭─root@user ~ [options]  
╰─➤ OPTIONS
exit     ~ exits the program
boost    ~ generate boost nitro
classic  ~ generate classic nitro
options  ~ print options 
whoami   ~ who am i?
"""
while True:
 

    if cmd not in commands:
        print("invalid command")
        subprocess.run(["python3", "main.py"])


    elif cmd.startswith("exit"):
        print("ending")
        time.sleep(1)
        sys.exit(1)

    elif cmd.startswith("whoami"):
        print("Hello i am alex")
        subprocess.run(["python3", "main.py"])

    elif cmd.startswith("options"):
        print(options)
        subprocess.run(["python3", "main.py"])

    elif cmd.startswith("boost"):
                
        err = 0
    code = random.choice(string.ascii_letters + string.digits)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(24))
    for _ in range(24):
        

        url = 'https://discord.com/api/v8/entitlements/gift-codes/' + code + '?with_application=false&with_subscription_plan=true'
    rs = requests.session()
    r = rs.get(url)

    if 'subscription_plan' in r.text:
      print(Fore.GREEN + ('Valid | https://discord.gift/', code))
      break

    elif 'Access denied' in r.text:
      print(Fore.RED + 'Access denied')
      err +=1
      if err > 5:
        break
      else:
        continue

    else:
      print(Fore.RED + ('Invalid | https://discord.gift/' + code))
      

    if cmd.startswith("classic"):
                    
        err = 0
    code = random.choice(string.ascii_letters + string.digits)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    for _ in range(16):
        

        url = 'https://discord.com/api/v8/entitlements/gift-codes/' + code + '?with_application=false&with_subscription_plan=true'
    rs = requests.session()
    r = rs.get(url)

    if 'subscription_plan' in r.text:
      print(Fore.GREEN + ('Valid | https://discord.gift/', code))
      break

    elif 'Access denied' in r.text:
      print(Fore.RED + 'Access denied')
      err +=1
      if err > 5:
        break
      else:
        continue

    else:
      print(Fore.RED + ('Invalid | https://discord.gift/' + code))
      
