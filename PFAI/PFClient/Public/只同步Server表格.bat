@echo off
echo ׼����ʼͬ������˱��

echo ����Ŀ���ļ���
set ServerTableFolder=../Server/Config/
set PublicServerTablesFolder=./ServerTables/

echo ת�����������ΪUTF8��ʽ��������

if %PROCESSOR_ARCHITECTURE%==x86 goto p1 else goto p2

:p2
echo x64������...
start /wait ./OtherTools/TxtConvExe_64/TxtConvWin7_64.exe  %PublicServerTablesFolder% %ServerTableFolder%
goto ep

:p1
echo x86������...
start /wait ./OtherTools//TxtConvExe/TxtConv.exe  %PublicServerTablesFolder% %ServerTableFolder%
goto ep

:ep
CD %ServerTableFolder%

echo �ɹ�

pause
