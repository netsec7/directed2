#!/usr/bin/env python
"receive packets sent by nodes to controller and computation of link state and send to the "
from scapy.layers.inet import *


def recvInController(packet):
    # print(packet.summary())



    # print("***Getting payload: ",packet[TCP].payload)



    # subprocess.call(["echo",packet[TCP].payload,"> n"])


    # srcIP=packet[0].getlayer(IP).src
    # print("***Getting packets from: ", packet[0].getlayer(IP).src)
    # a=packet[TCP].payload
    # print(type(a))
    # print(type(str(a)))
    # b=str(a)
    # subprocess.Popen(['echo {}> dummy'.format(str(a))], shell=True)
    # with open("dummy2","wr+") as f:
    #
    #     f.write(b)

    # f=open("neigh","w+")
    # popen2(['echo ',n,'> n'])
    time.sleep(3)

    if packet[0].getlayer(IP).src == "10.0.0.1":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC1","wr+") as file1:
            file1.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}>> dummy'.format("from 10.0.0.1")], shell=True)
    elif packet[0].getlayer(IP).src == "10.0.0.2":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC2","wr+") as file2:
            file2.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh2'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}> dummy'.format("from 10.0.0.2")], shell=True)

    elif packet[0].getlayer(IP).src == "10.0.0.3":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC3","wr+") as file3:
            file3.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh3'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}>> dummy'.format("from 10.0.0.3")], shell=True)

    elif packet[0].getlayer(IP).src == "10.0.0.4":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC4","wr+") as file4:
            file4.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh4'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}>> dummy'.format("from 10.0.0.4")], shell=True)

    elif packet[0].getlayer(IP).src == "10.0.0.5":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC5","wr+") as file5:
            file5.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh5'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}>> dummy'.format("from 10.0.0.5")], shell=True)

    elif packet[0].getlayer(IP).src == "10.0.0.6":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC6","wr+") as file6:
            file6.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh6'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}>> dummy'.format("from 10.0.0.6")], shell=True)

    elif packet[0].getlayer(IP).src == "10.0.0.7":
        print("*** receiving from",packet[0].getlayer(IP).src)
        with open("neighC7","wr+") as file7:
            file7.write(str(packet[TCP].payload))
        # subprocess.Popen(['echo {}> neigh7'.format(packet[TCP].payload)], shell=True)
        # subprocess.Popen(['echo {}>>dummy'.format("from 10.0.0.7")], shell=True)
    else:
        print("packets not received yet")
    # print >>
    print("************")
#     host=""getti
#     port=6633
#     buf=1024
#     addr=(host,port)
#     s=socket(AF_INET,SOCK_DGRAM)
#     s.bind(addr)
#     print("waiting to receive message")
#     while
#
#


     # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
     # s.bind(("10.0.0.254",6633))
     # while True:
     #     data, addr = s.recvfrom(1024)
     #     subprocess.call('echo', data, '> fileReceive')
     #     subprocess.call('echo', addr, '>> fileReceive')


while True:

    print("sniffing packets")
    sniff(iface='ctr-wlan0', prn=recvInController, filter="tcp")
    # print(packet)


