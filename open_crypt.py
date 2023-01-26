import pyAesCrypt
import os, sys, shutil
from getpass import getpass
import time
from colorama import Fore, Style
import datetime
from art import *

print(f"{Fore.GREEN}{line}")
print(f"{skull}")
print(f"{banner}")
print(f"{banner2}")
password = getpass(prompt="      Password: ")
print(f"{line}{Style.RESET_ALL}")

min_decrypted = int(
    input("\n  Enter number of minutes needed to work in encrypted directory: ")
)

time_max = 40
sec_per_min = 10

if(min_decrypted >= time_max):
    print(f"{Fore.RED}{Style.BRIGHT} {time_max} is the current max decrypted minutes")
    sys.exit(' You exceeded maximum decrypt time')

secret_path = os.path.join(os.getcwd(), "secrets")
sanctum_path = os.path.join(os.getcwd(), "sanctum")

# making the secret and sanctum dirs, if they do not exist.
if not os.path.exists(secret_path):
    os.mkdir(secret_path)
if not os.path.exists(sanctum_path):
    os.mkdir(sanctum_path)

# secrets_path = os.path.join(os.getcwd(), "secrets")
dir_list = os.listdir(secret_path)

# De-crypting files.
for secret_file in dir_list:
    try:
        pyAesCrypt.decryptFile(
            os.path.join(secret_path, secret_file),
            os.path.join(secret_path, secret_file.replace(".aes", "")),
            password)
    except ValueError as e:
        sys.exit(f"{Fore.RED}     Wrong password  -- or file(s) corrupted.{Style.RESET_ALL}")

# remove all .aes files in secrets
for item in dir_list:
    if item.endswith(".aes"):
        os.remove(os.path.join(secret_path, item))

# min_decrypted = 1
symbols = ["-","|","/","-","\\" ,"|","/"]
len_symbols = len(symbols)
for sec in range(0, min_decrypted * sec_per_min):
    time.sleep(1)
    next_symbol = symbols[sec%len_symbols]
    seconds_remaining = min_decrypted * sec_per_min - sec
    time_remaining = datetime.timedelta(seconds=seconds_remaining)
    print(f"{Fore.GREEN}{Style.BRIGHT}--- make relavant changes, you have -- {time_remaining} until re-encryption --- {next_symbol} {Style.RESET_ALL}",
          end="\r",
          flush=True)

dir_list_2 = os.listdir(secret_path)

for secret_file in dir_list_2:
    pyAesCrypt.encryptFile(
        os.path.join(secret_path, secret_file),
        os.path.join(secret_path, secret_file + ".aes"),
        password)

dir_list_3 = os.listdir(secret_path)


# clear sanctum <-- perhaps questionable ..
# would create race condition .. maybe sanctum
# should hold everything ever encrypted ..
"""
sanctum_list = os.listdir(sanctum_path)
for item in sanctum_list:
    os.remove(os.path.join(sanctum_path, item))
"""

# remove all non .aes files in secrets
# and copy all .aes to the inner sanctum.
for item in dir_list_3:
    if not item.endswith(".aes"):
        print(item)
        os.remove(os.path.join(secret_path, item))
    else:
        shutil.copy(
            os.path.join(secret_path, item),
            os.path.join(sanctum_path, item)
        )

print("\n")
print(f"{Fore.GREEN}{Style.BRIGHT}All files are now encrypted again.{Style.RESET_ALL}")


