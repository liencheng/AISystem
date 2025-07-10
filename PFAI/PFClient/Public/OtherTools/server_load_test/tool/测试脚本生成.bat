rem 本工具脚本使用python3制作，需要安装python3执行

rem 测试脚本生成，将抓包工具保存的pcap文件放到pcaps文件夹下
rem 修改输入和输出文件名，然后运行此脚本
rem 文件的actions(协议)序列在lastaction.log中
rem 生成的文件在outputs文件夹中

C:\Python39\python.exe parse_scap.py --pcap=change_scene.pcap --output=change_scene

echo found action infos in lastaction.log
echo check output python file under ./outputs/
pause