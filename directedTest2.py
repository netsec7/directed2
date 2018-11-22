#! /usr/bin/python

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh, wifiDirectLink, adhoc
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
from mininet.node import Controller, RemoteController
from mn_wifi.node import OVSKernelAP, UserAP, OVSAP
# # from mininet.util import dumpNodeConnections
# # from mininet.link import Link, Intf, TCLink, TCULink
# from scapy.layers.inet import *

import threading, time


def topology():
    "Create a network."
    global sta1, sta2, sta3, sta4, sta5, sta6, sta7,ctr, net
    net = Mininet_wifi(controller=Control, wmediumd_mode=interference,link=wmediumd,accessPoint=UserAP)

    info("***creating APs \n")
    ap1=net.addAccessPoint('ap1',ssid="apSSid",protocols='OpenFlow13',channel='1',inNamespace=True, position='200,200,0')

    info("*** Creating stations\n")
    sta1 = net.addStation('sta1', wlans=2, ssid='ssid1,',position='100,0,0')
    sta2 = net.addStation('sta2', wlans=2, ssid='ssid2,',position='100,100,0')
    sta3 = net.addStation('sta3', wlans=2, ssid='ssid3,',position='0,0,0')
    sta4 = net.addStation('sta4', wlans=2, ssid='ssid4,', position='100,150,0')
    sta5 = net.addStation('sta5', wlans=2, ssid='ssid5,', position='170,10,0')
    sta6 = net.addStation('sta6', wlans=2, ssid='ssid6,',position='150,150,0')
    sta7 = net.addStation('sta7', wlans=2, ssid='ssid7,', position='300,100,0')
    ctr=net.addStation('ctr',ip='10.0.0.254')

    info( "***Creating controller \n")
    c0=net.addController('c0', controller=Control, ip='10.0.0.254',port=6633)

    info("***plotting the graph \n")
    net.plotGraph(max_x=500, max_y=500)

    info("***configure wireless cards and range as propagation model \n")
    net.configureWifiNodes()
    net.propagationModel(model="logDistance", exp=4)

    info("*** Creating links\n")

    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)
    net.addLink(sta4, ap1)
    net.addLink(sta5, ap1)
    net.addLink(sta6, ap1)
    net.addLink(sta7, ap1)
    net.addLink(ctr, ap1)

    info("*** Starting network\n")
    net.build()


    #setting ip on other interface
    sta1.setIP('11.0.0.1/8', intf='sta1-wlan1',)
    sta2.setIP('11.0.0.2/8', intf='sta2-wlan1')
    sta3.setIP('11.0.0.3/8', intf='sta3-wlan1')
    sta4.setIP('11.0.0.4/8', intf='sta4-wlan1')
    sta5.setIP('11.0.0.5/8', intf='sta5-wlan1')
    sta6.setIP('11.0.0.6/8', intf='sta6-wlan1')
    sta7.setIP('11.0.0.7/8', intf='sta7-wlan1')
    # ctr.cmdPrint('python controlscript.py &')

    t=threading.Thread(target=threadStart)
    t.start()
    # x=threading.Thread(target=receivePackets)
    # x.start()
    # print(net.iperf(hosts='sta1,sta2'))

    c0.start()
    ap1.start([c0])

    ap1.cmd('ifconfig ap1-wlan1 10.0.0.200')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

def threadStart():

    "thread "
    listenForNodes()
    while(True):
        time.sleep(10)
        neighDiscover()
        # ctrl=ControlPlane.receivePackets()
        print(".....thread end line")
        time.sleep(10)


def neighDiscover():
        "Dicovers neighbor of each nodes and assigns as items into the list"

        info('***checking for neighbors \n')

        print("line one")
        stan1=sta1.cmdPrint('arp-scan --interface=sta1-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan1.pop(-1)
        sta1.cmdPrint('echo', stan1, '> neighborList1')
        stan2=sta2.cmdPrint('arp-scan --interface=sta2-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan2.pop(-1)
        sta2.cmdPrint('echo', stan2, '> neighborList2')
        stan3=sta3.cmdPrint('arp-scan --interface=sta3-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan3.pop(-1)
        sta3.cmdPrint('echo', stan3, '> neighborList3')
        stan4=sta4.cmdPrint('arp-scan --interface=sta4-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan4.pop(-1)
        sta4.cmdPrint('echo', stan4, '> neighborList4')
        stan5=sta5.cmdPrint('arp-scan --interface=sta5-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan5.pop(-1)
        sta5.cmdPrint('echo', stan5, '> neighborList5')
        stan6=sta6.cmdPrint('arp-scan --interface=sta6-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan6.pop(-1)
        sta6.cmdPrint('echo', stan6, '> neighborList6')
        stan7=sta7.cmdPrint('arp-scan --interface=sta7-wlan0 11.0.0.0/28 | egrep -o "(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])\.(25[0-4]|2[0-4][0-9]|[01][0-9][0-9]|[0-9][0-9]|[0-9])"').split('\r\n')
        stan7.pop(-1)
        sta7.cmdPrint('echo', stan7, '> neighborList7')

        # #delete last item as empty item due to split
        # for i in range(1,8):
        #     "stan"+str(i).pop(-1)
        # print(stan1)netdev


        sendFromNodes()
        # del stan1
        print("........neighDiscover completed\n")
        # for y in range(0,len(sta1Nlist)-1):
        # # info('*** checking bandwidth between nodes \n')
        # sta2Neigh=open("sta2Neigh.txt", "r")
        # sta2N=sta2Neigh.read()
        # sta2nn=re.findall(r"(.+?)+(\d)+(.+?)\s{2,}(\w)*", sta2N)
        # print(sta2nn)


def sendFromNodes():
    "send link information to the controller"
    #using scapy

    print("***sending LinkState information")

    sta1.cmdPrint('python packetSenderToCtrl.py 1')
    # receivePackets()

    sta2.cmdPrint('python packetSenderToCtrl.py 2')
    sta3.cmdPrint('python packetSenderToCtrl.py 3')
    sta4.cmdPrint('python packetSenderToCtrl.py 4')
    sta5.cmdPrint('python packetSenderToCtrl.py 5')
    sta6.cmdPrint('python packetSenderToCtrl.py 6')
    sta7.cmdPrint('python packetSenderToCtrl.py 7')


    # print(op)
    print("....packet Sent completed")


# def receivePackets():
#     "opens ports for listening in controller and other nodes"
#     ctr.cmdPrint('python controlscript.py')

def computation():
    "checks the file and computes the best route"
    pass
def listenForNodes():
    """receive computed tables by nodes ie open ports for Listen using scapy
        for now it is just the neighbor/ip table without computation f
    """
    ctr.cmdPrint('python controlscript.py &')
    sta1.cmdPrint('python node_receive.py 1 &')
    sta2.cmdPrint('python node_receive.py 2 &')
    sta3.cmdPrint('python node_receive.py 3 &')
    sta4.cmdPrint('python node_receive.py 4 &')
    sta5.cmdPrint('python node_receive.py 5 &')
    sta6.cmdPrint('python node_receive.py 6 &')
    sta7.cmdPrint('python node_receive.py 7 &')

def setPath():


        pass


class Control(RemoteController):
    def checkListening(self):

        return


    # def receivePackets(self):
    #     x=ctr.cmdPrint('python controlscript.py')
    #     print(x)
    #
    # def sendPackets( self):
    #     pass
    # def computation(self):
    #     pass


# class CustomControl(Controller):
#     def __init__(self, name, cdir, command='', cargs='', **kwargs):
#
#             Controller.__init__(self,name,cdir,command,cargs,**kwargs)
#
# controllers={'customController':CustomControl}

if __name__=='__main__':

    setLogLevel('info')
    topology()









