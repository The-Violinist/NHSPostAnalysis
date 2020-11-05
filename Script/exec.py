from pypsexec.client import Client

server = "192.168.0.60"
username = "IEUser"
password = "Passw0rd!"
executable = "whoami.exe"
arguments = "/all"

c = Client(server, username=username, password=password,  encrypt=False)

c.connect()
try:
    c.create_service()
    stdout, stderr, rc = c.run_executable("C:/Users/IEUser/Desktop/Registration/registration.exe")
except:
    print("done")