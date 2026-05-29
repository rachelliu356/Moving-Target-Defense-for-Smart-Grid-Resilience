def add_backbone_link(topo, node1, node2, bw=1000):
    '''
    Core Backbone link
    
    Switch to switch:
    1 Gbps bandwidth, 10-20 ms delay (ignore)
    '''
    topo.addLink(node1, node2, bw=bw)

def add_edge_link(topo, node1, node2, bw=100):
    '''
    Edge/Substation link
    
    Host to switch:
    100 Mbps bandwidth, 1-5 ms delay (ignore)
    '''
    topo.addLink(node1, node2, bw=bw)