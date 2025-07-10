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


_g_error_file_total = []
_g_error_msg_total = []
_g_table_data = {}

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

def fun_check_tab_str_utf8(str_value):
	str_val_len = 0
	try:
		val = str_value.decode("gbk").encode("utf-8")
		str_val_len = len(val)
	except:
		return True
	else:
		if str_val_len > 510:
			return False
	return True
	
def fun_check_tab_str_special_str(str_value):
	if len(str_value) <= 0:
		return True
		
	firstchar = str_value[0:1]
	if firstchar == "\"" or firstchar == "“":
		return False 

	return True

def fun_check_is_float(str_float):
	the_cmp_tt = str_float
	if len(str_float) > 0 and '-' == str_float[0]:
		the_cmp_tt = str_float[1:]
	try:
		if len(str_float) <= 0:
			return True
		val = float(the_cmp_tt)
		return True
	except:
		return False

def fun_check_is_int(str_int):
	the_temp_str = str_int
	if len(str_int) > 0 and '-' == str_int[0]:
		the_temp_str = str_int[1:]
	return 0 == len(str_int) or the_temp_str.isdigit()

def fun_parse_line(key, line_data):
	#MAX_ID=99999;MAX_RECORD=10241;TableType=Hash;
	line_list = re.split("#|=|;",line_data)
	line_num = len(line_list)
	line_idx = 0
	while line_idx < line_num:
		tmp_key = line_list[line_idx]
		line_idx += 1
		if tmp_key == key:
			return line_list[line_idx]
	return ""

def fun_check_server_line(list_file_header_info, list_data):
	file_path_name = list_file_header_info["file_name"]
	len_a = len(list_file_header_info["type"])
	len_b = len(list_file_header_info["ign"])
	len_c = len(list_data)

	if len_a != len_b or len_a != len_c:
		clr.print_red_text("column num error")
		return False

	list_ignor = list_file_header_info["ign"]
	list_type = list_file_header_info["type"]
	list_name = list_file_header_info["name"]
	len_idx = 0
	is_check_ok = True
	while len_idx < len_a:
		now_idx = len_idx
		len_idx += 1

		colum_name = list_name[now_idx]
		vtype = list_type[now_idx]
		val = list_data[now_idx]
		
		if vtype == "STRING" and True != fun_check_tab_str_utf8(val):
			msg = "column[%s] string value too long"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
		if vtype == "STRING" and fun_parse_file_name(file_path_name) == "StrDictionary" and True != fun_check_tab_str_special_str(val):
			msg = "column[%s] string value first char contain \""
			log_msg = msg %(colum_name)
			is_check_ok = False
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue 
		if vtype == "FLOAT" and True != fun_check_is_float(val):
			msg = "column[%s] is float but value is str"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
		if vtype == "INT" and True != fun_check_is_int(val):
			msg = "column[%s] is int but value is str"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue

		if val != "" or vtype == "STRING":
			continue

		if now_idx == len_a - 1:
			msg = "column[%s] data is empty"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
	return is_check_ok

def fun_make_file_data_map(list_file_header_info, list_data):
	list_name = list_file_header_info["name"]
	ret_data_map = {}
	list_num = len(list_data)
	list_idx = 0
	while list_idx < list_num:
		name = list_name[list_idx]
		ret_data_map[name] = list_data[list_idx]
		list_idx += 1
	return ret_data_map

def fun_parse_file_name(file_path):
	file_path_list = file_path.replace("\\","/").split("/")
	idx = len(file_path_list) - 1
	return file_path_list[idx].split(".")[0]

def fun_parse_server_txt(file_path):
	clr.print_green_text("[INFO] begin parse file[%s]" %(file_path))

	bIsUTF16 = isUTF16ByFilePath(file_path)
	if 1 == bIsUTF16:
		the_document = codecs.open(file_path, "rb", 'utf-16-le')
	else:
		# the_document = codecs.open(file_path, "r", "utf-8")
		the_document = open(file_path, "r")

	file_context = the_document.read()
	the_document.close()

	line_list = file_context.split('\n')
	line_num = len(line_list)

	list_file_header_info = {}
	list_file_data = {}
	list_table_id = []
	max_id_calc = -1
	max_id_std = -1
	max_record_calc = 0
	max_record_std = -1

	list_file_header_info["file_name"] = file_path
	line_idx = 0
	is_check_ok = True
	while line_idx < line_num - 1:
		line_data = line_list[line_idx]
		now_idx = line_idx
		line_idx += 1

		if now_idx == 0:
			#列名字
			temp = line_data.split('\t')
			list_file_header_info["name"] = temp
			continue

		if now_idx == 1:
			#类型说明
			temp = line_data.split('\t')
			for type_it in temp:
				if "" != type_it.strip(' '):
					continue
				
				is_check_ok = False
				log_msg = "Type Empty!!!"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = "unknow"
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
			list_file_header_info["type"] = temp
			continue

		if now_idx == 2:
			#忽略列说明
			temp = line_data.split('\t')
			list_file_header_info["ign"] = temp

			#最大项说明
			max_record_std = fun_parse_line(
				"MAX_RECORD", 
				line_data)

			max_id_std = fun_parse_line(
				"MAX_ID", 
				line_data)

			max_id_std = int(max_id_std)
			max_record_std = int(max_record_std)
			continue

		if now_idx < 4:
			continue

		if line_data == '':
			log_msg = "have empty line"
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = now_idx
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue
	
		if line_data[0] == '#' :
			continue

		line_temp = line_data.split('\t')
		num_col = len(line_temp)
		if num_col <= 0 :
			log_msg = "line have no column data"
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = "unknow"
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue

		if line_temp[0] == '':
			log_msg = "have empty id"
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = now_idx
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue

		flag = fun_check_server_line(list_file_header_info, 
			line_temp)
		if flag != True:
			log_msg = "check table colum num failed"
			line_id = int(line_temp[0])
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = line_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue
		else:
			#计算最大ID和记录数
			line_map = fun_make_file_data_map(
				list_file_header_info,
				line_temp)
			line_id = int(line_temp[0])
			
			#最后一列不允许为空
			if line_temp[num_col - 1] == "" :
				log_msg = "the last column is empty"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = line_id
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
				is_check_ok = False
				continue

			flag = list_file_data.has_key(line_id)
			if flag == True:
				is_check_ok = False
				log_msg = "Repeat Id"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = line_id
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
				break

			list_file_data[line_id] = line_map
			list_table_id.append(line_id)
			max_record_calc += 1

			if line_id > max_id_calc:
				max_id_calc = line_id
			continue

	if max_record_calc > max_record_std:
		is_check_ok = False
		log_msg = "MAX_RECORD"
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = file_path
		error_msg["id"] = "unknow"
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)

	if max_id_calc > max_id_std:
		is_check_ok = False
		log_msg = "MAX_ID"
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = file_path
		error_msg["id"] = "unknow"
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)

	file_short_name = fun_parse_file_name(file_path)
	file_temp = {}
	file_temp["head"] = list_file_header_info
	file_temp["data"] = list_file_data
	file_temp["ids"] = list_table_id
	_g_table_data[file_short_name] = file_temp
	if is_check_ok == True:
		log_msg = "[OK] parse file[%s]"
		clr.print_green_text(log_msg %(file_path))
		return
	_g_error_file_total.append("[FAILED] parse file[%s]" %(file_path))
	
def fun_do_parse_server_txt_file(the_file_dir):
	file_list = fun_parse_all_txt_files(the_file_dir)
	file_num = len(file_list)
	if file_num <= 0:
		return True
	
	deal_idx = 0
	while deal_idx < file_num:
		file_path = file_list[deal_idx]
		deal_idx += 1
		fun_parse_server_txt(file_path)

def fun_check_client_line(list_file_header_info, list_data):
	file_path_name = list_file_header_info["file_name"]
	len_a = len(list_file_header_info["type"])
	len_b = len(list_data)

	if len_a != len_b:
		clr.print_red_text("column num error")
		return False

	list_type = list_file_header_info["type"]
	list_name = list_file_header_info["name"]
	len_idx = 0
	is_check_ok = True
	while len_idx < len_a:
		now_idx = len_idx
		len_idx += 1

		colum_name = list_name[now_idx]
		vtype = list_type[now_idx]
		val = list_data[now_idx]

		if vtype == "FLOAT" and True != fun_check_is_float(val):
			msg = "column[%s] is float but value is str"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
		if vtype == "STRING"  and fun_parse_file_name(file_path_name) == "StrDictionary" and True != fun_check_tab_str_special_str(val):
			msg = "column[%s] string value first char contain \""
			log_msg = msg %(colum_name)
			is_check_ok = False
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue 
		if vtype == "INT" and True != fun_check_is_int(val):
			msg = "column[%s] is int but value is str"
			log_msg = msg %(colum_name)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path_name
			error_msg["id"] = list_data[0]
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
	return is_check_ok

def fun_do_parse_cli_white_file():
	the_special_symble_file = open("./tool_config.ini", "r")
	total_lines = the_special_symble_file.readlines()
	the_special_symble_file.close()

	ret_data_info = []
	key_flag = False
	for raw_line in total_lines:
		line = raw_line.strip(' ').strip('\r').strip('\n')
		if len(line) <= 0 or True == line.startswith("#"):
			continue
		
		if line.startswith("[no_check]"):
			key_flag = True
			continue
		
		if key_flag and line.startswith("["):
			break
		
		if True != key_flag:
			continue
		ret_data_info.append(line)
	return ret_data_info

def fun_parse_client_txt(file_path):
	clr.print_green_text("[INFO] begin parse file[%s]" %(file_path))

	bIsUTF16 = isUTF16ByFilePath(file_path)
	if 1 == bIsUTF16:
		the_document = codecs.open(file_path, "rb", 'utf-16-le')
	else:
		# the_document = codecs.open(file_path, "r", "utf-8")
		the_document = open(file_path, "r")

	file_context = the_document.read()
	the_document.close()

	line_list = file_context.split('\n')
	line_num = len(line_list)

	list_file_header_info = {}
	list_file_data = {}
	list_table_id = []
	
	list_file_header_info["file_name"] = file_path
	line_idx = 0
	is_check_ok = True
	real_num_index = 0
	while line_idx < line_num - 1:
		line_data = line_list[line_idx]
		now_idx = line_idx
		line_idx += 1
		
		if line_data[0] == '#' :
			continue
			
		real_num_index += 1
		if real_num_index == 1:
			#列名字
			temp = line_data.split('\t')
			list_file_header_info["name"] = temp
			continue

		if real_num_index == 2:
			#类型说明
			temp = line_data.split('\t')
			for type_it in temp:
				if "" != type_it.strip(' '):
					continue
				
				is_check_ok = False
				log_msg = "Type Empty!!!"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = "unknow"
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
			list_file_header_info["type"] = temp
			continue
		
		line_temp = line_data.split('\t')
		if len(line_temp) <= 0 :
			log_msg = "line have no column data"
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = "unknow"
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue

		flag = fun_check_client_line(list_file_header_info, 
			line_temp)
		if flag != True:
			log_msg = "check table colum num failed"
			line_id = int(line_temp[0])
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = file_path
			error_msg["id"] = line_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			is_check_ok = False
			continue
		else:
			if "" == line_temp[0]:
				log_msg = "id is empty"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = "unknow"
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
				is_check_ok = False
				continue
				
			line_map = fun_make_file_data_map(
				list_file_header_info,
				line_temp)
			
			line_id = int(line_temp[0])
			flag = list_file_data.has_key(line_id)
			if flag == True:
				is_check_ok = False
				log_msg = "Repeat Id"
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = file_path
				error_msg["id"] = line_id
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
				break
			list_table_id.append(line_id)
			list_file_data[line_id] = line_map

	file_short_name = fun_parse_file_name(file_path)
	file_temp = {}
	file_temp["head"] = list_file_header_info
	file_temp["data"] = list_file_data
	file_temp["ids"] = list_table_id
	_g_table_data[file_short_name] = file_temp
	if is_check_ok == True:
		log_msg = "[OK] parse file[%s]"
		clr.print_green_text(log_msg %(file_path))
		return
	_g_error_file_total.append("[FAILED] parse file[%s]" %(file_path))

def fun_do_parse_client_txt_file(the_file_dir):
	file_list = fun_parse_all_txt_files(the_file_dir)
	file_num = len(file_list)
	if file_num <= 0:
		return True
	
	white_file_list = fun_do_parse_cli_white_file()
	deal_idx = 0
	while deal_idx < file_num:
		file_path = file_list[deal_idx]
		deal_idx += 1
		file_name = os.path.split(file_path)[1]
		if file_name in white_file_list:
			continue
		fun_parse_client_txt(file_path)

def fun_do_parse_special_symble_config():
	the_special_symble_file = open("./tool_config.ini", "r")
	total_lines = the_special_symble_file.readlines()
	the_special_symble_file.close()

	ret_data_info = []
	key_flag = False
	for raw_line in total_lines:
		line = raw_line.strip(' ').strip('\r').strip('\n')
		if len(line) <= 0 or True == line.startswith("#"):
			continue
		
		if line.startswith("[special_symble]"):
			key_flag = True
			continue
		
		if key_flag and line.startswith("["):
			break
		
		if True != key_flag:
			continue
		
		t_array = line.split("#")
		if 3 != len(t_array):
			continue
		ret_data_info.append(t_array)
	return ret_data_info

def fun_check_special_symble():
	the_check_array = fun_do_parse_special_symble_config()
	for t_array in the_check_array:
		table_name = t_array[0]
		col_name = t_array[1]
		symbles = t_array[2]
		if not _g_table_data.has_key(table_name):
			continue
		table_t = _g_table_data[table_name]
		table_datas = table_t["data"]
		key_id_list = table_datas.keys()
		
		is_find_error = False
		for table_id in key_id_list:
			table_line = table_datas[table_id]
			if not table_line.has_key(col_name):
				continue
			
			data_col = table_line[col_name]
			if re.search(symbles,data_col):
				err_msg = "(%s) %s" %(symbles, data_col)
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = table_name
				error_msg["id"] = table_id
				error_msg["msg"] = err_msg
				_g_error_msg_total.append(error_msg)
				is_find_error = True
		if True == is_find_error:
			msg = "[FAILED] check symbles[%s] colum[%s]" \
				%(table_name, col_name)
			clr.print_red_text(msg)
	clr.print_green_text("[OK] check special symbles finshed")

def fun_check_idip_white_item():
	table_name = "IdipWhiteItem"
	if not _g_table_data.has_key(table_name):
		return
	
	table_t = _g_table_data[table_name]
	t_data_list = table_t["data"]
	key_id_list = table_t["ids"]
	is_find_error = False
	for table_id in key_id_list:
		table_line = t_data_list[table_id]
		str_int = table_line["MaxNum"]
		flag = fun_check_is_int(str_int)
		if True == flag:
			num = int(str_int)
			if num > 0 and num <= 100000:
				continue
		error_msg = {}
		error_msg["msg"] = "max num err"
		error_msg["type"] = "error"
		error_msg["file"] = table_name
		error_msg["id"] = table_id
		_g_error_msg_total.append(error_msg)
		is_find_error = True				
	if True == is_find_error:
		msg = "[FAILED] [%s]" %(table_name)
		clr.print_red_text(msg)
		return
	clr.print_green_text("[OK] check idip_white_item finshed")

def fun_do_parse_id_must_inc_config():
	the_special_symble_file = open("./tool_config.ini", "r")
	total_lines = the_special_symble_file.readlines()
	the_special_symble_file.close()

	ret_data_info = []
	key_flag = False
	for raw_line in total_lines:
		line = raw_line.strip(' ').strip('\r').strip('\n')
		if len(line) <= 0 or True == line.startswith("#"):
			continue
		
		if line.startswith("[id_must_inc]"):
			key_flag = True
			continue
		
		if key_flag and line.startswith("["):
			break
		
		if True != key_flag:
			continue
		ret_data_info.append(line)
	return ret_data_info

def fun_check_id_must_inc():
	the_check_array = fun_do_parse_id_must_inc_config()
	for table_name in the_check_array:
		if not _g_table_data.has_key(table_name):
			continue
		table_t = _g_table_data[table_name]
		key_id_list = table_t["ids"]
		
		is_find_error = False
		last_table_id = -1
		for table_id in key_id_list:
			if table_id <= last_table_id:
				err_msg = "table id increase [%d]" \
					%(last_table_id)
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = table_name
				error_msg["id"] = table_id
				error_msg["msg"] = err_msg
				_g_error_msg_total.append(error_msg)
				is_find_error = True
				continue
			last_table_id = table_id
		if True == is_find_error:
			msg = "[FAILED] tableid inc[%s]" %(table_name)
			clr.print_red_text(msg)
	clr.print_green_text("[OK] check table id increase finshed")

def fun_do_parse_id_auto_inc_config():
	the_special_symble_file = open("./tool_config.ini", "r")
	total_lines = the_special_symble_file.readlines()
	the_special_symble_file.close()

	ret_data_info = []
	key_flag = False
	for raw_line in total_lines:
		line = raw_line.strip(' ').strip('\r').strip('\n')
		if len(line) <= 0 or True == line.startswith("#"):
			continue
		
		if line.startswith("[id_auto_inc]"):
			key_flag = True
			continue
		
		if key_flag and line.startswith("["):
			break
		
		if True != key_flag:
			continue
		
		t_data = line.split("#")
		if 2 != len(t_data):
			continue
		ret_data_info.append(t_data)
	return ret_data_info

def fun_check_id_must_auto_inc():
	the_check_array = fun_do_parse_id_auto_inc_config()
	for table_rule in the_check_array:
		if not _g_table_data.has_key(table_rule[0]):
			continue
		tableid_auto_inc = int(table_rule[1])
		table_name = table_rule[0]
		table_t = _g_table_data[table_name]
		key_id_list = table_t["ids"]
		
		is_find_error = False
		last_table_id = -1
		for table_id in key_id_list:
			if table_id != tableid_auto_inc:
				err_msg = "tableid auto increase [%d]" \
					%(tableid_auto_inc)
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = table_name
				error_msg["id"] = table_id
				error_msg["msg"] = err_msg
				_g_error_msg_total.append(error_msg)
				is_find_error = True
				break
			tableid_auto_inc += 1
		if True == is_find_error:
			msg = "[FAILED] tableid inc[%s]" %(table_name)
			clr.print_red_text(msg)
	clr.print_green_text("[OK] check table id increase finshed")

def fun_print_error_files():
	err_num = len(_g_error_file_total)
	err_idx = 0
	while err_idx < err_num:
		now_idx = err_idx
		err_idx += 1
		clr.print_red_text(_g_error_file_total[now_idx])

def fun_is_have_data(table_name, table_id):
	flag = _g_table_data.has_key(table_name)
	if flag != True :
		return False

	tar_table = _g_table_data[table_name]
	return tar_table["data"].has_key(int(table_id))

def fun_check_table_depend():
	#NpcAttr中ID在RoleBaseAttr中存在
	the_check_data_list = _g_table_data["NpcAttr"]["data"]
	key_id_list = the_check_data_list.keys()
	line_num = len(key_id_list)
	line_idx = 0
	is_check_ok = True
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		the_check_id = key_id_list[now_idx]

		flag = fun_is_have_data("RoleBaseAttr",
			the_check_id)
		if flag != True:
			msg = "NpcAttr[%d] Not In RoleBaseAttr"
			log_msg = msg %(the_check_id)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "NpcAttr"
			error_msg["id"] = "unknow"
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
	if is_check_ok == True:
		msg = "[OK] check file[NpcAttr]"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check file[NpcAttr]")

	#ZombieAttr中ID在RoleBaseAttr中存在
	the_check_data_list = _g_table_data["ZombieAttr"]["data"]
	key_id_list = the_check_data_list.keys()
	line_num = len(key_id_list)
	line_idx = 0
	is_check_ok = True
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		data_id = key_id_list[now_idx]
		the_check_id = the_check_data_list[data_id]["RoleId"]
		flag = fun_is_have_data("RoleBaseAttr",
			the_check_id)
		if flag != True:
			msg = "ZombieAttr[%s] Not In RoleBaseAttr"
			log_msg = msg %(the_check_id)
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "ZombieAttr"
			error_msg["id"] = "unknow"
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
	if is_check_ok == True:
		msg = "[OK] check file[ZombieAttr]"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check file[ZombieAttr]")

	#CommonItem中可以摆摊的Item数量上限控制
	the_check_data_list = _g_table_data["CommonItem"]["data"]
	key_id_list = the_check_data_list.keys()
	line_num = len(key_id_list)
	line_idx = 0
	is_check_ok = True
	stall_item_num = 0
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		data_id = key_id_list[now_idx]
		flag = the_check_data_list[data_id]["StallItemID"]
		if int(flag) != -1:
			stall_item_num += 1

		if stall_item_num > 19500:
			log_msg = "CommonItem Too Manay StallItem"
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "CommonItem"
			error_msg["id"] = "unknow"
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
		
		flag = the_check_data_list[data_id]["MaxStackSize"]
		if int(flag) > 9999:
			log_msg = "CommonItem MaxStackSize > 9999"
			is_check_ok = False

			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "CommonItem"
			error_msg["id"] = data_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
	if is_check_ok == True:
		msg = "[OK] check file[CommonItem]"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check file[CommonItem]")
		
def fun_check_dlc_update_time():
	#DLCVersion两个不能低于8天
	the_check_data_list = _g_table_data["DLCVersion"]["data"]
	key_id_list = the_check_data_list.keys()
	line_num = len(key_id_list)
	line_idx = 0
	is_check_ok = True
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		the_check_id = key_id_list[now_idx]
		next_line_idx = line_idx
		check_line = the_check_data_list[the_check_id]
		check_update_time_str = check_line["UpdateDateTime"]
		check_update_time_str += "000000"
		check_update_time = time.strptime(check_update_time_str, "%Y%m%d%H%M%S")
		while next_line_idx < line_num:
			the_next_check_id = key_id_list[next_line_idx]
			next_check_line = the_check_data_list[the_next_check_id]
			next_check_update_time_str = next_check_line["UpdateDateTime"]
			next_check_update_time_str += "000000"
			next_check_update_time = time.strptime(next_check_update_time_str, "%Y%m%d%H%M%S")
			elapseTime = (time.mktime(next_check_update_time) - time.mktime(check_update_time))
			if elapseTime < 0:
				elapseTime *= -1
			if (elapseTime < 8 * 24 * 60 * 60):
				msg = "DLCVersionId1[%d] Id2[%d] UpdateTime Less than 8 days In DLCVersion"
				log_msg = msg %(key_id_list[line_idx], key_id_list[next_line_idx])
				is_check_ok = False
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = "DLCVersion"
				error_msg["id"] = "unknow"
				error_msg["msg"] = log_msg
				_g_error_msg_total.append(error_msg)
				
			next_line_idx += 1
			  		
	if is_check_ok == True:
		msg = "[OK] check file[DLCVersion]"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check file[DLCVersion]")

def fun_parse_sequip_check_ids():
	table_equip_map = _g_table_data["EquipAttr"]["data"]
	table_equip_ids = _g_table_data["EquipAttr"]["ids"]
	ret_equip_ids = []
	for tab_id in table_equip_ids:
		flag = table_equip_map.has_key(tab_id)
		if True != flag:
			continue
		data_map = table_equip_map[tab_id]
		flag = data_map["RandWeightId"]
		if "-1" == flag:
			continue
		ret_equip_ids.append(int(tab_id))
	return ret_equip_ids

def fun_check_sequip_ids():
	is_check_ok = True	
	id_array_2 = _g_table_data["ArtifactAttrTips"]["ids"]
	src_data_2 = _g_table_data["EquipAttr"]["data"]
	for id in id_array_2:
		flag = src_data_2.has_key(id)
		if True == flag:
			val = int(src_data_2[id]["RandWeightId"])
			if -1 != val:
				continue
		msg = "EquitCheck [%d] Not In EquipAttr"
		log_msg = msg %(int(id))
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "EquipAttr"
		error_msg["id"] = "unknow"
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		is_check_ok = False
	if is_check_ok == True:
		msg = "[OK] check static attr equip"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check static attr equip")

def fun_check_sequip_attr_base():
	is_check_ok = True
	table_map_a = _g_table_data["ArtifactAttrTips"]["data"]
	table_map_b = _g_table_data["EquipAttr"]["data"]
	deal_equip_ids = fun_parse_sequip_check_ids()
	for id in deal_equip_ids:
		flag_a = table_map_a.has_key(id)
		flag_b = table_map_b.has_key(id)
		if True != flag_a or True != flag_b:
			continue
		
		data_a = table_map_a[id]
		data_b = table_map_b[id]
		
		t_a_1 = data_a["BaseAttrType1"]
		t_a_2 = data_a["BaseAttrType2"]
		t_a_3 = data_a["BaseAttrType3"]
		t_a_4 = data_a["BaseAttrType4"]
		
		t_b_1 = data_b["BaseAttrType1"]
		t_b_2 = data_b["BaseAttrType2"]
		t_b_3 = data_b["BaseAttrType3"]
		t_b_4 = data_b["BaseAttrType4"]
		
		if	t_a_1 == t_b_1 and \
			t_a_2 == t_b_2 and \
			t_a_3 == t_b_3 and \
			t_a_4 == t_b_4:
			continue
		msg = "EquitCheck [%d] BaseAttrTypeNotMatch"
		log_msg = msg %(int(id))
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "ArtifactAttrTips"
		error_msg["id"] = "unknow"
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		is_check_ok = False
	
	for id in deal_equip_ids:
		flag_a = table_map_a.has_key(id)
		flag_b = table_map_b.has_key(id)
		if True != flag_a or True != flag_b:
			continue
			
		data_a = table_map_a[id]
		data_b = table_map_b[id]
		
		t_a_1 = data_a["BaseAttrValueMin1"]
		t_a_2 = data_a["BaseAttrValueMin2"]
		t_a_3 = data_a["BaseAttrValueMin3"]
		t_a_4 = data_a["BaseAttrValueMin4"]
		t_a_5 = data_a["BaseAttrValueMax1"]
		t_a_6 = data_a["BaseAttrValueMax2"]
		t_a_7 = data_a["BaseAttrValueMax3"]
		t_a_8 = data_a["BaseAttrValueMax4"]
		
		t_b_1 = data_b["BaseAttrValueMin1"]
		t_b_2 = data_b["BaseAttrValueMin2"]
		t_b_3 = data_b["BaseAttrValueMin3"]
		t_b_4 = data_b["BaseAttrValueMin4"]
		t_b_5 = data_b["BaseAttrValueMax1"]
		t_b_6 = data_b["BaseAttrValueMax2"]
		t_b_7 = data_b["BaseAttrValueMax3"]
		t_b_8 = data_b["BaseAttrValueMax4"]
		
		if	t_a_1 == t_b_1 and \
			t_a_2 == t_b_2 and \
			t_a_3 == t_b_3 and \
			t_a_4 == t_b_4 and \
			t_a_5 == t_b_5 and \
			t_a_6 == t_b_6 and \
			t_a_7 == t_b_7 and \
			t_a_8 == t_b_8:
			continue


		errorMsg =""
		if t_a_1 !=t_b_1:
			errorMsg ="BaseAttrValueMin1 " +t_a_1 +" NotEqual " +t_b_1
		if t_a_2 !=t_b_2:
			errorMsg ="BaseAttrValueMin2 " +t_a_2 +" NotEqual " +t_b_2
		if t_a_3 !=t_b_3:
			errorMsg ="BaseAttrValueMin3 " +t_a_3 +" NotEqual " +t_b_3
		if t_a_4 !=t_b_4:
			errorMsg ="BaseAttrValueMin4 " +t_a_4 +" NotEqual " +t_b_4
		if t_a_5 !=t_b_5:
			errorMsg ="BaseAttrValueMax1 " +t_a_5 +" NotEqual " +t_b_5					
		if t_a_6 !=t_b_6:
			errorMsg ="BaseAttrValueMax2 " +t_a_6 +" NotEqual " +t_b_6	
		if t_a_7 !=t_b_7:
			errorMsg ="BaseAttrValueMax3 " +t_a_7 +" NotEqual " +t_b_7	
		if t_a_8 !=t_b_8:
			errorMsg ="BaseAttrValueMax4 " +t_a_8 +" NotEqual " +t_b_8	

		if errorMsg == "":
			continue


		msg = "EquitCheck [%d] table ArtifactAttrTips.txt and  EquipAttr.txt Have Same Column But Value Not Match [%s]"
		log_msg = msg %(int(id),errorMsg)
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "ArtifactAttrTips"
		error_msg["id"] = "unknow"
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		is_check_ok = False
	if is_check_ok == True:
		msg = "[OK] check equip base attr"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check equip base attr")

def fun_static_equip_attr(equip_id, col_name, limit_col):
	equip_line = _g_table_data["EquipAttr"]["data"][int(equip_id)]
	attr_type_limit = int(equip_line[limit_col])
	group_id = int(equip_line[col_name])
	if group_id < 0:
		return []
	tab_map_group = _g_table_data["EquipAffixGroup"]["data"]
	flag = tab_map_group.has_key(group_id)
	if True != flag:
		msg = "EquitCheck [%d] NotFindEquipAffixGroup"
		log_msg = msg %(int(equip_id))
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "EquipAffixGroup"
		error_msg["id"] = group_id
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		return []
	tab_map_attr = _g_table_data["EquipRandomAffix"]["data"]
	group_line = tab_map_group[group_id]
	ret_type_array = []
	for i in range(1,41):
		set_id = int(group_line["AffixSetID%d" %(i)])
		if set_id <= 0:
			continue
		flag = tab_map_attr.has_key(set_id)
		if True != flag:
			msg = "EquitCheck [%d] NotFindEquipRandomAffix"
			log_msg = msg %(int(equip_id))
		
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "EquipRandomAffix"
			error_msg["id"] = set_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
		#固定属性取第一条即可
		type_id = int(tab_map_attr[set_id]["AffixType1"])
		if type_id < 0:
			msg = "EquitCheck [%d] AffixType1 Is Error"
			log_msg = msg %(int(equip_id))
		
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "EquipRandomAffix"
			error_msg["id"] = set_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			continue
		ret_type_array.append(type_id)
	if len(ret_type_array) > attr_type_limit:
		msg = "EquitCheck [%d] AttrOverLimit Col(%s)"
		log_msg = msg %(int(equip_id), col_name)
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "EquipAttr"
		error_msg["id"] = equip_id
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		return []
	return ret_type_array

def fun_parse_equip_attrval_rate(equip_id):
	equip_line = _g_table_data["EquipAttr"]["data"][int(equip_id)]
	weight_id = int(equip_line["RandWeightId"])
	line = _g_table_data["EquipRandWeight"]["data"][weight_id]
	for i in range(1,101):
		flag = int(line["Percent%d" %(i)])
		if flag <= 0:
			continue
		return i / 100.0
	return 1

def fun_static_equip_value(equip_id):
	equip_line = _g_table_data["EquipAttr"]["data"][int(equip_id)]
	attr = _g_table_data["EquipAttrValue"]["data"]
	equip_att_val_id = int(equip_line["ValueLevel"])
	flag = attr.has_key(equip_att_val_id)
	if True != flag:
		msg = "EquitCheck [%d] EquipAttr.txt Column ValueLevel " + str(equip_att_val_id) + " Not Find In Table EquipAttrValue.txt Id Column"
		log_msg = msg %(int(equip_id))
		
		error_msg = {}
		error_msg["type"] = "error"
		error_msg["file"] = "EquipAttrValue"
		error_msg["id"] = equip_att_val_id
		error_msg["msg"] = log_msg
		_g_error_msg_total.append(error_msg)
		return {}
	rate = fun_parse_equip_attrval_rate(equip_id)
	tab_attr_line = attr[equip_att_val_id]
	ret_attr_val = {}
	for i in range(1,103):
		key = "AttrType%d" %(i)
		base_val = int(tab_attr_line[key])
		ret_attr_val[i - 1] = int(rate * base_val)
	return ret_attr_val

def fun_parse_equip_attr_tips_info(equip_id):
	tip_tab_map = _g_table_data["ArtifactAttrTips"]["data"]
	table_line = tip_tab_map[equip_id]
	ret_type = []
	ret_type_val_map = {}
	for i in range(1,11):
		val_min = int(table_line["AddAttrValueMin%d" %(i)])
		val_max = int(table_line["AddAttrValueMax%d" %(i)])
		type = int(table_line["AddAttrType%d" %(i)])
		if type < 0:
			continue
		if val_min != val_max:
			msg = "EquitCheck [%d] AttrMinNotEqualMax"
			log_msg = msg %(int(equip_id))
		
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "ArtifactAttrTips"
			error_msg["id"] = equip_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			return False
		ret_type.append(type)
		flag = ret_type_val_map.has_key(type)
		if True == flag:
			val_old = ret_type_val_map[type]
			if val_old == val_min:
				continue
			msg = "EquitCheck [%d] AttrValueError"
			log_msg = msg %(int(equip_id))
		
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "ArtifactAttrTips"
			error_msg["id"] = equip_id
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			return False
		ret_type_val_map[type] = val_min
	ret_info = {}
	ret_info["value"] = ret_type_val_map
	ret_info["type"] = sorted(ret_type)
	return ret_info
	
def fun_check_sequip_attr_add():
	is_check_ok = True
	table_map_a = _g_table_data["ArtifactAttrTips"]["data"]
	table_map_b = _g_table_data["EquipAttr"]["data"]
	deal_equip_ids = fun_parse_sequip_check_ids()
	total_is_check_ok = True
	for id in deal_equip_ids:
		flag_a = table_map_a.has_key(id)
		flag_b = table_map_b.has_key(id)
		if True != flag_a or True != flag_b:
			continue
		info_b = fun_parse_equip_attr_tips_info(id)
		if False == info_b:
			continue
		type_a = []
		debugAffixInfo =""
		equip_line = _g_table_data["EquipAttr"]["data"][int(id)]
		type_1 = fun_static_equip_attr(id,	\
			"BaseAffixGroupID",				\
			"BaseAdditionalAttrNum")
		if len(type_1) > 0:
			type_a.extend(type_1)
			group_id = int(equip_line["BaseAffixGroupID"])
			debugAffixInfo = "BaseAffixGroupID " + str(group_id) +" Add Affix Type Count:" + str(len(type_1))
		
		type_2 = fun_static_equip_attr(id,	\
			"ExAffixGroupID1",				\
			"ExAdditionalAttrNum1")
		if len(type_2) > 0:
			type_a.extend(type_2)
			group_id = int(equip_line["ExAffixGroupID1"])
			debugAffixInfo += "ExAffixGroupID1 " +str(group_id) + "Add Affix Type Count:" + str(len(type_2))
		
		type_3 = fun_static_equip_attr(id,	\
			"ExAffixGroupID2",				\
			"ExAdditionalAttrNum2")
		if len(type_3) > 0:
			type_a.extend(type_3)
			group_id = int(equip_line["ExAffixGroupID2"])
			debugAffixInfo += "ExAffixGroupID2 " +str(group_id) + "Add Affix Type Count:" + str(len(type_3))
		
		#type_b  ArtifactAttrTips AddAttrType[column] 一共配置了多少有效数值 
		type_b  = info_b["type"]

		#value_b  ArtifactAttrTips.txt 表中 AddAttrType[column] 每个type 以及对应的最小值 AddAttrValueMin[1-N] 的字典 
		value_b = info_b["value"]
		type_a  = sorted(type_a)
		
		# EquipAttrValue 表里结合概率表 EquipRandWeight 拿到的属性
		value_a = fun_static_equip_value(id)
		

		equip_line = _g_table_data["EquipAttr"]["data"][int(id)]
		equip_att_val_id = int(equip_line["ValueLevel"])

		is_check_ok = True
		debug_msg = ""
		while True:
			if len(type_a) != len(type_b):
				debug_msg = "ArtifactAttrTips column AddAttrType[1-N] AttrType Count " + str(len(type_b))  +" Not Equal EquipAttr.txt RandomAffix Total Count " + str(len(type_a)) +" " +debugAffixInfo
				is_check_ok = False
				break
			for i in range(0, len(type_a)):
				t_a = type_a[i]
				t_b = type_b[i]
				if t_a != t_b:
					debug_msg = "AttrTypeNotMatch  EquipAttr.txt RandomAffix AttrType Have AttrType:" +str(t_a) +" Not AddAttrType[1-N]"
					is_check_ok = False
					break
			for key in value_b.keys():
				flag = value_a.has_key(key)
				if True != flag:
					debug_msg = "EquipAttrValue.txt Config AttrType[1-N] Doesn't Contains ArtifactAttrTips.txt  AddAttrType[column] config AttrType " +str(key)
					is_check_ok = False
					break
				t_b = value_b[key]
				t_a = value_a[key]
				if t_b != t_a:
					attrTipErrorMinAttrTypeColumn =""
					equipAttrColumName = "AttrType" + str(int(key) +1)
					tip_tab_map = _g_table_data["ArtifactAttrTips"]["data"]
					table_line = tip_tab_map[id]
					for i in range(1,11):
						val_min = int(table_line["AddAttrValueMin%d" %(i)])
						attrType = int(table_line["AddAttrType%d" %(i)])
						if val_min == t_b and attrType==int(key):
							attrTipErrorMinAttrTypeColumn = "AddAttrValueMin%d" %(i)
							break


					aricraftTip =" EquipAttrValue.txt id:" +str(id) +" Column:" +attrTipErrorMinAttrTypeColumn
					valueNotMatchTip = " EquipAttrValue.txt value:" +str(t_a) +" ArtifactAttrTips.txt value:" +str(t_b)
					debug_msg = "EquipAttrValue.txt and ArtifactAttrTips.txt AttrValNotMatch "  + " EquipAttrValue.txt id:" +str(equip_att_val_id) + " ColumnName:" +equipAttrColumName + aricraftTip +valueNotMatchTip
					is_check_ok = False
					break
			break
		if True != is_check_ok:
			msg = "EquitCheck [%d] AddAttrNotMatch(%s)"
			log_msg = msg %(int(id), debug_msg)
		
			error_msg = {}
			error_msg["type"] = "error"
			error_msg["file"] = "unknow"
			error_msg["id"] = 0
			error_msg["msg"] = log_msg
			_g_error_msg_total.append(error_msg)
			total_is_check_ok = False
	if total_is_check_ok == True:
		msg = "[OK] check equip add attr"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check equip add attr")

def fun_check_fashion_isshow_time():
	#FashionData显示时间检查
	the_check_data_list = _g_table_data["FashionDisplay"]["data"]
	key_id_list = the_check_data_list.keys()
	line_num = len(key_id_list)
	line_idx = 0
	is_check_ok = True
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		the_check_id = key_id_list[now_idx]
		check_line = the_check_data_list[the_check_id]
		check_update_time_str = check_line["IsShow"].replace("*", "")
		
		if check_update_time_str != "1" and int(check_update_time_str) > 0:
			try:
				check_update_time = time.strptime(check_update_time_str, "%Y%m%d%H%M%S")
			except:
				clr.print_red_text("[FAILED] check file[FashionDisplay] " + check_update_time_str)
				is_check_ok = False
			  		
	if is_check_ok == True:
		msg = "[OK] check file[FashionDisplay]"
		clr.print_green_text(msg)
	else:
		clr.print_red_text("[FAILED] check file[FashionDisplay]")


def fun_check_servantdraw_recommend():
	is_check_ok = True
	table_servantDrawSet = _g_table_data["ServantDrawSet"]["data"]
	table_servantdrawRecommend = _g_table_data["ServantDrawRecommend"]["data"]
	#table_commonItem = _g_table_data["CommonItem"]["data"]
	table_usableItem = _g_table_data["UsableItem"]["data"]


	tab_servantdraw_rec_key_id_list = table_servantdrawRecommend.keys()
	line_num = len(tab_servantdraw_rec_key_id_list)
	line_idx = 0
	#所有推荐的英魂列表
	allRecServants = []
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		the_check_id = tab_servantdraw_rec_key_id_list[now_idx]
		currentLine = table_servantdrawRecommend[the_check_id]
		for i in range(1,9):
			columnName = "Servant"+str(i)
			servantIdStr =currentLine[columnName]
			if servantIdStr!="-1" and int(servantIdStr) >0:
				allRecServants.append(servantIdStr)


	allNeedRecItemServant =[]
	line_idx = 0
	table_servantDrawSet_key_id_list = table_servantDrawSet.keys()
	line_num = len(table_servantDrawSet_key_id_list)
	while line_idx < line_num:
		now_idx = line_idx
		line_idx += 1
		the_check_id = table_servantDrawSet_key_id_list[now_idx]
		currentLine = table_servantDrawSet[the_check_id]
		collection = currentLine["BelongCollection"]
		itemId = currentLine["ItemId"]
		if collection == "1" or collection =="2" :
			tab_UseableData = table_usableItem[int(itemId)]
			useableServant =  tab_UseableData["UseParamA"]
			allNeedRecItemServant.append(useableServant)
			if not useableServant in allRecServants:
				errMsg = "servantdraw rec error,not show in ServantDrawRecommend.txt itemid:" +itemId  +" servantId:" +useableServant
				clr.print_red_text(errMsg)
				error_msg = {}
				error_msg["type"] = "error"
				error_msg["file"] = "ServantDrawRecommend"
				error_msg["id"] = the_check_id
				error_msg["msg"] = errMsg
				_g_error_msg_total.append(error_msg)

	



if __name__ == '__main__':
	clr.print_green_text("============")
	fun_do_parse_server_txt_file("..\\..\\PublicTables")
	fun_do_parse_server_txt_file("..\\..\\ServerTables")
	fun_do_parse_client_txt_file("..\\..\\ClientTables")
	fun_print_error_files()
	clr.print_green_text("============")
	fun_check_table_depend()
	clr.print_green_text("============")
	fun_check_sequip_ids()
	fun_check_sequip_attr_base()
	fun_check_sequip_attr_add()
	clr.print_green_text("============")
	clr.print_green_text("============")
	fun_check_special_symble()
	fun_check_id_must_inc()
	fun_check_id_must_auto_inc()
	fun_check_idip_white_item()
	fun_check_dlc_update_time()
	fun_check_fashion_isshow_time()
	fun_check_servantdraw_recommend()
	
	err_num = len(_g_error_msg_total)
	if err_num <= 0:
		clr.print_green_text("congratulate no error!!!")
		sys.exit()
	
	log_path = "table_check.log"
	clr.print_red_text("error loged in %s" %(log_path))
	
	file_obj = open("..\\..\\" + log_path, "w")
	err_idx = 0
	while err_idx < err_num:
		now_idx = err_idx
		err_idx += 1

		info = _g_error_msg_total[now_idx]
		file_name = fun_parse_file_name(info["file"])
		if now_idx == 0:
			file_obj.write("detail info:\n")

		file_obj.write("\n[no_%s]:\n" %(err_idx))
		file_obj.write("type[%s]\n" %(info["type"]))
		file_obj.write("file[%s]\n" %(file_name))
		file_obj.write("id[%s]\n" %(info["id"]))
		file_obj.write("msg: %s\n" %(info["msg"]))
	file_obj.close()
	clr.print_green_text("============================================")
