from os import getcwd, system
from json import loads
from random import choice
from sys import argv

try:
    from requests import get
    from colorama import Fore
    import git

except ModuleNotFoundError:
    system("python3 setup.py install --user")

helptext = f"""
{Fore.GREEN + open("repomonster.txt","r").read() + Fore.RESET}
{Fore.YELLOW} --user=<User to select a random repo> {Fore.RESET}
{Fore.LIGHTBLUE_EX} --dirname=<Repo to save> {Fore.RESET}
"""

repos = []

user_specified = False
dirname_specified = False

if(len(argv) == 1):
    print(helptext)

else:
    for arg in argv:
        if("--user=" in arg or "-u=" in arg or "--u=" in arg):
            user = arg.split("=")[1]
            user_specified = True
        
        if("--dirname=" in arg or "-dn=" in arg or "--dn=" in arg):
            dirname = arg.split("=")[1]
            if(len(dirname)>0):
                dirname_specified = True

    if(not user_specified):
        print(Fore.RED + "User has to be specified. Otherwise I do not have any ability to predict it, normally..." + Fore.RESET)
        exit(127)
    
    if(not dirname_specified):
        print(Fore.RED + "You have to specify the dirname to tell me where to save this repo!" + Fore.RESET)
        exit(127)

    elif(user_specified and dirname_specified):
        github_api_req = get(f"https://api.github.com/users/{user}/repos")
        if(github_api_req.status_code == 200):
            github_api_res = loads(github_api_req.content)
            for repo in github_api_res:
                repos.append(repo["html_url"])

        repo_choice = choice(repos)
        
        try:
            print(f"Cloning {Fore.GREEN}{repo_choice}{Fore.RESET} to {Fore.MAGENTA}{getcwd() + dirname}{Fore.RESET}")
            git.Repo.clone_from(repo_choice, getcwd() + "/" + dirname)
        
        except git.exc.GitCommandError:
            print(f"{Fore.RED}Directory already exists, change the name please.{Fore.RESET}")