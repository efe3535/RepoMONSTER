from colorama.ansi import Fore
import requests
from sys import argv
from colorama import Fore

helptext = f"""
{open("repomonster.txt","r").read()}
--user=<User to select a random repo>
"""

user_specified = False

if(len(argv) == 1):
    print(helptext)

else:
    for arg in argv:
        if("--user=" in arg or "-u=" in arg or "--u=" in arg):
            user = arg.split("=")[1]
            user_specified = True
    if(not user_specified):
        print("User has to be specified. Otherwise I do not have any ability to predict it, normally...")
        exit(127)
    