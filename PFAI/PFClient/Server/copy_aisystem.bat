@echo off
rem 要复制的源文件
set "SRCEXE=%~dp0../../x64/Debug/PFAI.exe"
set "SRCPDB=%~dp0../../x64/Debug/PFAI.pdb"
rem %~dp0 代表当前 .bat 文件自身所在的目录，最后自带反斜杠
copy "%~dp0..\..\x64\Debug\PFAI.exe" "%~dp0" /Y
copy "%~dp0..\..\x64\Debug\PFAI.pdb" "%~dp0" /Y
echo Copied %SRCEXE% to %~dp0
echo Copied %SRCPDB% to %~dp0
pause
