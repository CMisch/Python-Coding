#Sending and recieving a packet then unloading the packet header and body
#Created by Chris Misch

from scapy.all import Ether, IP, TCP, Raw 


#Create a packet to send 
packet = Ether()/IP(dst="172.64.152.139")/Raw(load="hello, there friend. ")

#unpack the packet
eth_layer = packet.getlayer(Ether)
ip_layer = packet.getlayer(IP)
payload = packet.getlayer(Raw)

#Access the IP header fields
source_ip = ip_layer.src
destination_ip = ip_layer.dst

#access the payload of the packet
payload_data = payload.load

#print the extracted information
print("Source IP: ", source_ip)
print("Destination IP: ", destination_ip)
print("Payload: ", payload_data)