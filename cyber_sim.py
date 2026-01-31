import pyfiglet
import time
from rich import print

#BANNER

banner = pyfiglet.figlet_format("DR.CYBER")
print(banner)

#WARNINGS

print("[bold red][+] v 2.0.1")
print("[bold yellow][+] warning: All items is simulater!!")
print("")
print("[bold red]_"*54)

#ITEMS & SERViCES

print("[bold green]1 DOS WIFI & ACCOUNT\n2 GOOGLE\n3 FACEBOOK\n4 INSTGRAM")
print("[bold red]_"*54)
services = input("INTER YOUR SERVICES: ")
if services == "1":
	targets = input("INTER YOUR TARGET & ACCOUNT: ")
	while True:
		time.sleep(0.1)
		print(f"[bold green]attacking.... {targets} 👻")
elif services == "1" or "2" or "3" or "4":
	services2 = input("INTER YOUR NAME ACCOUNT: ")
	
#PASSWORDS LISTS

anonymous = {
    "GOOGLE": "AYMEN999",
    "FACEBOOK": "AHMEDBVB000",
    "INSTGRAM": "insss11108",
}
passwordlist = ["admin", "root", "qewtry12334", "password1123", "qazwsxedc", "plmoknijb", "aleaas1199", "edcrfvtgb123", "AYMEN999", "AHMEDBVB000", "insss11108"]

#TRY PASSWORDS

for password in passwordlist:
	print(f"[bold red]CRACKING PASSWORD .... [   {password}   ]")
	time.sleep(0.5)
	
#SCANING PASS

if services == "GOOGLE":
	print("PASSWORD FOUND! [  AYMEN999  ]")
elif services == "2":
	print("[bold green]PASSWORD FOUND! [  AHMEDBVB000  ]")
elif services == "3":
	print("[bold green]PASSWORD FOUND! [ insss11108  ]")
elif services == "4":
	print("[bold green]PASSWORD FOUND! [  insss11108  ]")
else:
	print("[bold black]PASSWORD NOT FOUND!")
	exit()