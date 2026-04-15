import time
import sys
import os
from colorama import Fore, Style, init

# Initialize Colorama for Termux colors
init(autoreset=True)

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def typing_effect(text, color=Fore.WHITE, speed=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def bd_loader():
    sys.stdout.write(Fore.GREEN + "  [SYSTEM] ")
    loading_chars = ["|", "/", "-", "\\"]
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {Fore.GREEN}[PROCESSING] {Fore.RED}{loading_chars[i % 4]} ")
        sys.stdout.flush()
    print(Fore.GREEN + "SUCCESS! 🇧🇩\n")

def logo():
    clear()
    # Bangladesh Flag Inspired Logo
    print(Fore.GREEN + Style.BRIGHT + r"""
    ╔══════════════════════════════════════════════╗
    ║  ██████████████████████████████████████████  ║
    ║  █████████████████        █████████████████  ║
    ║  ██████████████    {Fore.RED}██████{Fore.GREEN}    ██████████████  ║
    ║  █████████████    {Fore.RED}████████{Fore.GREEN}    █████████████  ║
    ║  ██████████████    {Fore.RED}██████{Fore.GREEN}    ██████████████  ║
    ║  █████████████████        █████████████████  ║
    ║  ██████████████████████████████████████████  ║
    ╚═══════════════ {Fore.WHITE}CODEXBD    {Fore.GREEN}═══════════════╝""".format(Fore=Fore))
    print(f"\n        {Fore.RED}★ {Fore.GREEN}BANGLADESH SPECIAL EDITION {Fore.RED}★")
    print(f"        {Fore.WHITE}------------------------------\n")

def main():
    while True:
        logo()
        print(f"  {Fore.CYAN}┌──({Fore.WHITE}MAIN MENU{Fore.CYAN})")
        print(f"  {Fore.CYAN}│")
        print(f"  {Fore.CYAN}├──[01] {Fore.GREEN}TEXT TO MORSE {Fore.WHITE}(ENCRYPT)")
        print(f"  {Fore.CYAN}├──[02] {Fore.GREEN}MORSE TO TEXT {Fore.WHITE}(DECRYPT)")
        print(f"  {Fore.CYAN}└──[00] {Fore.RED}EXIT PROGRAM")
        
        choice = input(f"\n  {Fore.GREEN}CODEXBD-BD {Fore.RED}❯ {Fore.WHITE}")

        if choice == '1' or choice == '01':
            msg = input(f"\n  {Fore.YELLOW}ENTER MESSAGE: {Fore.WHITE}")
            bd_loader()
            cipher = ''
            for char in msg.upper():
                cipher += MORSE_CODE_DICT.get(char, char) + ' '
            
            print(f"  {Fore.GREEN}RESULT:")
            typing_effect(f"  {cipher}", Fore.YELLOW, 0.05)
            input(f"\n  {Fore.RED}[ Press Enter to Back ]")

        elif choice == '2' or choice == '02':
            msg = input(f"\n  {Fore.YELLOW}ENTER MORSE: {Fore.WHITE}")
            bd_loader()
            words = msg.split(' / ')
            decoded = ""
            try:
                for word in words:
                    chars = word.split()
                    for char in chars:
                        decoded += REVERSE_DICT.get(char, '?')
                    decoded += " "
                
                print(f"  {Fore.GREEN}RESULT:")
                typing_effect(f"  {decoded.strip()}", Fore.YELLOW, 0.05)
            except:
                print(f"  {Fore.RED}[!] ERROR: INVALID DATA")
            input(f"\n  {Fore.RED}[ Press Enter to Back ]")

        elif choice == '0' or choice == '00':
            typing_effect("\n  Stopping CODEXBD System... 🇧🇩", Fore.RED)
            time.sleep(1)
            break
        else:
            print(f"  {Fore.RED}[!] WRONG INPUT!")
            time.sleep(1)

if __name__ == "__main__":
    main()