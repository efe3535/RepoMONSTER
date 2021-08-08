from os import getcwd, system
from json import loads
from random import choice

try:
    from requests import get
    from colorama import Fore
    import git
    from tkinter import *
    from tkinter.messagebox import showinfo, showerror
except ModuleNotFoundError:
    system("python3 setup.py install --user")



root = Tk()
root.geometry("300x150")
root.eval('tk::PlaceWindow . center')
repos = []
username = StringVar()
foldername = StringVar()

def main():
    if(len(username.get()) >= 1 and len(foldername.get()) >= 1):
        github_api_req = get(f"https://api.github.com/users/{username.get()}/repos")
        
        if(github_api_req.status_code == 200):
            github_api_res = loads(github_api_req.content)
            for repo in github_api_res:
                repos.append(repo["html_url"])

        repo_choice = choice(repos)
        
        try:
            showinfo(f"Cloning {Fore.GREEN}{repo_choice}{Fore.RESET} to {Fore.MAGENTA}{getcwd() + foldername.get()}{Fore.RESET}")
            git.Repo.clone_from(repo_choice, getcwd() + "/" + foldername.get())
        
        except git.exc.GitCommandError:
            showerror(f"{Fore.RED}Directory already exists, change the name please.{Fore.RESET}")

username_label = Label(text="Enter username to fetch repos at")
username_label.pack()

username_entry = Entry(textvariable=username)
username_entry.pack()

foldername_label = Label(text="\nEnter foldername to save repos at")
foldername_label.pack()

foldername_entry = Entry(textvariable=foldername)
foldername_entry.pack()

submit = Button(text="Submit", command=main)
submit.pack()

root.mainloop()