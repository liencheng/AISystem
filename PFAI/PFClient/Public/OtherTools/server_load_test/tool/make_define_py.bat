@echo off
rem bat 读取define_template.txt和PacketID.cfg文件，生成Defines.py文件

if not exist define_template.txt (
	echo define_template.txt file not exist
	goto end
)

echo read define_template.txt ..

if not exist PacketID.cfg (
	echo PacketID.cfg file not exist
	goto end
)

echo read PacketID.cfg ..

set outfile=Defines.py

if exist %outfile% (
	del /f %outfile%
)

echo parsing ..

for /f "delims=" %%j in (define_template.txt) do (
	if %%j equ #line1 (
		echo.>> %outfile%
	) else if %%j neq #don't_modify_directly (
		echo %%j>> %outfile%
	) else (
		for /f "delims=" %%i in (PacketID.cfg) do (
			echo %%i,>> %outfile%
			rem if %label:~0,5% equ LABLE_ (
			rem 	echo %%i>> %outfile%
			rem ) else (
			rem 	echo %%i,>> %outfile%
			rem )
		)
	)
)

echo parsing finished
echo copy Defines.py to wmydjd\tasks\actions\net_packets

copy /Y Defines.py ..\wmydjd\tasks\actions\net_packets\

echo update Defines.py finished