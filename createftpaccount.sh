#!/bin/bash

read abalo
echo $abalo


adduser -r $1

echo $1:"$2" | chpasswd

sudo mkdir -p /data/sftp/$1/$1-Files

sudo chown root:root /data/sftp/$1

sudo chmod 755 /data/sftp/$1

sudo chown $1:$1 /data/sftp/$1/$1-Files

sudo echo "##################################################
Match User $1
        ForceCommand internal-sftp
        PasswordAuthentication yes
        ChrootDirectory /data/sftp/$1
        PermitTunnel no
        AllowAgentForwarding no
        AllowTcpForwarding no
        X11Forwarding no" >> /etc/ssh/sshd_config

sudo systemctl restart sshd
