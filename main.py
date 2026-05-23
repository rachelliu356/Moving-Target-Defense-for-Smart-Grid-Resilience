from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from functools import partial

from mininet_test_topo import TestTopo

OVSSwitch14 = partial(OVSSwitch, protocols='OpenFlow14')

def run(topo):
    setLogLevel('info')
    net = Mininet(
        topo=topo,
        controller=RemoteController,
        switch=OVSSwitch14,
        link=TCLink
    )
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    topo = TestTopo()
    run(topo)