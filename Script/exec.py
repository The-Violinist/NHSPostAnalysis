from pypsexec.client import Client

server = "192.168.0.56"
username = "IEUser"
password = "Passw0rd!"
executable = "whoami.exe"
arguments = "/all"

c = Client(server, username=username, password=password,  encrypt=False)

c.connect()
try:
    c.create_service()
    # stdout, stderr, rc = c.run_executable("C:\\Users\\IEUser\\Desktop\\registration.exe")
    stdout, stderr, rc = c.run_executable("cmd.exe", arguments="/c copy \\\\WIN-4QHOB3UVE3F\\Patient\\test.txt c:\\Users\\IEUser\\Documents")
except:
    print("done")