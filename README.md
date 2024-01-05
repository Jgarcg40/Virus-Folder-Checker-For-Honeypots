# VirusFolderChecker

This small script will be monitoring the folders that you put above it so that when a new file is introduced it will give you the virustotal report in another folder (a URL to the file analysis).
For it to work correctly, Virustotal's own API key is needed, which will be placed above in the code.
The application is designed to be used on Linux, in my case it has been used to record and analyze the viruses that reached my Honeypot.
I recommend using nohup so that it is always running in the background with this command: "nohup python tu_script.py &" (you can also use cron to start with the system: "@reboot nohup python3 /tu_script.py &").
