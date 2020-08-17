import os
import time
from .main import create_test
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\t    SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def install():
    signal(SIGINT, handler)
    print("Enter package name!")
    package = str(input(">> "))
    print('=' * 100)
    print(f"Installing package {package}")
    print('=' * 100)
    try:
        cmd_to_screen = f'sudo apt-get install {package}' 
        cmd_to_file = f'sudo apt-get install {package} >> install_info.txt' 
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("Done")
        time.sleep(2)
        os.system('clear')
        main()
    except OSError as identifier:
        print('Error code : ' + identifier)
        time.sleep(2)
        main()

def search():
    signal(SIGINT, handler)
    print("Enter package name!")
    pkg = str(input(">> "))
    print('=' * 100)
    print(f"Searching package {pkg}")
    print('=' * 100)

    try:
        cmd_to_screen = f'sudo apt-get search {pkg}'
        os.system(cmd_to_screen)
        print("Done")
        time.sleep(2)
        os.system('clear')
    except OSError as err:
        print("Erorr : " + err)
        time.sleep(2)
        main()

def show():
    signal(SIGINT, handler)
    print("Enter package name!")
    pkg = str(input(">> "))
    print('=' * 100)
    print(f"Showing package {pkg} informations")
    print('=' * 100)

    try:
        cmd_to_screen = f'sudo apt-get show {pkg}' 
        cmd_to_file = f'sudo apt-get show {pkg} >> show_info.txt' 
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("Done")
        time.sleep(2)
        os.system('clear')
        main()
    except OSError as err:
        print("Erorr : " + err)
        time.sleep(2)
        main()

def list_pkg():
    signal(SIGINT, handler)
    print("Listing all installed packages...")
    os.system('clear')
    try:
        cmd_to_screen = f'sudo apt list --installed' 
        cmd_to_file = f'sudo apt list --installed >> all_packages_list.txt' 
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("Done")
        time.sleep(2)
        os.system('clear')
        main()
    except OSError as err:
        print("Erorr : " + err)
        time.sleep(2)
        main()

def read():
    signal(SIGINT, handler)
    print("1. Installed Packages file (all_packages.txt)")
    print("2. Install log Recommended after installing a package (install_info.txt)")
    print("3. Informations about package before (show_info.txt)")
    print("4. Back ") 
    print("Select your choice! ")

    choice = int(input(">> "))

    if choice == 1:
        os.system('clear')
        os.system('cat files/all_packages.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 2:
        os.system('clear')
        os.system('cat files/install_info.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 3:
        os.system('clear')
        os.system('cat files/show_info.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 4:
        main()
    else:
        print("Numers 1,2,4 accept, Try again")
        read()
def main():
    signal(SIGINT, handler)
    os.system('cat ../banner/banner.txt')
    create_test.create()

    print("Enter your package name!\n")

    print("What do you want to do?\n")
    print("1. Search for package to see if exists ")
    print("2. Install package ")
    print("3. Show package informations ")
    print("4. View all packages ")
    print("5. Read file saved! ")
    print("\n\a")
    signal(SIGINT, handler)
    user_response = int(input(">> "))

    if user_response == 1:
        search()
    elif user_response == 2:
        install()
    elif user_response == 3:
        show()
    elif user_response == 4:
        list_pkg()
    elif user_response == 5:
        read()
    else:
        print("Don\'t know that command!")
        main()
main()
