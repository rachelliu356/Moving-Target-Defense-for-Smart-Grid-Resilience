#!/usr/bin/env python3
import os
import time
import subprocess
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

    # popen correctly places the process inside the host's network namespace
    info('*** Starting GOOSE observer on h2\n')
    obs_log  = open('/tmp/goose_obs.log', 'w')
    h2.popen([GOOSE_OBS, 'h2-eth0'],
             stdout=obs_log, stderr=subprocess.STDOUT)

    time.sleep(1)

    info('*** Starting GOOSE publisher on h1\n')
    pub_log = open('/tmp/goose_pub.log', 'w')
    h1.popen([GOOSE_PUB, 'h1-eth0'],
             stdout=pub_log, stderr=subprocess.STDOUT)

    time.sleep(2)

    info('*** Starting GOOSE subscriber on h2\n')
    sub_log = open('/tmp/goose_sub.log', 'w')
    h2.popen([GOOSE_SUB, 'h2-eth0'],
             stdout=sub_log, stderr=subprocess.STDOUT)

    info('\n*** All GOOSE processes started\n')
    info('*** Check logs:\n')
    info('    h1 cat /tmp/goose_pub.log\n')
    info('    h2 cat /tmp/goose_obs.log\n')
    info('    h2 cat /tmp/goose_sub.log\n')
    info('    h2 tcpdump -i h2-eth0 ether proto 0x88b8 -c 3\n')

    CLI(net)

    obs_log.close()
    pub_log.close()
    sub_log.close()

    net.stop()


if __name__ == '__main__':
    run()