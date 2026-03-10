#!/bin/bash
set -e
 
# Amazon Linux 2023はpip3が標準でないためdnfでインストール
sudo dnf install -y python3-pip
 
cd /home/ec2-user/janken-app
/usr/bin/python3 -m pip install -r requirements.txt
