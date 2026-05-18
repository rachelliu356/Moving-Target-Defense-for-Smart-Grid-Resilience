from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class TestTopo(Topo):
    '''Simple topology for testing Mininet commands.'''

    def build(self):
        '''Create custom topo.'''

        # Add switches

        s = [0]*3
        for i in range(len(s)):
            s[i] = self.addSwitch('s'+str(i))
        # s1 = self.addSwitch('s1')
        # s2 = self.addSwitch('s2')
        # s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # Edge/Substation links: hosts to switches
        add_edge_link(self, h1, s[0])
        add_edge_link(self, h2, s[0])
        add_edge_link(self, h3, s[1])
        add_edge_link(self, h4, s[1])
        add_edge_link(self, h5, s[2])
        add_edge_link(self, h6, s[2])

        # Core Backbone links: switches to switches
        add_backbone_link(self, s[0], s[1])
        add_backbone_link(self, s[1], s[2])
        add_backbone_link(self, s[2], s[0])

topos = {'testtopo': (lambda: TestTopo())}