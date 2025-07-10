rem 本工具脚本使用python3制作，需要安装python3执行

call make_define_py.bat
call make_proto_py.bat

echo begin generate PACKETS.py
python genPACKETS.py
python genPACKETShandle.py
echo finish genearate PACKETS.py

echo begin generate actions
python genActions.py
python genActionsParams.py
echo finish genearate actions

echo finished all.
pause