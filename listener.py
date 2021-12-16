import scapy.all as scapy
from scapy_http import http
import optparse
import os

os.system("figlet listener")

def inputs():

	object1 = optparse.OptionParser()
	object1.add_option("-i" , "--interface" , dest = "interface" , help = "enter your interface")
	input_of_user = object1.parse_args()[0]
	return input_of_user.interface

def listener(interface):

	scapy.sniff(iface = interface , store = False , prn = function)

def function(packets):

	packets.show()

listener(inputs())
