# this uses python3 and pyAesCrypt
import pyAesCrypt
import sys
import os
from getpass import getpass

password = getpass()
secrets_path = os.path.join(os.getcwd(), "secrets")
# encrypt
pyAesCrypt.encryptFile(sys.argv[1],
                       os.path.join(secrets_path, sys.argv[1].replace(".txt",".aes")),
                       password)

