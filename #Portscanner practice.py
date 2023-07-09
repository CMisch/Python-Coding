#U9A1 - Port Scanning
#This program will scan an IP address for any open ports between 1 and 1000
#Created by Chris Misch


import socket

#Create a function that takes host IP and start/end ports
def scan_ports(host, start_port, end_port):
    open_ports = []                         #Creates a list that holds each open port
#Create a loop that will try and loop through each port in range
    for port in range(start_port, end_port + 1):
        try:
#socket.socket() binds socket to a specific transport service 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)      #sets the lenght of time before signal times out
            result = sock.connect_ex((host, port))
#Create an if statment that adds found ports to open_ports variable
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
#return all open ports if found
    return open_ports

# Ask user for an IP to scan
host = input("Enter an IP to scan for open ports: ")

# Scan ports on the local machine
start_port = 1  # Starting port number
end_port = 1000  # Ending port number
#Return search request to user console
print(f"Scanning {host} for open ports...")
open_ports = scan_ports(host, start_port, end_port)

#Return open ports or if non found return no ports found
if open_ports:
    print("Open ports found:")
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print("No open ports found.")


