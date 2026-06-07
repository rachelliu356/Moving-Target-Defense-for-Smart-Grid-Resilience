from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands and traffic.'''

    def build(self):
        '''Create custom topo.'''

        # Add switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')

        # Add hosts with fixed MAC and IP
        h1 = self.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24')

        # Hosts connect to leaf switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)

topos = {'testtopo': (lambda: TestTopo())}