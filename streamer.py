#!/usr/bin/python

# Takes multiple pcap files (packet*.pcap) and...
### Combines them into one pcap (combined.pcap)
### Detects the number of TCP streams
### For each stream, converts it to ascii and stores them in order in a file (encoded_streams.txt)
### Converts URL (percent encoded) values to plaintext equivalent (decoded_streams.txt)

# Run this in the same directory as your packet*.pcap files

import urllib
from subprocess import call, Popen, PIPE

# System call to combine all the packets
call("mergecap -w <.pcap> packet*", shell=True)

# tshark -r combined.pcap -T fields -e tcp.stream | sort -u | wc -l
ps = Popen(['tshark', '-r<.pcap>','-Tfields', '-etcp.stream'], stdout=PIPE)
ps = Popen(['sort', '-u'], stdin=ps.stdout, stdout=PIPE)
ps = Popen(['wc', '-l'], stdin=ps.stdout, stdout=PIPE)
t = int(ps.stdout.read())

for i in range (0, t):
	#tshark -r combined.pcap -q -z follow,tcp,ascii,0
	f = open("encoded_streams.txt", "a+")
	command =  ["tshark", "-r<.pcap>", "-q", "-z", "follow,tcp,ascii," + str(i)]
	call(command, stdout=f)

# Takes a URL encoded file (such as a TCP stream) and decodes it.
fin = open("encoded_streams.txt")
fout = open("decoded_streams.txt", "wt")
for line in fin:
    fout.write(urllib.unquote(line))
fin.close()
fout.close()
