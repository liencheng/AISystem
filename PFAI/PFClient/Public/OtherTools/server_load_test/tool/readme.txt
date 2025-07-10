


【目录说明】
自建脚本
make_define_py.bat	读取define_template.txt和PacketID.cfg文件，生成Defines.py文件
make_proto_py.bat	读取PBMessage.proto，生成PBMessage_pb2.py
make_PACKETS_py.bat	调用genPackets.py，功能：根据PacketID.cfg，更新PACKETS.py， 如果有特写保留特写，如果有增加或删除，则相应增加或删除（删除的协议如果有特写，则改删除为注释
genActions.py		
genActionsParams.py	


继承脚本
GetPackets.cmd 调用tshark.exe截取协议存到pdml.xml文件，再调用Buf2TXT.py，解析pdml.xml，生成