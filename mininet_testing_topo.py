# Simple topology for testing Mininet commands

from mininet.topo import Topo

class TestTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Add links
        self.addLink(h1, s3)
        self.addLink(s3, s4)
        self.addLink(s4, h2)

topos = { 'testtopo': ( lambda: TestTopo() ) }