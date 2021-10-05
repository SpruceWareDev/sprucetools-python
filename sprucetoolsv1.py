import os
import requests
import json
# utils
def print_logo():
    print(" ___ ___ ___ _ _ ___ ___ ")
    print("|_ -| . |  _| | |  _| -_|")
    print("|___|  _|_| |___|___|___|")
    print("    |_|                  ")

def print_options():
    print("1) File stuff")
    print("2) Server stuff")
    print("3) Chat thingy (idk if i do)")
    print("4) Fun stuff (might add more soon)")
    print("5) Quit")

#main functions
def file_stuff():
    print_logo()
    print("File Utils")
    print("1) File searcher")
    print("2) Back")
    usrIn = int(input("File Utils>"))
    if usrIn == 1:
        fileName = input("Enter the name of the text file (with .txt) >")
        file = open(fileName, "r")
        print("File opened!")
        searchIn = input("Enter something to search for >")
        found = False
        line_number = 0
        for line in file:
            line_number += 1
            if searchIn in line:
                lineFound = line_number
                found = True
                break
        if found == True:
            print("String found in file opened on line " + str(lineFound))
        else:
            print("String not found in file opened!")
        file.close()
    elif usrIn == 2:
        print("gone back!")

def server_stuff():
    print_logo()
    url = "http://ip-api.com/json/"
    ipIn = input("IP Searcher> Enter an IP to search :")
    resp = requests.get(url=url, params=ipIn)
    data = resp.json()
    for key, value in data.items():
        print(key, ":", value)

def chat():
    print_logo()
    print("Nothing here yet!")

def fun_stuff():
    print_logo()
    print("Fun Stuff")
    print("1) About")
    print("2) Back")
    usrIn = int(input("Fun Stuff>"))
    # about command
    if usrIn == 1:
        print_logo()
        print("Spruce Tools by Spruce#7704")
        print("Made in python bc idk")
        print("Idk why I made this but it exist now ig :troll:")

# main handling
running = True
print("Welcome to spruce tools!")
print_logo()
print_options()

while running:
    optionSelected = int(input(">"))

    if optionSelected == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        file_stuff()
    elif optionSelected == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        server_stuff()
    elif optionSelected == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        chat()
    elif optionSelected == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        fun_stuff()
    elif optionSelected == 5:
        running = False
