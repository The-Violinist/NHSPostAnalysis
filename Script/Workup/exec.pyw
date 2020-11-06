from pypsexec.client import Client

server = "192.168.0.60"
username = "IEUser"
password = "Passw0rd!"
executable = "uninstall.exe"
# arguments = "/all"

cli = Client(server, username=username, password=password,  encrypt=False)

cli.connect()
try:
    # import pdb; pdb.set_trace()
    cli.create_service()
    stdout, stderr, rc = cli.run_executable("C:/Users/IEUser/Downloads/Registration/reg.exe")
    print(stdout, stderr, rc)
except:
    # import pdb; pdb.set_trace()
    print("done")
finally:
    cli.remove_service
    cli.disconnect