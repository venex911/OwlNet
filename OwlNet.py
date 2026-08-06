# © 2026 Venex. All rights reserved.
# All rights to the software, source code, documentation, and associated files are owned by Venex.
# Terms of Use: Use of these tools is authorized strictly for security assessments and educational purposes.
# Any misuse, especially for illegal activities, is strictly prohibited.
# The author assumes no liability for damages resulting from the use of these tools.
# Distribution: Unauthorized reproduction, modification, or redistribution of this software without explicit written permission from Venex is prohibited. 


import os
import sys
import subprocess
import time
from colorama import init, Fore, Style

os.system(' title OwlNetV1 - Main Menu ')

init(autoreset=True)

#
LOGO = r"""

                                                 ________         .__    _______          __   
                                                 \_____  \__  _  _|  |   \      \   _____/  |_ 
                                                  /   |   \ \/ \/ /  |   /   |   \_/ __ \   __\
                                                 /    |    \     /|  |__/    |    \  ___/|  |  
                                                 \_______  /\/\_/ |____/\____|__  /\___  >__|  
                                                         \/                     \/     \/              
"""

def print_menu():
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}{LOGO}{Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                           ╔═════                                                    ═════╗{Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                           ║{Fore.RESET}                                                              {Fore.YELLOW}{Style.BRIGHT}║{Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                            {Fore.RESET}                {Fore.GREEN}[1]{Fore.RESET} Discord Webhook Spammer {Fore.YELLOW}{Style.BRIGHT}                              {Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                            {Fore.RESET}                {Fore.GREEN}[2]{Fore.RESET} DoS Tool     {Fore.YELLOW}{Style.BRIGHT}      {Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                            {Fore.RESET}                {Fore.GREEN}[3]{Fore.RESET} Discord Nuker     {Fore.YELLOW}{Style.BRIGHT}      {Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                            {Fore.RESET}                {Fore.GREEN}[4]{Fore.RESET} Exit                  {Fore.YELLOW}{Style.BRIGHT}                                {Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                           ║{Fore.RESET}                                                              {Fore.YELLOW}{Style.BRIGHT}║{Fore.RESET}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                           ╚═════                                                    ═════╝{Fore.RESET}")
    print(f"{Fore.BLUE}{Style.BRIGHT}                                                               Select an option: {Fore.RESET}", end='')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    print(f"{Fore.YELLOW}Loading menu...{Fore.RESET}", end='', flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end='', flush=True)
    print("\n")

def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if not os.path.exists(script_path):
        print(f"\n{Fore.RED}Error: '{script_name}' not found in current directory.{Fore.RESET}")
        print(f"{Fore.YELLOW}Please ensure your tool scripts are in the same folder as this menu.{Fore.RESET}")
        input("\nPress Enter to return to menu...")
        return

    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n{Fore.RED}Tool '{script_name}' exited with error code {e.returncode}.{Fore.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Tool was interrupted by user.{Fore.RESET}")
    except Exception as e:
        print(f"\n{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
    finally:
        input("\nPress Enter to return to the main menu...")

def main_menu():
    loading_animation()
    while True:
        print_menu()
        choice = input().strip()

        if choice == '1':
            run_script('tools/OwlSpammer.py')
        elif choice == '2':
            clear_screen()
            run_script('tools/OwlDoS.py')
        elif choice == '3':
            run_script('tools/OwlNuke/main.py')
        elif choice == '4':
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}Invalid option.{Fore.RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Program terminated by user.{Fore.RESET}")
        sys.exit(0)