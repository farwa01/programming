import netmiko
import time

print("Welcome to the remote access.")

connectionInfo = {
    'device_type':'cisco_ios',
    'host':'192.168.1.1',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}

print("Connecting via SSH...")
session = netmiko.ConnectHandler(**connectionInfo)
session.enable()
config = session.send_command("sh running-config")
session.close()

print("Saving configuration to a file!")
file = open("config-output.txt", "w")
file.write(config)
file.close()
time.sleep(2)

connectionInfoTelnet = {
    'device_type':'cisco_ios_telnet',
    'host':'192.168.1.1',
    'username':'cisco',
    'password':'cisco',
    'secret':'class'
}

print("Connecting via Telnet...")

session = netmiko.ConnectHandler(**connectionInfoTelnet)
session.enable()
config = session.send_command("sh running-config")
session.close()



