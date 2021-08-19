#!/usr/bin/python3


# (1) pip3 install pyshark
# (2) python3 tstream.py

import pyshark

file = "<pcap file>"

STREAM_NUMBER =  0

cap = pyshark.FileCapture(file,display_filter='tcp.stream eq %d' % STREAM_NUMBER)

while True:
	try:
	    p = cap.next()
	except StopIteration:
	    break
	try:
	    print(p.data.data.binary_value)
	except AttributeError:
	    pass
