import os
import time
from signal import signal, SIGINT
from sys import exit
import sys
import glob


def del_files():
    try:
        files = glob.glob('./files/*.txt')
        for file in files:
            print('+' * 20)
            print(f"File removed : {file.strip('[]')}")
            print('+' * 20)
            os.remove(file)

        text = input("Press Enter to go back !!!")

        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError:
        print("=" * 100)
        print('Error code : ' + OSError)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
        


def create():
    try: 
        if not os.path.exists('files'):
            os.makedirs('files')
    except:
        print("=" * 100)
        print('Error code : ' + OSError)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")

def handler(signal_received, frame):
    # Handle any cleanup here
    print("-" * 100)
    print("*" * 100)
    print('\tCTRL-C detected. Exiting gracefully')
    print("*" * 100)
    print("-" * 100)
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
        cmd_to_file = f'sudo apt-get install {package} >> ./files/install_info.txt'
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("Done")
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")

    except OSError as identifier:
        print("=" * 100)
        print('Error code : ' + identifier)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def search():
    signal(SIGINT, handler)
    print("Enter package name!")
    pkg = str(input(">> "))
    print('=' * 100)
    print(f"Searching package {pkg}")
    print('=' * 100)

    try:
        cmd_to_screen = f'sudo apt-get search {pkg}'
        cmd_to_file = f'sudo apt-get search {pkg} >> ./files/search.txt'
        os.system(cmd_to_screen)
        os.system(cmd_to_file)
        print("=" * 100)
        print("Done")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError as err:
        print("=" * 100)
        print("Erorr : " + err)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def show():
    signal(SIGINT, handler)
    print("Enter package name!")
    pkg = str(input(">> "))
    print('=' * 100)
    print(f"Showing package {pkg} informations")
    print('=' * 100)

    try:
        cmd_to_screen = f'sudo apt-get show {pkg}'
        cmd_to_file = f'sudo apt-get show {pkg} >> files/show_info.txt'
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("=" * 100)
        print("Done")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError as err:
        print("=" * 100)
        print("Erorr : " + err)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def list_pkg():
    signal(SIGINT, handler)
    print("Listing all installed packages...")
    os.system('clear')
    try:
        cmd_to_screen = f'sudo apt list --installed'
        cmd_to_file = f'sudo apt list --installed >> ./files/all_packages.txt'
        os.system(cmd_to_screen)
        print("Wrinting to file... ")
        os.system(cmd_to_file)
        print("=" * 100)
        print("Done")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError as err:
        print("=" * 100)
        print("Erorr : " + err)
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def read():
    signal(SIGINT, handler)
    print("1. Installed Packages file (all_packages.txt)")
    print("2. Install log Recommended after installing a package (install_info.txt)")
    print("3. Informations about package before (show_info.txt)")
    print("4. Read update.txt ")
    print("5. Read upgrade.txt ")
    print("6. Read satisfy.txt ")
    print("7. Read remove.txt ")
    print("8. Read autoremove.txt ")
    print("9. Remove all files ")
    print("99. Back ")
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
        os.system('clear')
        os.system('cat files/update.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 5:
        os.system('clear')
        os.system('cat files/upgrade.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 6:
        os.system('clear')
        os.system('cat files/satisfy.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 7:
        os.system('clear')
        os.system('cat files/removed.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 8:
        os.system('clear')
        os.system('cat files/autoremove.txt')
        print("\n")
        text = input("Type Enter to exit")  # or raw_input in python2
        if text == "":
            read()
    elif choice == 9:
        # or raw_input in python2
        text = input("Type \"yes\" to delete or \" no \" to not delete !")
        if text == "yes":
            del_files()
        elif text == "no":
            read()
        main()
    elif choice == 99:
        main()
    else:
        print("Numers 1,2,3,4,5,6,7,8,9 accept, Try again")
        read()


def update():
    signal(SIGINT, handler)
    print("-" * 50)
    print("*" * 50)
    print("\tUpdating Repositories and creating file update.txt to see results")
    print("*" * 50)
    print("-" * 50)
    try:
        os.system("sudo apt-get update >> ./files/update.txt")
        os.system("sudo apt-get update")
        print("=" * 100)
        print("\tDone")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError:
        print("-" * 50)
        print("*" * 50)
        print(OSError)
        print("*" * 50)
        print("-" * 50)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def upgrade():
    signal(SIGINT, handler)
    print("-" * 50)
    print("*" * 50)
    print("\tUprading Packages and creating file upgrade.txt to see results")
    print("*" * 50)
    print("-" * 50)
    try:
        os.system("sudo apt-get update >> ./files/upgrade.txt")
        os.system("sudo apt-get update")
        print("=" * 100)
        print("\tDone")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except OSError:
        print("-" * 50)
        print("*" * 50)
        print(OSError)
        print("*" * 50)
        print("-" * 50)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def satisfy():
    signal(SIGINT, handler)
    package = str(input("Enter package name: "))
    print("-" * 50)
    print("*" * 50)
    print(
        f"\tSatisfying {package} and creating file satisfy.txt to see results")
    print("*" * 50)
    print("-" * 50)
    try:
        os.system(f"sudo apt-get satisfy {package} >> ./files/statisfy.txt")
        os.system(f"sudo apt-get satisfy {package}")
        print("=" * 100)
        print("\tDone")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except SystemError:
        print("-" * 50)
        print("*" * 50)
        print(SystemError)
        print("*" * 50)
        print("-" * 50)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def remove():
    signal(SIGINT, handler)
    package = str(input("Enter package name: "))
    print("-" * 50)
    print("*" * 50)
    print(f"\tRemoving {package} and creating file removed.txt to see results")
    print("*" * 50)
    print("-" * 50)
    try:
        os.system(f"sudo apt-get remove {package} >> ./files/removed.txt")
        os.system(f"sudo apt-get remove {package}")
        print("=" * 100)
        print("\tDone")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except SystemError:
        print("-" * 50)
        print("*" * 50)
        print(SystemError)
        print("*" * 50)
        print("-" * 50)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def autoremove():
    signal(SIGINT, handler)
    print("-" * 50)
    print("*" * 50)
    print("\tRemoving packages that are not needed and creating file autoremove.txt to see results")
    print("*" * 50)
    print("-" * 50)
    try:
        os.system("sudo apt-get autoremove >> ./files/autoremove.txt")
        os.system("sudo apt-get autoremove")
        print("=" * 100)
        print("\tDone")
        print("=" * 100)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")
    except SystemError:
        print("-" * 50)
        print("*" * 50)
        print(SystemError)
        print("*" * 50)
        print("-" * 50)
        text = input("Press Enter to go back !!!")
        if text == "":
            main()
        else:
            print("Only ENTER is accepted")


def main():
    create()
    signal(SIGINT, handler)
    os.system('cat banner/banner.txt')
    print("-" * 50)
    print("*" * 50)
    print("Hit CTRL + C to exit\n")
    print("What do you want to do?\n")
    print("1. Search for package to see if exists ")
    print("2. Install package ")
    print("3. Show package informations ")
    print("*" * 50)
    print("*" * 50)
    print("4. View all packages ")
    print("5. Read file saved! ")
    print("6. Update Repositories ")
    print("7. Upgrade Packages ")
    print("*" * 50)
    print("*" * 50)
    print("8. Satisfy dependency ")
    print("9. Remove package ")
    print("10. Autoremove packages ")
    print("*" * 50)
    print("-" * 50)
    print("Select your choice !!!\n")

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
    elif user_response == 6:
        update()
    elif user_response == 7:
        upgrade()
    elif user_response == 8:
        satisfy()
    elif user_response == 9:
        remove()
    elif user_response == 10:
        autoremove()
    else:
        print("Don\'t know that command!")
        main()


main()
