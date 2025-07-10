@echo off
setlocal

REM =======================================================================
REM AutoTest Team Source File.
REM Copyright(C), Changyou.com
REM Connector:        2015/12/03 by zhangbingpeng@cyou-inc.com
REM -----------------------------------------------------------------------
REM Dissector.cmd
REM Description:    
REM invoke tshark to get packets and output as pdml format
REM -----------------------------------------------------------------------
REM History:
REM 2015/12/03:     zhangbingpeng@cyou-inc.com
REM =======================================================================



set WIRESHARKEXE="C:\Program Files (x86)\Wireshark\tshark.exe"
::set FILTERSTR="(src 10.12.26.153 and dst 120.132.89.114) or (src 120.132.89.114 and dst 10.12.26.153)"
set FILTERSTR="(src 10.12.1.160 and dst 10.1.14.134) or (src 10.1.14.134 and dst 10.12.1.160)"
set DURATIONTIME=120
set OUTPUT=pdml.xml
echo %time%:  %WIRESHARKEXE% -i 1 -f %FILTERSTR% -a duration:%DURATIONTIME% -T pdml > %OUTPUT%
%WIRESHARKEXE% -i 1 -f %FILTERSTR% -a duration:%DURATIONTIME% -T pdml > %OUTPUT%
endlocal