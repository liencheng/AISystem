echo ׼����ʼ���ɱ���

set homeford=%cd%
echo %homeford%
cd..
cd..
set workpath=%cd%
cd "%homeford%"

echo 设置目标文件夹
set DstTableFolder=%workpath%\Client\Assets\Game\Script\GlobalSystem\GameTables
set SrcTableFolder=%workpath%\Public\CreateTableTool\TmpClientDic
set ClientTableFolder=%workpath%\Client\Assets\Game\Table\

rem 设置本地目录，生成到本地，手动拷贝到指定目标目录
rem set DstTableFolder=./DstCSharp
rem set SrcTableFolder=./SrcTXT

echo 请将txt表格放入到%SrcTableFolder%目录下
xcopy /Y %ClientTableFolder%*.txt %SrcTableFolder%  /s  /e


for /r ".\CodeTable\CSharp\AOT" %%i in (*.cs) do del "%%i" /f /q >nul 2>nul 
for /r ".\CodeTable\CSharp\HotFix" %%i in (*.cs) do del "%%i" /f /q >nul 2>nul 

echo 开始生成代码文件...

if %PROCESSOR_ARCHITECTURE%==x86 goto p1 else goto p2

:p2
echo x64处理中...
PlistTableCode.exe -d:%SrcTableFolder% -CSharp
goto ep

:p1
echo x86处理中...
PlistTableCode.exe -d:%SrcTableFolder% -CSharp
goto ep

:ep
echo 拷贝*.cs

REM for /r "%DstTableFolder%" %%i in (*.cs) do del "%%i" /f /q >nul 2>nul 

xcopy /Y .\CodeTable\CSharp\AOT %DstTableFolder%  /s  /e

echo add%DstTableFolder%路径下所有文件到svn
svn add %DstTableFolder% --no-ignore --force

for /r ".\CodeTable\CSharp\AOT" %%i in (*.cs) do del "%%i" /f /q >nul 2>nul 
for /r ".\CodeTable\CSharp\HotFix" %%i in (*.cs) do del "%%i" /f /q >nul 2>nul 
for /r "%SrcTableFolder%" %%i in (*.txt) do del "%%i" /f /q >nul 2>nul


echo 请及时到相关目录Add文件，不然就编不过啦！ 

pause
