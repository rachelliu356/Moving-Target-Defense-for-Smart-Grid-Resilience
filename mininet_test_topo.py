from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands.'''

    def build(self):
        '''Create custom topo.'''

        # Add switches
        s0 = self.addSwitch('s0')

        # Add hosts
        h0 = self.addHost('h0')
        h1 = self.addHost('h1')

        # Edge/Substation links: hosts to switches
        add_edge_link(self, h0, s0)
        add_edge_link(self, h1, s0)

topos = {'testtopo': (lambda: TestTopo())}