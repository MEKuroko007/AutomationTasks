# automate shutdown multiple desktops 
import time
import subprocess

while True :
    time_now=time.asctime(time.localtime(time.time()))
    time_split=time_now.split(' ')
    if time_split[3] =="01:16:00":
        list_pc = ["10.0.0.20","10.0.0.21"] #enter all ip of desktops that will shutdown
        for ip in list_pc:
            respone=subprocess.getoutput(f'ping {ip}')
            if " Received = 4" in respone :
                    print(subprocess.getoutput(f"shutdown  -m \\\\{ip} -s -f -t 0"))
        
        print(subprocess.getoutput('shutdown -f -s -t 0 -m \\\\127.0.0.1'))
