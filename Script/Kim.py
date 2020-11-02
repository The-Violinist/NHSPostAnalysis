#!/usr/bin/env python3

# Script:                 NHS Project 
# Author:                 Kimberly Dills
# Date of last revision:  11/2/2020
# Description of purpose: Brute Force Attack

import smtplib
import itertools
import sys
import time
from pexpect import pxssh
import zipfile
from shutil import copyfile
from sys import exit

    
def cracker(user, ipAddress, badFile, secret ):
    source = "C:\User\iexplorer\Downloads\registration.ext"
    target = "C:\User\iexplorer\Downloads\registration.ext"
    s=pxssh.pxssh()
    try: 
        copyfile(source, target)

    try:
        s.login(ipAddress, user, secret)
        s.sendline("cd C:\User\iexplorer\Downloads\registration.ext")
        break    
    except pxssh.ExceptionPxssh as e:
        print ("pxssh failed to login")
        print(e)
        time.sleep(1)

