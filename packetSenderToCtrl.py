#! /usr/bin/env python

import sys
from scapy.layers.inet import *

# sendLinkStateInfo(x=stan1)
def sendPkt():
    print("###entered packetSenderToCtrl")
    a=sys.argv[1]
    SA='10.0.0.%s'%a
    f=open('neighborList%s'%a,'r')
    x=f.read()
    print("********>",x)
    f.close()
    SA='10.0.0.%s'%sys.argv[1]
    if x is not None:
        print(x)
        pkt=IP(dst="10.0.0.254", src=SA)/TCP()/x
        send(pkt)
        time.sleep(3)

    # print(pkt)            #this line created issue when invoked as sta1.cmd() but runned well using xterm
        print("..... packet send end ")
    else:
        print('No packet found')


if __name__=='__main__':
    sendPkt()
