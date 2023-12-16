import os
import sys

def menu():
    menus = {
        "1": git_install,
        "2": git_setup,
        "3": git_check,
        "4": full_install,
        "0": exit_program,  
        "5": uninstall,
    }

    option = input(
        "\n\nGit install for Windows 10:\n"
        "1. Install Git\n"   # Start from option 1
        "2. Change basic Git configuration\n"
        "3. Check Git configuration\n"
        "4. Run full Git install\n"
        "5. Uninstall Git\n"
        "0. Exit installer\n"  
        "+----+\n"
        "Select variant:"
    )

    while option not in menus.keys():
        print("Invalid option. Please enter a valid option.")
        option = input(
            "\n\nGit install for Windows 10:\n"
            "1. Install Git\n"
            "2. Change basic Git configuration\n"
            "3. Check Git configuration\n"
            "4. Run full Git install\n"
            "5. Uninstall Git\n"
            "0. Exit installer\n"
            "+----+\n"
            "Select variant:"
        )

    menus.get(option)()

def git_install():
    print("\033[93m{}".format("Downloading required packages"))
    os.system("choco install git")
    print("\033[93m{}".format("Git installed!"))
    menu()

def git_setup():
    print("\033[93m{}".format("Creating Git user"))
    username = input("\033[96m{}".format("Git username: "))
    email = input("\033[96m{}".format("Git email: "))
    set_username_cmd = f"git config --global user.name '{username}'"
    set_email_cmd = f"git config --global user.email '{email}'"
    print("\033[93m{}".format("Applying changes"))
    os.system(set_username_cmd)
    os.system(set_email_cmd)
    print("\033[92m{}".format("Git configuration is OK."))
    menu()

def git_check():
    print("\033[93m{}".format("Checking Git version"))
    os.system("git --version")
    print("\033[92m{}".format("\n\nChecking Git configuration"))
    os.system("git config --list")
    menu()

def full_install():
    git_install()
    git_setup()
    git_check()
    menu()

def exit_program():
    sys.exit()

def uninstall():
    print("\033[93m{}".format("Uninstalling Git"))
    os.system("choco uninstall git")
    print("\033[93m{}".format("Git uninstalled!"))
    menu()

if __name__ == "__main__":
    menu()
