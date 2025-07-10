from . import Defines
import logging
import struct
from tasks.actions.net_packets import PBMessage_pb2
# from person import Person


class Packet:
    def __init__(self, person):
        self.person = person
        self.obj = eval("PBMessage_pb2." + self.__class__.__name__ + "()")

    def __getitem__(self, name):
        return eval("self.obj." + name)

    def __setitem__(self, name, value):
        if isinstance(value, str):
            return eval("self.obj.__setattr__(\"" + name + "\",\"" + value + "\")")
        else:
            return eval("self.obj.__setattr__(\"" + name + "\"," + str(value) + ")")

    def get_data_stream(self):
        return self.obj.SerializeToString()

    def fill_data_from_stream(self, buf):
        self.obj.ParseFromString(buf)

    def get_id(self):
        return Defines.ID_DEFINE(self.__class__.__name__)

    def get_data_size(self):
        return self.obj.ByteSize()

    def dump(self):
        return str(self.obj)

    def has_field(self, field):
        return self.obj.HasField(field)


# if __name__ == "__main__":
#     class PTest:
#         def __init__(self, name):
#             self.obj = eval("PBMessage_pb2." + name + "()")
#
#
#         def __getitem__(self, name):
#             return eval("self.obj." + name)
#
#         def __setitem__(self, name, value):
#             if isinstance(value, str):
#                 return eval("self.obj.__setattr__(\"" + name + "\",\"" + value + "\")")
#             else:
#                 return eval("self.obj.__setattr__(\"" + name + "\"," + str(value) + ")")
#
#         def __str__(self):
#             return self.obj
#     buf = b''
#     test = PTest('GC_SESSION')
#     print(test)