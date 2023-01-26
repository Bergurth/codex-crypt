#!/bin/sh

current_dir=$(pwd)
secret_dir="${current_dir}/secrets"
shell_string="rm -rf ${secret_dir}/*"
echo $shell_string > /etc/init.d/crypt_script


ln -s /etc/init.d/crypt_script /etc/rc0.d/K99_crypt_script
ln -s /etc/init.d/crypt_script /etc/rc6.d/K99_crypt_script
chmod a+x /etc/init.d/crypt_script

