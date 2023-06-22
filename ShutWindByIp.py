import subprocess
computers_list=['192.168.1.200','192.168.1.201']
for c in computers_list:
    print(subprocess.getoutput("shutdown -m \\\\" + c + "-f -t 0"))
