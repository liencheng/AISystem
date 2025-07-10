echo parsing PBMessage.proto ..
protoc --python_out=./ ./PBMessage.proto
echo parsing finished

echo copy PBMessage_pb2.py to wmydjd\tasks\actions\net_packets
copy /Y PBMessage_pb2.py ..\wmydjd\tasks\actions\net_packets
echo update PBMessage_pb2.py ok

pause
