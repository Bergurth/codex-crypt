#!/bin/sh

current_dir=$(pwd)
secret_dir="${current_dir}/secrets"
echo -e "rm -rf ${secret_dir}/\*" > /${current_dir}/pre-shutdown.sh
sed -i 's/\\//g' $current_dir/pre-shutdown.sh
chmod a+x $current_dir/pre-shutdown.sh

echo -e "[Unit]\nDescription=Pre-Shutdown Processes\nDefaultDependencies=no\nAfter=final.target\n\n\n[Service]\nType=oneshot\nExecStart=/usr/bin/bash ${current_dir}/pre-shutdown.sh\n\n[Install]\nWantedBy=final.target"  > /etc/systemd/system/clear_crypt.service

chmod a+x /etc/systemd/system/clear_crypt.service

systemctl daemon-reload
systemctl enable clear_crypt.service


