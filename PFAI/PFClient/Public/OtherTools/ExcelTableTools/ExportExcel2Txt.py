import os
import xlrd
import sys

def ProcessDirectory(dir):
    files = {}
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        pos = fileName.rfind(".xls")
        if pos != -1 and fileName[0] != '~':
            if files != None:
                files[fileName[0:pos]] = dir + "/" + fileName

    for key in files:
        file = files[key]
        '''print("process excel file:" + file)'''
        allTxt = ""
        book = xlrd.open_workbook(file)
        '''print("book opend")'''
        sheet = book.sheets()[0]
        '''print("sheet opend")'''
        for i in range(0, sheet.nrows):
            for j in range(0, len(sheet.row_values(i))):
                sep = "\t"
                if j + 1 == len(sheet.row_values(i)):
                    sep = "\r\n"
                cell = sheet.cell(i, j)
                cellValue = cell.value
                if cell.ctype in (2, 3):
                    if int(cellValue) == cellValue:
                        cellValue = int(cellValue)
                    allTxt += str(cellValue) + sep
                else:
                    allTxt += cellValue + sep
        '''print("txt Parsed")'''
        txtName = dir + "\\" + key + ".txt"
        '''if os.path.isfile(txtName):
            print("EXCEL and TXT Both Exist with Name:" + key)'''
        txtFile = open(txtName, "w+b")
        txtFile.write(bytes(allTxt.encode("GBK")))
        txtFile.close()

def CleanUpDirectory(dir):
    files = {}
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        pos = fileName.rfind(".xls")
        if pos != -1 and fileName[0] != '~':
            if files != None:
                files[fileName[0:pos]] = dir + "/" + fileName

    for key in files:
        txtName = dir + "\\" + key + ".txt"
        if os.path.isfile(txtName):
            os.remove(txtName)

def Main():
    try:
        if len(sys.argv) < 1:
            return

        option = sys.argv[1]
        if option == "c":
            ProcessDirectory(os.path.join(os.getcwd(), "ClientTables"))
        elif option == "s":
            ProcessDirectory(os.path.join(os.getcwd(), "ServerTables"))
        elif option == "p":
            ProcessDirectory(os.path.join(os.getcwd(), "PublicTables"))
        elif option == "f":
            CleanUpDirectory(os.path.join(os.getcwd(), "ClientTables"))
            CleanUpDirectory(os.path.join(os.getcwd(), "ServerTables"))
            CleanUpDirectory(os.path.join(os.getcwd(), "PublicTables"))
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    Main()