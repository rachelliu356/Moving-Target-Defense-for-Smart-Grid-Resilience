from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands.'''

    def build(self):
        '''Create custom topo.'''

        # Add switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')
        s2 = self.addSwitch('s2', dpid='0000000000000002')
        s3 = self.addSwitch('s3', dpid='0000000000000003')

        # Add hosts with fixed MAC and IP
        h1 = self.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03', ip='10.0.0.3/24')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04', ip='10.0.0.4/24')

        # Tree structure: s1 is root, s2 and s3 are children
        self.addLink(s1, s2)
        self.addLink(s1, s3)

        # Hosts connect to leaf switches
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)
        
        # # Add switch
        # s0 = self.addSwitch('s0', dpid='0000000000000001')

        # # Add hosts
        # h0 = self.addHost('h0', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
        # h1 = self.addHost('h1', mac='00:00:00:00:00:02', ip='10.0.0.2/24')

        # # Edge/Substation links: hosts to switches
        # add_edge_link(self, h0, s0)
        # add_edge_link(self, h1, s0)

topos = {'testtopo': (lambda: TestTopo())}