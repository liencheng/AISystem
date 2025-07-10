#!/bin/python
# -*- coding=utf-8 *-*

from colorama import init,Fore
from datetime import datetime
import time
import codecs
import sys
import os
import re
import struct
import codecs
reload(sys)
sys.setdefaultencoding('utf8')

class Color:
	def print_warn_text(self, print_text):
		print(Fore.MAGENTA + print_text)

	def print_red_text(self, print_text):
		print(Fore.RED + print_text)

	def print_green_text(self, print_text):
		print(Fore.GREEN + print_text)

	def print_blue_text(self, print_text):
		print(Fore.BLUE + print_text)
	
	def __init__(self):
		init(autoreset=True)
clr = Color()

def isUTF16ByFilePath(filePath):
	fileHandle = open(filePath, "rb");
	fileContent = fileHandle.read(2);
	fileHandle.close();
	val = struct.unpack("H", fileContent)[0];
	if int(0xFEFF) == val:
		return 1;
	else:
		return 0;

def fun_parse_all_txt_files(the_file_dir):
	path_list = os.listdir(the_file_dir)
	out_file_list = []
	for path_name in path_list:
		tmp_path_name = os.path.join(the_file_dir, path_name)
		if not os.path.isfile(tmp_path_name):
			continue
		
		type = (os.path.splitext(tmp_path_name))[1]
		if type != ".txt" :
			continue
			
		out_file_list.append(tmp_path_name)
	return out_file_list
	
def fun_replace_table_double_quotes(file_path):
	clr.print_green_text("begin relpace file [%s]" %(file_path))
	bIsUTF16 = isUTF16ByFilePath(file_path)
	if 1 == bIsUTF16:
		the_document = codecs.open(file_path, "rb", 'utf-16-le')
	else:
		the_document = open(file_path, "r")
		
	file_context = the_document.read()
	the_document.close()
	line_list = file_context.split('\n')
	line_num = len(line_list)
	new_file_context = ""
	line_idx = 0
	line_type = {}
	is_new_text = False
	while line_idx < line_num:
		line_data = line_list[line_idx]
		now_idx = line_idx
		line_idx += 1
		
		if line_data == '':
			continue
		
		#类型说明
		if now_idx == 1:
		   line_type = line_data.split('\t')
		   new_file_context = new_file_context +  line_data + "\n"
		   continue
				   
		if now_idx < 4 and now_idx != 3:
			new_file_context = new_file_context +  line_data + "\n"
			continue
			
		if line_data[0] == '#' and now_idx != 3:
			new_file_context = new_file_context +  line_data + "\n"
			continue
			
		line_temp = line_data.split('\t')
		num_col = len(line_temp)
		column_idx = 0
		new_line = ''
		while column_idx < num_col:
			old_coulmn_idx = column_idx
			column_idx += 1
			line_val = line_temp[old_coulmn_idx]
			if line_type[old_coulmn_idx].strip(' ').strip('\r') == "STRING" or now_idx == 3:	
			   val_len = len(line_val)		
			   if val_len > 2:
				  last_len = val_len
				  if line_val[val_len - 1] == '\r':
					 last_len = last_len - 1
					 
				  if last_len > 2:	 
					  bHead = (line_val[0] == '\"' and line_val[last_len -1] == '\"') or (line_val[0] == '“' and line_val[last_len - 1] == '”')
					  bMiddle = (line_val.find('""') > 0 or line_val.find('""') > 0)
					  if (bHead or bMiddle):
						  if bHead:
							new_val = line_val[1 : last_len - 1]
						  else:
							new_val = line_val[0 : last_len]
						  new_val = new_val.replace('""', '"')
						  new_val = new_val.replace('""', '"')
						  new_line += new_val
						  if last_len != val_len:
							 new_line += '\r'	
						  is_new_text = True
						  clr.print_red_text("relpace(%s) to new(%s)"%(line_val, new_val))
						  if column_idx != num_col:
							 new_line += '\t'
						  continue
					  
			new_line += line_val   
			if column_idx != num_col:
				new_line += '\t'
		new_file_context = new_file_context + new_line + '\n'
	
	if is_new_text == True:
		if 1 == bIsUTF16:
			the_newdocument = codecs.open(file_path, "wb", 'utf-16-le')
		else:
			the_newdocument = open(file_path, "w")
		the_newdocument.write(new_file_context)
		the_newdocument.close()

def fun_replace_tables_double_quotes(the_file_dir):
	file_list = fun_parse_all_txt_files(the_file_dir)
	file_num = len(file_list)
	if file_num <= 0:
		return True
	
	deal_idx = 0
	while deal_idx < file_num:
		file_path = file_list[deal_idx]
		deal_idx += 1
		fun_replace_table_double_quotes(file_path)
	
	
if __name__ == '__main__':
	clr.print_green_text("============")
	fun_replace_tables_double_quotes("..\\..\\PublicTables")
	fun_replace_tables_double_quotes("..\\..\\ServerTables")
	fun_replace_tables_double_quotes("..\\..\\ClientTables")
	clr.print_green_text("Relace finished")
	clr.print_green_text("============================================")
