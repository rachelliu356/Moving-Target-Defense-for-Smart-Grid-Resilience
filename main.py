from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from functools import partial

from topologies.mininet_test_topo import TestTopo
# from topologies.ieee_24_bus_rts_topo import IEEETopo

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
    # topo = IEEETopo()
    run(topo)