import requests
import os 
from colorama import Fore, Back, Style
os.system("clear")
print(Fore.GREEN+"""
##############################
#                            #
#       Admin Spider         #
#                            #
##############################""")
print('')
print("Example : google.com")
print('')
UrlInput = input(Fore.RED+"Enter URl To Find a Admin Panal : ")
file = open('wordlist.txt','r').read().splitlines()
file2 = open("wordlist2.txt",'r').read().splitlines()
for admin in file2:
    url2 = f"https://{admin}.{UrlInput}"
    try:
        req2 = requests.get(url2)
        print(Fore.GREEN+"{+} Found : "+url2 )
    except requests.ConnectionError:
        pass
for admin in file :
    url1 = f"https://{UrlInput}/{admin}"
    try:
        req = requests.get(url1)
        if req.status_code == 200:
            print(Fore.GREEN+"{+} Found : "+url1 )
        elif req.status_code == 404:
            print(Fore.RED+"{-} Not Found : "+url1 )
        elif req.status_code == 403:
            print(Fore.RED+"{-} Not Found : "+url1 )
    except requests.ConnectionError:
        pass
