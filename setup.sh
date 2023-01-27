#!/bin/sh

current_dir=$(pwd)
secret_dir="${current_dir}/secrets"
echo -e "rm -rf ${secret_dir}/\*" > /etc/init.d/crypt_script
sed -i 's/\\//g' /etc/init.d/crypt_script


ln -s /etc/init.d/crypt_script /etc/rc0.d/K99_crypt_script
ln -s /etc/init.d/crypt_script /etc/rc6.d/K99_crypt_script
chmod a+x /etc/init.d/crypt_script

