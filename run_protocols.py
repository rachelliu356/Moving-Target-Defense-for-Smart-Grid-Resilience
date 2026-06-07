#!/usr/bin/env python3
import os
import time
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from functools import partial

from topologies.mininet_test_topo import TestTopo

OVSSwitch14 = partial(OVSSwitch, protocols='OpenFlow14')

GOOSE_DIR = os.path.abspath('protocols/goose')
GOOSE_PUB = os.path.join(GOOSE_DIR, 'goose_publisher')
GOOSE_SUB = os.path.join(GOOSE_DIR, 'goose_subscriber')
GOOSE_OBS = os.path.join(GOOSE_DIR, 'goose_observer')


def run():
    setLogLevel('info')
    topo = TestTopo()
    net = Mininet(
        topo=topo,
        controller=RemoteController,
        switch=OVSSwitch14,
        link=TCLink
    )
    net.start()

    h1, h2 = net.get('h1'), net.get('h2')

    # Step 1 — start the observer on h2 first.
    # It accepts ALL GOOSE frames regardless of GoCbRef.
    # If this sees nothing, the problem is the network (ONOS/OVS),
    # not the publisher code.
    info('*** Starting GOOSE observer on h2 (h2-eth0)\n')
    h2.cmd(f'sudo {GOOSE_OBS} h2-eth0 > /tmp/goose_obs.log 2>&1 &')

    time.sleep(1)

    # Step 2 — start the publisher on h1.
    info('*** Starting GOOSE publisher on h1 (h1-eth0)\n')
    h1.cmd(f'sudo {GOOSE_PUB} h1-eth0 > /tmp/goose_pub.log 2>&1 &')

    time.sleep(2)

    # Step 3 — check observer output before starting subscriber.
    # This tells you whether frames are reaching h2 at all.
    info('*** Observer log so far:\n')
    obs_output = h2.cmd('cat /tmp/goose_obs.log')
    info(obs_output + '\n')

    # Step 4 — start the subscriber on h2.
    # This filters specifically on the GoCbRef the publisher uses.
    # If observer saw frames but subscriber sees nothing, the GoCbRef
    # strings don't match — check both files.
    info('*** Starting GOOSE subscriber on h2 (h2-eth0)\n')
    h2.cmd(f'sudo {GOOSE_SUB} h2-eth0 > /tmp/goose_sub.log 2>&1 &')

    info('\n*** All GOOSE processes started.\n')
    info('*** Useful commands inside the Mininet CLI:\n')
    info('    h2 cat /tmp/goose_obs.log   <- did frames arrive?\n')
    info('    h2 cat /tmp/goose_sub.log   <- did subscriber decode them?\n')
    info('    h1 cat /tmp/goose_pub.log   <- did publisher send successfully?\n')
    info('    h2 tcpdump -i h2-eth0 ether proto 0x88b8 -v\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    run()