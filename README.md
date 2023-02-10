# Codex Crypt
A minimal, Personal or company/organization secret management system. A Chamber of Secrets, if you will.

# Installation
```
pip install -r requirements.txt
```
currently there is a setup.sh script that works on linux systems with systemd. If run on such a system thusly:
```
sudo bash setup.sh
```
It will make it so that, from then on the contents of the secrets folder are erased in the event of a system shutdown/reboot.


# Use

```
python open_crypt.py
```
This, after displaying some killer text-based artwork, will prompt you for a password, then decrypt all the contents of the secrets folder, if any, wrt. that password, prompt you for a number of minutes, Wait said number of minutes (allowing you to veiw the unencrypted files, add files, modify, ect.) then it will re-encrypt everything in the secrets folder, then copy all that into the sanctum folder encrypted for safe keeping.
The Idea is that, there should only ever be encrypted material in the sanctum folder. While the secrets folder will some of the time have unencrypted files.


# Warning

This program is only shown here for academic purposes. The author(s) of this program do not currently make any guarantees regarding the safety and or integrity
of any data that anyone might attempt to protect with it's use. Use at your own discretion.
