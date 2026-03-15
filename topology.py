from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

class MyTopo(Topo):
   
    def build(self):
        
        # Create 3 hosts
        h1 = self.addHost("h1", ip="10.0.0.1", mac="00:00:00:00:01:1e")
        h2 = self.addHost("h2", ip="10.0.0.2", mac="00:00:00:00:02:1e")
        h3 = self.addHost("h3", ip="10.0.0.3", mac="00:00:00:00:03:1e")

        # Create 1 switch
        s1 = self.addSwitch("s1")

        # Link all devices to form a star topology
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s1)

topos = {'mytopo': (lambda: MyTopo())}

if __name__ == "__main__":
    topo = MyTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip="127.0.0.1", port=6633))

    # Enable IP forwarding on the attacker host
    h3 = net.get("h3")
    h3.cmd("sysctl -w net.ipv4.ip_forward=1")

    net.start()
    CLI(net)
    net.stop()