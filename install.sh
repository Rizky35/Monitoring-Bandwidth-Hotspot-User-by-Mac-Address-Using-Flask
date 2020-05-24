#!/bin/bash

apt-get install python python-pip mongodb -y
pip install pymongo
pip install flask

chmod +x /root/flask/*
touch /etc/cron.d/hotspot
echo "52 23 * * * root /usr/bin/python /root/flask/mon.py >> /root/flask/logmon.txt 2>&1 &" > /etc/cron.d/hotspot

touch /etc/systemd/system/hotspot.service
echo "[Unit]\r\nDescription=This Script Run running on port 5000\r\n\r\n[Service]\r\nType=simple\r\nExecStart=/usr/bin/python /root/flask/index.py >> /root/flask/logindex.txt 2>&1 &\r\n\r\n[Install]\r\nWantedBy=multi-user.target" > /etc/systemd/system/hotspot.service
systemctl daemon-reload
