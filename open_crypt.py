import pyAesCrypt
import os, sys
from getpass import getpass
import time
from colorama import Fore, Style
import datetime
from art import *

print(f"{Fore.GREEN}{skull}{Style.RESET_ALL}")
print(f"{Fore.GREEN}{banner}{Style.RESET_ALL}")
print(f"{Fore.GREEN}{banner2}{Style.RESET_ALL}")
password = getpass()
min_decrypted = int(
    input("Enter number of minutes needed to work in encrypted directory: ")
)

time_max = 40

if(min_decrypted >= time_max):
    print(f"{Fore.RED}{Style.BRIGHT} {time_max} is the current max decrypted minutes")
    sys.exit('You exceeded maximum decrypt time')

secrets_path = os.path.join(os.getcwd(), "secrets")
dir_list = os.listdir(secrets_path)


for secret_file in dir_list:
    pyAesCrypt.decryptFile(
        os.path.join(secrets_path, secret_file),
        os.path.join(secrets_path, secret_file.replace(".aes", ".txt")),
        password)

# remove all .aes files in secrets
for item in dir_list:
    if item.endswith(".aes"):
        os.remove(os.path.join(secrets_path, item))

# min_decrypted = 1
symbols = ["-","|","/","-","\\" ,"|","/"]
len_symbols = len(symbols)
for sec in range(0, min_decrypted * 60):
    time.sleep(1)
    next_symbol = symbols[sec%len_symbols]
    seconds_remaining = min_decrypted * 60 - sec
    time_remaining = datetime.timedelta(seconds=seconds_remaining)
    print(f"{Fore.GREEN}{Style.BRIGHT}--- make relavant changes, you have -- {time_remaining} until re-encryption --- {next_symbol} {Style.RESET_ALL}",
          end="\r",
          flush=True)

dir_list_2 = os.listdir(secrets_path)

for secret_file in dir_list_2:
    pyAesCrypt.encryptFile(
        os.path.join(secrets_path, secret_file),
        os.path.join(secrets_path, secret_file.replace(".txt", ".aes")),
        password)

# remove all .txt files in secrets
for item in dir_list_2:
    if item.endswith(".txt"):
        os.remove(os.path.join(secrets_path, item))

print("\n")
print(f"{Fore.GREEN}{Style.BRIGHT}All files are now encrypted again.{Style.RESET_ALL}")

