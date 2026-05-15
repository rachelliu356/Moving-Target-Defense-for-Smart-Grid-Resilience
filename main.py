from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

from mininet_testing_topo import TestTopo

def run(topo):
    setLogLevel('info')
    net = Mininet(topo=topo, controller=OVSController, link=TCLink)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    topo = TestTopo()
    run(topo)