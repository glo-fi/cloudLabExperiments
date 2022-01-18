#!/bin/bash

sleep 30

tcpdump -w /local/outfile.pcap &

wget http://10.10.1.2
