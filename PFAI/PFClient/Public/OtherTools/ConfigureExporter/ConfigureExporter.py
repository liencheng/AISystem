#!/bin/python
# -*- coding=utf-8 *-*

from colorama import init,Fore
from chardet.universaldetector import UniversalDetector
import numpy as np
import chardet
import csv
import codecs
import sys
import os
import re
import pandas as pd
import xlrd
import configparser
import tkinter as tk
from tkinter import ttk

_g_error_msg_total = []

class ConfigWnd:
	def on_combobox_select(self,event):
		selected_value = self.combo.get() # 获取所选项的值
		print("Selected value:", selected_value)
	
	def on_button(self):
		selected = self.combo.get() #获取选中项的值
		print(f"选中项：{selected}")
		
		self.root.destroy() #关闭窗口
		RunConfigExporter(selected)

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("配置表导出")

		# 设置窗口大小为500x300像素
		self.root.geometry("330x130+800+300")

		self.label = ttk.Label(self.root,text="请选择要操作的导出表");
		self.label.place(x=10,y=20)
		
		# 创建一个ConfigParser对象
		config = configparser.ConfigParser()
		# 读取ini文件内容
		config.read('Config.ini')
		files = config.items("Files")

		self.combo = ttk.Combobox(self.root)
		comboValues = []
		for file in files:
			print(f"******filename: " + file[1])
			comboValues.append(file[1])
		self.combo["values"] = comboValues
		self.combo.place(x=150,y=20)
		self.combo.current(0)
		self.combo.bind("<<ComboboxSelected>>", self.on_combobox_select)

		self.btn = tk.Button(self.root, text="确定", command=self.on_button)
		self.btn.config(width=10,height=2);
		self.btn.place(x=125,y=55)

		self.root.mainloop()

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

def Fun_Parse_Sheet_name(file_path):
	file_path_list = file_path.replace("\\","/").split("/")
	idx = len(file_path_list) - 1
	return file_path_list[idx].split(".")[0]

def ConfigureExporter(selectFile):
	detector = UniversalDetector()
	clr.print_green_text("----------selectFile: " + selectFile + "----------")
	dfs = pd.read_excel(selectFile,sheet_name=None)
	for tableName in dfs:
		if tableName == '配置总览':
			continue

		print(tableName)
		changeLineInfos = []
		for line in dfs[tableName].values:
			if (isinstance(line[0],int)):
				#将nan替换为空字符
				for i,item in enumerate(line):
					if pd.isna(item):
						line[i] = ''
				strContent = np.array2string(line)
				strContent = strContent[1:len(strContent)-1]
				strContent = strContent.replace('\'','').replace(' ','	').replace('\n','')
				lineInfo = {}
				lineInfo["Id"] = int(line[0])
				lineInfo["Content"] = strContent
				#print(lineInfo["Content"])
				changeLineInfos.append(lineInfo)

		tablePath = ""
		clientPath = "..\..\ClientTables\%s.txt" %(tableName)
		publicPath = "..\..\PublicTables\%s.txt" %(tableName)
		serverPath = "..\..\ServerTables\%s.txt" %(tableName)
		if os.path.exists(clientPath):
			tablePath = clientPath
		elif os.path.exists(publicPath):
			tablePath = publicPath
		elif os.path.exists(serverPath):
			tablePath = serverPath

		if os.path.exists(tablePath):
			print(tablePath)
			detector.reset()
			try:
				f = open(tablePath, 'rb')
			except PermissionError:
				clr.print_red_text("文件%s已被打开,请关闭文件再执行此操作" %(tablePath))
				return
			#获取文件的编码格式，再通过编码的格式进行读取文件
			for line in f:
				detector.feed(line)
				if detector.done:
					break
			detector.close()

			#print("------------detect(data)--------")
			#print(detector.result)
			file_encoding = detector.result['encoding']
			if (file_encoding.find('GB') != -1):
				file_encoding = 'GBK'
			#elif (file_encoding.find('UTF') != -1):
			#	file_encoding = 'utf-8'

			try:
				f = open(tablePath, 'r', encoding=file_encoding, errors='ignore')
			except PermissionError:
				clr.print_red_text("文件%s已被打开,请关闭文件再执行此操作" %(tablePath))
				return

			csvReader = csv.reader(f)
			fileLineInfos = []
			index = 0
			for line in csvReader:
				strLine = ','.join(line)
				content = strLine[0:len(strLine)]
				lineDatas = content.split("\t")
				index = index + 1
				filelineInfo = {}
				if (index >= 4 and lineDatas[0].find('#') == -1):
					filelineInfo["Id"] = int(lineDatas[0])
				else:
					filelineInfo["Id"] = lineDatas[0]
				filelineInfo["Content"] = content
				fileLineInfos.append(filelineInfo)

			#遍历新增/修改的配置文本，和原始表格进行比对，有相同Id的进行覆盖，否则按Id顺序插入到原文本中
			print("---------------Update %s LineInfo Begin--------" %(tablePath))
			for changeLineInfo in changeLineInfos:
				preFileLineId = -1
				preLineIndex = 0
				lineIndex = 0
				for fileLineInfo in fileLineInfos:
					if (isinstance(fileLineInfo["Id"],int)):
						#print("------changeLineId:%s, fileLineId:%s" %(changeLineInfo["Id"],fileLineInfo["Id"]))
						if changeLineInfo["Id"] == fileLineInfo["Id"]:
							fileLineInfo["Content"] = changeLineInfo["Content"]
							print("Replace Id:%s" %(changeLineInfo["Id"]))
							break
						else:
							if fileLineInfo["Id"] > changeLineInfo["Id"] and preFileLineId < changeLineInfo["Id"]:
								#检查后面是否有相同Id的配置，如果没有则插入
								isHaveThisId = False
								for i in range(lineIndex+1,len(fileLineInfos)):
									if fileLineInfos[i]["Id"] == changeLineInfo["Id"]:
										isHaveThisId = True
										break;
								if (isHaveThisId == False):
									fileLineInfos.insert(preLineIndex+1, changeLineInfo)
									print("Insert new line:%s" %(changeLineInfo["Content"]))
									break
						preFileLineId = fileLineInfo["Id"]
						preLineIndex = lineIndex
					lineIndex = lineIndex + 1
				if (lineIndex == len(fileLineInfos)):
					#遍历到最后没找到合适的位置，说明是新的更大的Id，直接加到最后即可
					fileLineInfos.insert(preLineIndex+1, changeLineInfo)
					print("Add new line:%s" %(changeLineInfo["Content"]))

			print("---------------Update %s LineInfo End--------" %(tablePath))
			print("--------fileLineInfos Count:%s" %(len(fileLineInfos)))

			#将更新后的内容写入原始表格文件
			try:
				f = open(tablePath, 'w+', encoding=file_encoding, errors='ignore')
			except PermissionError:
				clr.print_red_text("文件%s已被打开,请关闭文件再执行此操作" %(tablePath))
				return

			print("---------------Write %s Begin--------" %(tablePath))
			for fileLineInfo in fileLineInfos:
				#print(fileLineInfo["Content"])
				f.writelines(fileLineInfo["Content"] + "\n")
			f.close()
			print("---------------Write %s End--------" %(tablePath))

def RunConfigExporter(selectFile):
	clr.print_green_text("============================================")
	ConfigureExporter(selectFile)

	err_num = len(_g_error_msg_total)
	if err_num <= 0:
		clr.print_green_text("============================================")
		sys.exit()
	
	log_path = "ConfigureExporter.log"
	clr.print_red_text("error loged in %s" %(log_path))
	
	file_obj = open("..\\..\\" + log_path, "w")
	err_idx = 0
	while err_idx < err_num:
		now_idx = err_idx
		err_idx += 1

		info = _g_error_msg_total[now_idx]
		sheet_name = Fun_Parse_Sheet_name(info["sheet"])
		if now_idx == 0:
			file_obj.write("detail info:\n")

		file_obj.write("\n[no_%s]:\n" %(err_idx))
		file_obj.write("type[%s]\n" %(info["type"]))
		file_obj.write("sheet[%s]\n" %(sheet_name))
		file_obj.write("row[%s]\n" %(info["row"]))
		file_obj.write("msg: %s\n" %(info["msg"]))
	file_obj.close()
	clr.print_green_text("============================================")

if __name__ == '__main__':
	configWnd = ConfigWnd()
	