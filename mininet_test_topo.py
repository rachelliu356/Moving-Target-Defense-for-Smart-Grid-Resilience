from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands.'''

    def build(self):
        '''Create custom topo.'''

        # Add switch
        s0 = self.addSwitch('s0', dpid='0000000000000001')

        # Add hosts
        h0 = self.addHost('h0', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
        h1 = self.addHost('h1', mac='00:00:00:00:00:02', ip='10.0.0.2/24')

        # Edge/Substation links: hosts to switches
        add_edge_link(self, h0, s0)
        add_edge_link(self, h1, s0)

topos = {'testtopo': (lambda: TestTopo())}