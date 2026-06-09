def add_backbone_link(topo, node1, node2, bus1, bus2, bw=1000):
    '''
    Core Backbone link
    
    Switch to switch:
    1 Gbps bandwidth, 10-20 ms delay (ignore)
    '''
    topo.addLink(node1, node2, port1 = 100+bus1, port2 = 100+bus2, bw=bw)

def add_edge_link(topo, host, switch, host_type, bw=100):
    '''
    Edge/Substation link
    
    Host to switch:
    100 Mbps bandwidth, 1-5 ms delay (ignore)
    '''
    match host_type:
        case "ied":
            topo.addLink(host, switch, port1=0, port2=1, bw=bw)
        case "pmu":
            topo.addLink(host, switch, port1=0, port2=2, bw=bw)
        case "rtu":
            topo.addLink(host, switch, port1=0, port2=3, bw=bw)
        case "cc":
            topo.addLink(host, switch, port1=0, port2=4, bw=bw)
