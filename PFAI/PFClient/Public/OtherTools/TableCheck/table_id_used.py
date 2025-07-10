#!/bin/python


from colorama import init, Fore
from datetime import datetime
import time
import codecs
import sys
import os
import re
import struct
import codecs
from operator import attrgetter
import configparser


_g_table_id_range_used = []
_g_id_used_whitelist = []
_g_id_used_output_path = "..\\..\\table_id_used.log"
_g_id_used_warn_factor = 0.8
_g_show_top_warn = 10
_g_both_warn = []
_g_id_warn = []
_g_record_warn = []
_g_white_list = []
_g_common_left = []

_g_fmt_title = "{:>6} {:>10} {:>8} {:>20} {:>10} {:>10} {:>10} {:>10}"
_g_fmt =       "{:>8}{:>10.2f}{:>10.2f}{:>40}.txt{:>10}{:>10}{:>10}{:>10}"

_g_file_fmt_title = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"
_g_file_fmt = "{}\t{:.2f}\t{:.2f}\t{}.txt\t{}\t{}\t{}\t{}"


class Color:
    def print_warn_text(self, print_text):
        print(Fore.MAGENTA + print_text)

    def print_red_text(self, print_text):
        print(Fore.RED + print_text)

    def print_green_text(self, print_text):
        print(Fore.GREEN + print_text)

    def print_blue_text(self, print_text):
        print(Fore.BLUE + print_text)

    def print_yellow_text(self, print_text):
        print(Fore.LIGHTYELLOW_EX + print_text)

    def print_red_str(self, print_text):
        print(Fore.RED + print_text, end="")

    def print_green_str(self, print_text):
        print(Fore.GREEN + print_text, end="")

    def print_blue_str(self, print_text):
        print(Fore.BLUE + print_text, end="")

    def print_yellow_str(self, print_text):
        print(Fore.LIGHTYELLOW_EX + print_text, end="")

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
        if type != ".txt":
            continue

        out_file_list.append(tmp_path_name)
    return out_file_list


def fun_parse_line(key, line_data):
    # MAX_ID=99999;MAX_RECORD=10241;TableType=Hash;
    line_list = re.split("#|=|;", line_data)
    line_num = len(line_list)
    line_idx = 0
    while line_idx < line_num:
        tmp_key = line_list[line_idx]
        line_idx += 1
        if tmp_key == key:
            return line_list[line_idx]
    return ""


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
    file_path_list = file_path.replace("\\", "/").split("/")
    idx = len(file_path_list) - 1
    return file_path_list[idx].split(".")[0]


def fun_parse_server_txt(file_path):
    #clr.print_green_text("parse file[%s]" % (file_path))

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
            # 列名字
            temp = line_data.split('\t')
            list_file_header_info["name"] = temp
            continue

        if now_idx == 1:
            # 类型说明
            temp = line_data.split('\t')
            for type_it in temp:
                if "" != type_it.strip(' '):
                    continue
            list_file_header_info["type"] = temp
            continue

        if now_idx == 2:
            # 忽略列说明
            temp = line_data.split('\t')
            list_file_header_info["ign"] = temp

            # 最大项说明
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

        if line_data[0] == '#':
            continue

        line_temp = line_data.split('\t')
        num_col = len(line_temp)
        if num_col <= 0:
            continue

        # 计算最大ID和记录数
        line_map = fun_make_file_data_map(
            list_file_header_info,
            line_temp)
        line_id = int(line_temp[0])

        # 最后一列不允许为空
        if line_temp[num_col - 1] == "":
            continue

        list_file_data[line_id] = line_map
        list_table_id.append(line_id)
        max_record_calc += 1

        if line_id > max_id_calc:
            max_id_calc = line_id
        continue

    file_short_name = fun_parse_file_name(file_path)
    range_used = {"FILE": file_path, "SIMPLE_PATH": file_short_name,
                  "MAX_ID": max_id_std, "MAX_RECORD": max_record_std,
                  "CUR_MAX_ID": max_id_calc, "CUR_RECORD": max_record_calc,
                  "ID_FACTOR": round((float(max_id_calc) / max_id_std), 2),
                  "RECORD_FACTOR": round((float(max_record_calc) / max_record_std), 2)}
    _g_table_id_range_used.append(range_used)


def fun_do_parse_server_txt_file(the_file_dir):
    file_list = fun_parse_all_txt_files(the_file_dir)
    file_num = len(file_list)
    if file_num <= 0:
        return True

    deal_idx = 0
    dur = 0
    start = time.process_time()
    while deal_idx < file_num:
        file_path = file_list[deal_idx]
        deal_idx += 1
        fun_parse_server_txt(file_path)
        dur = time.process_time() - start
        print("\r{}".format(" "*100)+"\r{:>3.0f}%[{:50}]{:2.2f}s".format(float(deal_idx)/file_num*100, file_path,  dur), end="\r")
        time.sleep(0)

    print("\r{}".format(" "*100)+"\r{:>3.0f}%[{:^50}]{:2.2f}s".format(float(deal_idx) / file_num * 100, (str(file_num))+" files parsed", dur), end="\n")


def fun_sort_table_range_used_and_show_top():
    fun_parse_id_used_range()
    warn_both_len = len(_g_both_warn)
    warn_id_len = len(_g_id_warn)
    warn_record_len = len(_g_record_warn)

    print(fun_format_used_head_str(_g_fmt_title))
    for i in range(warn_both_len):
        line_str = fun_format_one_used_data_str(_g_fmt, "[Both]", _g_both_warn[i])
        clr.print_red_text(line_str)

    for i in range(warn_record_len):
        line_str = fun_format_one_used_data_str(_g_fmt, "[Record]", _g_record_warn[i])
        clr.print_red_text(line_str)

    for i in range(warn_id_len):
        line_str = fun_format_one_used_data_str(_g_fmt, "[Id]", _g_id_warn[i])
        clr.print_red_text(line_str)

    return warn_both_len + warn_id_len + warn_record_len


def fun_parse_id_used_range():
    global _g_both_warn
    global _g_id_warn
    global _g_record_warn
    global _g_white_list
    global _g_common_left

    for data in _g_table_id_range_used:
        if data["SIMPLE_PATH"] in _g_id_used_whitelist:
            _g_white_list.append(data)
            continue
        if data["ID_FACTOR"] >= _g_id_used_warn_factor and data["RECORD_FACTOR"] >= _g_id_used_warn_factor:
            _g_both_warn.append(data)
        elif data["ID_FACTOR"] >= _g_id_used_warn_factor:
            _g_id_warn.append(data)
        elif data["RECORD_FACTOR"] >= _g_id_used_warn_factor:
            _g_record_warn.append(data)
        else:
            _g_common_left.append(data)
    return len(_g_both_warn) + len(_g_record_warn) + len(_g_id_warn)


def fun_log_table_range_used():
    log_path = _g_id_used_output_path
    file_obj = open(log_path, "w")
    head_str = fun_format_used_head_str(_g_file_fmt_title)
    file_obj.write(head_str+"\n")

    fun_write_one_used_warning_list(_g_file_fmt, "[both]", _g_both_warn, file_obj)
    fun_write_one_used_warning_list(_g_file_fmt, "[record]", _g_record_warn, file_obj)
    fun_write_one_used_warning_list(_g_file_fmt, "[id]", _g_id_warn, file_obj)
    fun_write_one_used_warning_list(_g_file_fmt, "[white_list]", _g_white_list, file_obj)
    fun_write_one_used_warning_list(_g_file_fmt, "[common_left]", _g_common_left, file_obj)

    file_obj.close()


def fun_format_used_head_str(fmt):
    line_str = fmt.format("告警类型", "ID百分比", "Record百分比", "配置文件", "当前使用最大ID", "MAX_ID", "当前配置条数", "MAX_RECORD")
    return line_str


def fun_format_one_used_data_str(fmt, line_prefix, data_dict):
    line_str = fmt.format(line_prefix, (data_dict["ID_FACTOR"] * 100), (data_dict["RECORD_FACTOR"] * 100),
                data_dict["SIMPLE_PATH"], data_dict["CUR_MAX_ID"], data_dict["MAX_ID"], data_dict["CUR_RECORD"], data_dict["MAX_RECORD"])
    return line_str


def fun_write_one_used_warning_list(fmt, line_prefix, data_list, file_obj):
    for data in data_list:
        line = fun_format_one_used_data_str(fmt, line_prefix, data)
        file_obj.write(line+"\n")


def fun_do_parse_id_check_white_file():
    the_special_symble_file = codecs.open("./table_id_used_config.ini", "rb", 'utf-16-le')
    total_lines = the_special_symble_file.read()
    the_special_symble_file.close()

    ret_data_info = []
    key_flag = False
    for raw_line in total_lines:
        line = raw_line.strip(' ').strip('\r').strip('\n')
        if len(line) <= 0 or True == line.startswith("#"):
            continue

        if line.startswith("[id_used_check_whitelist]"):
            key_flag = True
            continue

        if key_flag and line.startswith("["):
            break

        if True != key_flag:
            continue
        ret_data_info.append(line)

    global _g_id_used_whitelist
    _g_id_used_whitelist = ret_data_info
    print("WhiteList:", _g_id_used_whitelist)


def fun_do_parse_id_used_check_param_config():
    the_special_symble_file = codecs.open("./table_id_used_config.ini", "rb", 'utf-16-le')
    total_lines = the_special_symble_file.read()
    the_special_symble_file.close()

    ret_data_info = {}
    key_flag = False
    for raw_line in total_lines:
        line = raw_line.strip(' ').strip('\r').strip('\n')
        if len(line) <= 0 or True == line.startswith("#"):
            continue

        if line.startswith("[id_used_check_param]"):
            key_flag = True
            continue

        if key_flag and line.startswith("["):
            break

        if True != key_flag:
            continue

        t_data = line.split("#")
        if 2 != len(t_data):
            continue
        ret_data_info[t_data[0]] = t_data[1]

    if "WarningFactor" in ret_data_info:
        print("WarningFactor:"+ret_data_info["WarningFactor"])
        global _g_id_used_warn_factor
        _g_id_used_warn_factor = float(ret_data_info["WarningFactor"])

    if "Output" in ret_data_info:
        print("Output:"+ret_data_info["Output"])
        global _g_id_used_output_path
        _g_id_used_output_path = ret_data_info["Output"]

    # if ret_data_info.has_key("ShowTopWarn"):
    #     print "ShowTopWarn"+ret_data_info["ShowTopWarn"]
    #     global _g_show_top_warn
    #     _g_show_top_warn = int(ret_data_info["ShowTopWarn"])
    #     print "_g_show_top_warn ", _g_show_top_warn
    return ret_data_info


if __name__ == '__main__':
    # read config
    print("ConfigFile:", "./Public/OtherTools/TableCheck/table_id_used_config.ini")
    fun_do_parse_id_check_white_file()
    fun_do_parse_id_used_check_param_config()
    # config used
    # print _g_show_top_warn
    # print _g_id_used_warn_factor
    # print _g_id_used_output_path
    clr.print_green_text("parse table files")
    clr.print_green_text("============")
    print("PublicTables")
    fun_do_parse_server_txt_file("..\\..\\PublicTables")
    print()
    clr.print_green_text("============")
    print("ServerTables")
    fun_do_parse_server_txt_file("..\\..\\ServerTables")
    print()
    clr.print_green_text("============")
    clr.print_green_text("check id used :")
    print()
    count = fun_sort_table_range_used_and_show_top()
    if count == 0:
        clr.print_green_text("[OK] id range used well !!!")
        print("more id range used info see %s" % _g_id_used_output_path)
        clr.print_green_text("check id range used end success.")
        clr.print_green_text("============")
    else:
        print()
        count_warn_str = "[WARN] %d files id used exceed %.2f%% without whitelist!!!" % (count, (round(_g_id_used_warn_factor,2)*100))
        clr.print_red_text(count_warn_str)
        print("more id used info see %s" % _g_id_used_output_path)
        clr.print_red_text("Id used check quit with warning.")
    fun_log_table_range_used()
    sys.exit()
