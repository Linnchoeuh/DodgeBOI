"""
module_installer.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Header file for game function/class
Copyright (c) 2022
"""

import os

YES_CHAR: str = "Y".upper()
NO_STR: str = "N".upper()
INSTALL_SUCCESS: str = ""

def prompt_module_installer(module_name: str,
                            update_pip: bool) -> None:
    if (update_pip):
        if (os.system("python -m pip install --upgrade pip") != 0):
            print("pip seems missing.")
    decision: str = ""
    while (decision.upper() != NO_STR and decision.upper() != YES_CHAR):
        decision = input(f"Do you want to install: {module_name}? ({YES_CHAR}/{NO_STR}): ")
        if (decision.upper() == YES_CHAR):
            print(f"Installing {module_name}...")
            if (os.system(f"python -m pip install {module_name}") == 0):
                print("Installation success.")
            else:
                print("Installation failed.")
        elif (decision.upper() == NO_STR):
            print("Module installation canceled.")


if __name__ == "__main__":
    print("Installing all required module for this program...")
    prompt_module_installer("pygame", True)
    print("Installation ended.")
    exit()