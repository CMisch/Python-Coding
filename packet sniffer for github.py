# building on U10A1 packet sniffer.py
#U10A1 Packet Sniffer
#This program will sniff TCP/UDP packets
#Created by Chris Misch
#resource found @ https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/

from scapy.all import IP, Ether, TCP, Raw, sniff
from scapy.all import *

#Grab HTTP info from www.capella.edu
cap=Ether()/IP(dst="www.capella.edu")/TCP()/"GET /index.html HTTP/1.0 \n\n"
#try against google.com
#cap=Ether()/IP(dst="www.google.com")/TCP()/"GET /index.html HTTP/1.0 \n\n"
#Print hex data from index.html
#print(hexdump(cap))
#print(ls(cap))
cap.show()
#This code sniffs all traffic from this monitor with a timeout of 5 seconds
#packet= sniff(filter="www.capella.edu",timeout= 5) #This returned 7 TCP packets and 6 UDP
#print(packet)
    
