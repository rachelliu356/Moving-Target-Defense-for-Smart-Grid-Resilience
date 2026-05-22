from mininet.net import Mininet
from mininet.node import OVSController, OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

from mininet_test_topo import TestTopo

def run(topo):
    setLogLevel('info')
    net = Mininet(
        topo=topo,
        controller=RemoteController,
        switch=OVSSwitch,
        link=TCLink
    )
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    topo = TestTopo()
    run(topo)