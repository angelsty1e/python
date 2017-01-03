#####################################################################
# SNIFFING
# 03/02/2017
# JO
#####################################################################
from scapy.all import *
port = "Port de sniffing : "
port = raw_input(port)

sniff(filter=port, count=0, prn=None, lfilter=None, timeout=None, iface=All)
