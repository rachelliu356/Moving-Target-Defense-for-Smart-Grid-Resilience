def add_backbone_link(topo, node1, node2, delay='20ms', bw=1000):
    '''
    Core Backbone link
    
    Switch to switch:
    1 Gbps bandwidth, 10-20 ms delay
    '''
    topo.addLink(node1, node2, bw=bw, delay=delay)

def add_edge_link(topo, node1, node2, delay='5ms', bw=100):
    '''
    Edge/Substation link
    
    Host to switch:
    100 Mbps bandwidth, 1-5 ms delay
    '''
    topo.addLink(node1, node2, bw=bw, delay=delay)