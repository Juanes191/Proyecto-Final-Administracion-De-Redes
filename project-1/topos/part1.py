#!/usr/bin/python3
#!/usr/bin/python3 -tt

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.clean import cleanup

class part1_topo(Topo):
    def build(self, n=4):
        pass
        switch = self.addSwitch('S1')
        h1 = self.addHost('h1', ip = "10.0.1.2/24")
        h2 = self.addHost('h2', ip = "10.0.0.2/24")
        h3 = self.addHost('h3', ip = "10.0.0.3/24")
        h4 = self.addHost('h4', ip = "10.0.1.3/24")
        self.addLink(h1, switch)
        self.addLink(h2, switch)
        self.addLink(h3, switch)
        self.addLink(h4, switch)


def Test():
    topo = part1_topo(n=4)
    net = Mininet(topo)
    net.start()
    print ("Dump hosts")
    dumpNodeConnections(net.hosts)
    print ("Test de conexion")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    Test()
