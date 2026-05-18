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

        # Add hosts
        h = [0]*6
        for i in range(len(h)):
            h[i] = self.addHost('h'+str(i))

        # Edge/Substation links: hosts to switches
        add_edge_link(self, h[0], s[0])
        add_edge_link(self, h[1], s[0])
        add_edge_link(self, h[2], s[1])
        add_edge_link(self, h[3], s[1])
        add_edge_link(self, h[4], s[2])
        add_edge_link(self, h[5], s[2])

        # Core Backbone links: switches to switches
        add_backbone_link(self, s[0], s[1])
        add_backbone_link(self, s[1], s[2])
        add_backbone_link(self, s[2], s[0])

topos = {'testtopo': (lambda: TestTopo())}