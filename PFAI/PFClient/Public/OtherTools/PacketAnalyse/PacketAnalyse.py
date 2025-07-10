#!/usr/bin/python
#-*- encoding: utf-8 -*-

from __future__ import division
from collections import defaultdict
from heapq import nlargest
import sys
import re
import os

def check_argv():
	usage_msg = "Usage: PacketAnalyse.py -topidx=num -logdir=dir -outputfile=logname"
	if len(sys.argv) != 4:
		print usage_msg
		return False
	
	#param_1
	param_list_1 = str(sys.argv[1]).split("=")
	if len(param_list_1) != 2:
		print usage_msg
		return False
	
	param = param_list_1[0]
	if param != "-topidx":
		print usage_msg
		return False
	
	#param_2
	param_list_2 = str(sys.argv[2]).split("=")
	if len(param_list_2) != 2:
		print usage_msg
		return False
	
	param = param_list_2[0]
	if param != "-logdir":
		print usage_msg
		return False
	
	#param_3
	param_list_3 = str(sys.argv[3]).split("=")
	if len(param_list_3) != 2:
		print usage_msg
		return False
	
	param = param_list_3[0]
	if param != "-outputfile":
		print usage_msg
		return False
	return True
	
def get_topidx():
	return int(str(sys.argv[1]).split("=")[1])

def get_logdir():
	return str(str(sys.argv[2]).split("=")[1])
	
def get_outputfile():
	return str(str(sys.argv[3]).split("=")[1])

def scan_file(path):
	for dirs,subdir,files in os.walk(path):
		for fn in files:
			if fn.find("PacketStat") >= 0:
				yield path + fn
	
def print_info(dict, top_idx, out_file, label_name):
	top_list = nlargest(top_idx, dict.items(),key = lambda x: x[1])
	#print "Toppest_" + label_name
	out_file.write("Toppest_" + label_name + "\n")
	out_file.write("RankIndex PacketName " + label_name + "\n")
	index = 1;
	for item in top_list:
			#print(index, item[0], item[1])
			out_file.write(str(index)+ " " + str(item[0]) + " " + str(item[1]) + "\n")
			index += 1;
	out_file.write("\n")

if check_argv() != True:
	exit(0)
	
receivecount_dict= defaultdict(int); 
receivesize_dict= defaultdict(int);	
sendcount_dict	= defaultdict(int);		
sendsize_dict	= defaultdict(int);
pakcetname_dict	= defaultdict(str);
packetsize_dict	= defaultdict(int);

file_path = get_outputfile()
top_idx = get_topidx()
log_dir = get_logdir()

file_list = list(scan_file(log_dir))
for lfile in file_list:
	with open(lfile) as logfile:
		for line in logfile:
			if 	line.find("CG_") >= 0 or \
				line.find("GC_") >= 0 or \
				line.find("XX_") >= 0:
				pak_name, recv_n, recv_size, send_n, send_size = line.split()
				recv_size = (int)(recv_size)
				recv_n = (int)(recv_n)
			
				send_size = (int)(send_size)
				send_n = (int)(send_n)
				
				receivesize_dict[pak_name] += recv_size
				receivecount_dict[pak_name] += recv_n
				
				sendsize_dict[pak_name] += send_size
				sendcount_dict[pak_name] += send_n
				
				pakcetname_dict[pak_name] = pak_name
				
				if recv_n > 0 and recv_size > 0:
					packetsize_dict[pak_name] = recv_size / recv_n
				
				if send_n > 0 and send_size > 0:
					packetsize_dict[pak_name] = send_size / send_n

out_file = open(file_path, "w");
out_file.write("Toppest_" + str(top_idx) + "_OutPut\n");

print_info(receivecount_dict, top_idx, out_file, "receivecount")
print_info(receivesize_dict, top_idx, out_file, "receivesize")
print_info(sendcount_dict, top_idx, out_file, "sendcount")
print_info(sendsize_dict, top_idx, out_file, "sendsize")
print_info(packetsize_dict,top_idx, out_file, "packetsize")
out_file.close()
