# Monitoring Hotspot User by Mac Address Using Flask

# ===== File =====
index.py - Python Flask Rest API for input MikroTik Hotspot User Usage to MongoDB
mon.py - Calculate User Bandwidth Usage and Count User by MAC Address
rm.py - Python for remove User Bandwidth Usage and Count User by MAC Address
logmon.txt - Output log from mon.py file if an error.
MikroTik-to-Server.txt - Configuration MikroTik for Input to Server
install.sh - Installation file

# ===== Installation =====
1. Download all file and extract.

2. Move flask directory to root directory.

3. Run install.sh file on flask directory with this command "sh /root/flask/install.sh".
   command from file install.sh
   a. Install python, python-pip mongodb, pymongo, flask
   b. Add execute permission to file in /root/flask/
   c. Add /etc/cron.d/hotspot file to running mon.py at 11:52 PM
   d. Add /etc/systemd/system/hotspot.service file to start, stop, enable, and status this Script

4. Set Your Server Date with this command "timedatectl set-timezone (Time Zone)", example: timedatectl set-timezone Asia/Jakarta.

5. MongoDB will export to CSV file on /home/hotspot directory at 11:52 PM.

6. The /root/flask/mon.py process will write to /root/flask/logmon.txt.

7. Copy text in /root/flask/MikroTik-to-Server.txt file and put to MikroTik at IP > Hotspot > User Profile (Your user profile) > Script > On Logout (On bottom bar), and replace Server Address with Your Server IP Address.

8. To running this Script type "systemctl start hotspot" and if You want to start Script at boot You can type "systemctl enable hotspot",

9. (Optional) If You want to test the Script running or not You can replace "localhost" in /root/flask/index.py at line 21 with Your Server IP Address (at line 21 have 2 string "localhost").
