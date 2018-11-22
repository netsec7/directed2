#!/usr/bin/env python
"receive packets sent by controller;  open listening ports and save in file"
from scapy.layers.inet import *

b=sys.argv[1]

def recvInNodes(packet):
    print("###entered recvInNodes")
    print("*** receiving packets from",packet[0].getlayer(IP).src)
    with open("nodeReceive%s"%b,"wr+") as file:
        file.write(str(packet[TCP].payload))

while True:

    print("sniffing packets in Nodes")
    sniff(iface='sta%s-wlan0'%b, prn=recvInNodes, filter="tcp")
