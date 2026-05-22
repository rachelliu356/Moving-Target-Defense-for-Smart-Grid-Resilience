import time
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from functools import partial

from mininet_test_topo import TestTopo

OVSSwitch14 = partial(OVSSwitch, protocols='OpenFlow14', failMode='standalone')

def run(topo):
    setLogLevel('info')
    net = Mininet(
        topo=topo,
        controller=RemoteController,
        switch=OVSSwitch14,
        link=TCLink
    )
    net.start()
    time.sleep(5)

    for sw in net.switches:
        sw.cmd('ovs-ofctl -O OpenFlow14 add-flow %s priority=0,actions=CONTROLLER:65535' % sw.name)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    topo = TestTopo()
    run(topo)