from mininet.topo import Topo
from utils.link_utils import add_backbone_link, add_edge_link

class IEEETopo(Topo):
    """24-switch topology for Mininet that maps to the communication infrastructure
    of the IEEE 24-Bus Reliability Test System (RTS) power system.
 
    Buses:
      - 138 kV buses : 1–10
      - 230 kV buses : 11–24
 
    Host types:
    - CC    (PDC aggregator / SCADA master, bidirectional)
            1 unit   → bus 13  (slack bus, co-located with PDC)
    - PMU   (IEEE C37.118 UDP, 60 fps, ~4.8 Kbps/PMU)
            10 units → buses 1, 2, 7, 13, 15, 16, 18, 21, 22, 23
    - IED   (DNP3 + IEC 61850 GOOSE, sub-4 ms trip signals)
            10 units → buses 3, 8, 9, 10, 11, 12, 13, 15, 23, 24
    - RTU   (SCADA, DNP3/TCP polled by Control Center)
            24 units → every bus (one RTU per bus, standard utility practice)
 
    Link parameters
    - Core Backbone   : delay 10–20 ms, bw 1 Gbps   (add_backbone_link)
    - Edge/Substation : delay 1–5 ms,  bw 100 Mbps  (add_edge_link)
 
    Follows the standard IEEE 24-bus RTS generator and branch data 
    (IEEE Reliability Test System Task Force, “IEEE reliability test system,” IEEE Trans. 
    PAS, 1979; updated as “IEEE reliability test system-96,” IEEE Trans. Power Syst., 1999).
    """

    PMU_BUSES = {1, 2, 7, 13, 15, 16, 18, 21, 22, 23}
    IED_BUSES = {3, 8, 9, 10, 11, 12, 13, 15, 23, 24}
    CC_BUS    = 13 

    def build(self):
        '''Create topo.'''

        # Switches (one per IEEE bus)
        switches = {}
        for bus in range(1, 25):
            switches[bus] = self.addSwitch(f"s{bus}")

        ## Hosts (Control Center, PMU, IED, RTU)
        
        # Control Center / PDC – Bus 13 (slack bus, 230 kV, 3×197 MW = 591 MW)
        cc = self.addHost(
            "cc13",
            ip=f"10.0.{self.CC_BUS}.1/24",
        )
        add_edge_link(self, cc, switches[self.CC_BUS])

        # PMU hosts – IEEE C37.118 UDP synchrophasor streams to PDC at Bus 13
        pmu_hosts = {}
        for bus in self.PMU_BUSES:
            h = self.addHost(
                f"pmu{bus}",
                ip=f"10.0.{bus}.10/24",
            )
            pmu_hosts[bus] = h
            add_edge_link(self, h, switches[bus])

        # IED hosts – DNP3 + GOOSE protection; sub-4 ms trip-signal budget
        ied_hosts = {}
        for bus in self.IED_BUSES:
            h = self.addHost(
                f"ied{bus}",
                ip=f"10.0.{bus}.20/24",
            )
            ied_hosts[bus] = h
            add_edge_link(self, h, switches[bus])

        # RTU hosts – one per bus, polled by CC via DNP3/TCP
        for bus in range(1, 25):
            h = self.addHost(
                f"rtu{bus}",
                ip=f"10.0.{bus}.30/24",
            )
            add_edge_link(self, h, switches[bus])

        ## Core Backbone Links
        
        # Tier 2 - PMU
        pmu_links = [
            (1, 2), (1, 3), 
            (3, 9),
            (7, 8),
            (8, 10),
            (9, 11),
            (10, 12),
            (11, 12), (11, 14), (11, 20),
            (12, 13),
            (13, 23),
            (14, 15),
            (15, 16),
            (18, 19),
            (19, 20),
            (21, 22),
            (22, 23)
        ]

        # Tier 3 - SCADA (RTU)
        scada_links = [
            (1, 2), (1, 3), (1, 4),
            (3, 9),
            (4, 5),
            (5, 9),
            (6, 10),
            (7, 8),
            (8, 10),
            (9, 11),
            (10, 12),
            (11, 12), (11, 14), (11, 24),
            (12, 13),
            (12, 20),
            (13, 23),
            (14, 15), (14, 16),
            (17, 18),
            (18, 21),
            (19, 20),
            (21, 22),
            (22, 23),
        ]

        for (bus1, bus2) in pmu_links:
            add_backbone_link(self, switches[bus1], switches[bus2])
        for (bus1, bus2) in scada_links:
            if (bus1, bus2) not in pmu_links:
                add_backbone_link(self, switches[bus1], switches[bus2])


topos = {'ieeetopo': (lambda: IEEETopo())}