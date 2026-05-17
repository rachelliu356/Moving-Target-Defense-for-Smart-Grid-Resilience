from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands.'''

    def build(self):
        '''Create custom topo.'''

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # Edge/Substation links: hosts to switches
        add_edge_link(self, h1, s1)
        add_edge_link(self, h2, s1)
        add_edge_link(self, h3, s2)
        add_edge_link(self, h4, s2)
        add_edge_link(self, h5, s3)
        add_edge_link(self, h6, s3)

        # Core Backbone links: switches to switches
        add_backbone_link(self, s1, s2)
        add_backbone_link(self, s2, s3)
        add_backbone_link(self, s3, s1)

topos = {'testtopo': (lambda: TestTopo())}