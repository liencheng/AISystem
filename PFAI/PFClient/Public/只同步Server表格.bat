@echo off
echo 准备开始同步服务端表格

echo 设置目标文件夹
set ServerTableFolder=../Server/Config/
set PublicServerTablesFolder=./ServerTables/

echo 转化服务器表格为UTF8格式，并拷贝

if %PROCESSOR_ARCHITECTURE%==x86 goto p1 else goto p2

:p2
echo x64处理中...
start /wait ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe  %PublicServerTablesFolder% %ServerTableFolder%
goto ep

:p1
echo x86处理中...
start /wait ./OtherTools//TxtConvExe/TxtConv.exe  %PublicServerTablesFolder% %ServerTableFolder%
goto ep

:ep
CD %ServerTableFolder%

echo 成功

pause
