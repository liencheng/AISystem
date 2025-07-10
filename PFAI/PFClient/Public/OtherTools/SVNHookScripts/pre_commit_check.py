# -*- coding: utf-8 -*-
import sys
import os
import re
import subprocess

#记录所有新增的文件名
g_AllAddFiles = []
g_AllAddMateFiles = []

#记录所有的报错信息
g_ErrList = []

#记录日志用的文件对象
g_LogFile = None
g_IsDebug = True

def main(argv):
	# 从参数中取出来代码库和事务信息
	repos = argv[0]
	txn = argv[1]
	depth = argv[2]
	someArg = argv[3]

	g_LogFile = open("Debug.log", "w")
	WriteLog(g_LogFile, repos, "Debug")
	WriteLog(g_LogFile, txn, "Debug")
	WriteLog(g_LogFile, depth, "Debug")
	WriteLog(g_LogFile, someArg, "Debug")

	#sys.exit(1)
	#return

	#遍历本次提交的所有文件，分别通过svn diff取到本次提交所有的修改
	changedFiles = open(repos, "r").readlines()
	WriteLog(g_LogFile, "changedFile:" + str(len(changedFiles)), "Debug");
	for file in changedFiles:
		WriteLog(g_LogFile, "changedFile:" + file, "Debug")
		#output = os.popen("svn diff %s" % (file))
		#diffMessage = output.buffer.read().decode('GBK', errors='ignore')
		diffMessage = MyPopen("svn diff %s" % (file))
		WriteLog(g_LogFile, "svn diff return:" + str(diffMessage.encode('GBK')), "Debug")

		#文件名
		nameStartPos = file.rfind("/")
		fileName = file
		if nameStartPos != -1:
			fileName = file[nameStartPos+1:len(file)-1]


		#记录所有新增的文件名
		allAddFiles = {}
		allAddMateFiles = {}

		#收集所有“+XXX”开始的
		changedLines = {}
		index = 1
		diffMsgLines = diffMessage.split('\r\n')
		for changedLine in diffMsgLines:
			#changedLine = str(changedLine.encode('gb18030'))
			WriteLog(g_LogFile, "ChangedLine:" + changedLine, "Debug");
			isPlus = changedLine.find("+++ ") == 0
			isReduce = changedLine.find("--- ") == 0
			isNew = changedLine.rfind("(nonexistent)") != -1 and isReduce == True
			#记录所有新增的文件
			if isNew:
				fileNameBeginPos = changedLine.rfind("/");
				fileNameEndPos = changedLine.rfind(".");
				if fileNameBeginPos != -1 and fileNameBeginPos != len(changedLine)-1 and fileNameEndPos != -1 and fileNameEndPos != len(changedLine)-1:
					newFileName = changedLine[fileNameBeginPos+1:fileNameEndPos]
					WriteLog(g_LogFile, "  newFileName:" + newFileName, "Debug");
					#对于Client目录下的文件，检测是否meta文件
					if file.find("/Clinet/Assets/") != -1:
						metaPos = changedLine.rfind(".meta")
						if metaPos != -1 and metaPos != len(changedLine)-1:
							fileNameEndPos = changedLine[0:metaPos].rfind(".")
							newFileName = changedLine[fileNameBeginPos+1:fileNameEndPos]
							WriteLog(g_LogFile, "  metaFileName:" + newFileName, "Debug");
							g_AllAddMateFiles.append(newFileName)
						else:
							g_AllAddFiles.append(newFileName)
				
			#记录所有的修改内容（"+XXX"开始的）
			if isPlus == False:
				if len(changedLine) > 1:
					if changedLine[0] == '+' and changedLine[1] != '+':
						WriteLog(g_LogFile, "add changedLine:" + changedLine[1:len(changedLine)], "Debug")
						changedLines[index] = changedLine[1:len(changedLine)]
						index = index + 1

		#针对每一行修改的内容进行检测
		for index in changedLines:
			Check_MsgDefaultValue(fileName, changedLines[index], g_ErrList)
			Check_Chiness(fileName, changedLines[index], g_ErrList)
			Check_LuaIfZero(fileName, changedLines[index], g_ErrList)
			Check_IfSentence(fileName, changedLines[index], g_ErrList)

	#检测新增文件是否有对应Meta文件
	Check_NewMetaFile(g_ErrList)

	# 返回
	if len(g_ErrList) == 0:
		sys.stderr.write("居然执行成功了")
		g_LogFile.close()
		sys.exit(1)
		#sys.exit(0)
	else:
		# 输出返回信息
		for err in g_ErrList:
			sys.stderr.write(err)
			WriteLog(g_LogFile, "Pre_Commit Check Err:" + err, "Error")
		g_LogFile.close()
		sys.exit(1)

#######################
#写Log
#######################
def WriteLog(logFile, logInfo, logType):
	if g_IsDebug == False:
		if logType == "Debug" or logType == "Info" or logType == "Warning":
			return
	if logFile == None:
		return

	if logType == "Info":
		logInfo = "[Info]" + logInfo
	elif logType == "Warning":
		logInfo = "[Warning]" + logInfo
	elif logType == "Debug":
		logInfo = "[Debug]" + logInfo
	elif logType == "Error":
		logInfo = "[Error]" + logInfo

	logFile.write(logInfo + "\n")

#######################
#Msg的默认值检查
#######################
def Check_MsgDefaultValue(fileName,changedLine,errList):
	#文件名是否XXXMsg.h
	if fileName.rfind("Msg.h") == -1:
		return

	#只有int(int32_t、int64_t)、bool、time_t这些类型的变量需要赋初始值
	bRet = True
	if changedLine.find("int ") != -1 or changedLine.find("int32_t ") != -1 or changedLine.find("int64_t ") != -1:
		if changedLine.rfind("=") == -1:
			bRet = False
	if changedLine.find("bool ") != -1:
		if changedLine.rfind("=") == -1:
			bRet = False
	if changedLine.find("time_t ") != -1:
		if changedLine.rfind("=") == -1:
			bRet = False

	if bRet == False:
		errList.append("Msg基础类型变量未赋初始值，文件：" + fileName + " 内容：" + changedLine + "\n")

#######################
#检测新增文件是否同时提交了Meta文件
#######################
def Check_NewMetaFile(errList):
	for newFile in g_AllAddFiles:
		bFoundMeta = False
		for newMetaFile in g_AllAddMateFiles:
			if newFile == newMetaFile:
				bFoundMeta = True
				break
		if bFoundMeta == False:
			errList.append("新增文件未添加Meta文件，文件：" + newFile + "\n")


#######################
#代码内中文检测
#######################
def Check_Chiness(fileName, changedLine, errList):
	#只检测XXX.cs文件
	if fileName.rfind(".cs") == -1:
		return

	#排除注释
	isNotes = True
	notesPos = 0
	if changedLine.find("//") != -1 or changedLine.find("///") != -1:
		notesPos = changedLine.find("//")
		if notesPos != -1:
			for i in range(0, notesPos):
				if changedLine[i] != ' ':
					isNotes = False
					break;
			if isNotes == True:
				return
	if changedLine.find("/*") != -1:
		notesPos = changedLine.find("/*")
		if notesPos != -1:
			for i in range(0, notesPos):
				if changedLine[i] != ' ':
					isNotes = False
					break;
			if isNotes == True:
				return
	if changedLine.find("/*") == -1 and changedLine.find("*") != -1:
		notesPos = changedLine.find("*")
		if notesPos != -1:
			for i in range(0, notesPos):
				if changedLine[i] != ' ':
					isNotes = False
					break;
			if isNotes == True:
				return
	if changedLine.find("/*") == -1 and changedLine.find("*/") != -1:
		notesPos = changedLine.find("*/")
		if notesPos != -1:
			for i in range(0, notesPos):
				if changedLine[i] != ' ':
					isNotes = False
					break;
			if isNotes == True:
				return
	if changedLine.find("#") != -1:
		notesPos = changedLine.find("#")
		if notesPos != -1:
			for i in range(0, notesPos):
				if changedLine[i] != ' ':
					isNotes = False
					break;
			if isNotes == True:
				return

	#非纯注释行，取注释前面的部分			
	if isNotes == False:
		changedLine = changedLine[0:notesPos]

	#检查整个字符串是否包含中文
	bRet = True
	for i in range(0,len(changedLine)):
		if u'\u4e00' <= changedLine[i] <= u'\u9fff':
			if i > 0:
				if changedLine[i-1] == '\'' or changedLine[i-1] == '\"':
					bRet = False

	if bRet == False:
		errList.append("代码含有中文，文件：" + fileName + " 内容：" + changedLine + "\n")


#######################
#Lua文件if 0检测
#######################
def Check_LuaIfZero(fileName, changedLine, errList):
	#只检测XXX.lua文件
	if fileName.rfind(".lua") == -1:
		return

	#检测语句里是否有"if 0 then"
	if changedLine.find("if 0 then") != -1:
		errList.append("Lua脚本里有if 0语句，文件：" + fileName + " 内容：" + changedLine + "\n")

def MyPopen(cmd):
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.DEVNULL)
	return proc.stdout.read().decode('GBK', errors='ignore')

def Main():
	try:
		main(sys.argv[1:])
	except Exception as e:
		WriteLog(g_LogFile, "Exception:" + e, "Error")
		print(e)
		pass

#######################
#代码文件if ==误写成=检测
#######################
def Check_IfSentence(fileName, changedLine, errList):
	#只检测XXX.cs、XXX.h、XXX.cpp文件
	if fileName.rfind(".cs") == -1 and fileName.rfind(".h") == -1 and fileName.rfind(".cpp") == -1:
		return;

	#是否if语句
	if1BeginPos = changedLine.find("if(")
	if2BeginPos = changedLine.find("if (")
	if if1BeginPos != -1 or if2BeginPos != -1:
		ifBeginPos = if1BeginPos
		if if1BeginPos == -1:
			ifBeginPos = if2BeginPos
		ifEndPos = changedLine.find(")")

		#if()内语句内容
		ifContent = changedLine[ifBeginPos:ifEndPos]
		if ifEndPos == -1:
			ifContent = changedLine[ifBeginPos:len(changedLine)-1]
		if ifContent.find("==") == -1 and ifContent.find("=") != -1:
			errList.append("if语句==误写为=，文件：" + fileName + " 内容：" + changedLine + "\n")


if __name__ == "__main__":
	Main()
