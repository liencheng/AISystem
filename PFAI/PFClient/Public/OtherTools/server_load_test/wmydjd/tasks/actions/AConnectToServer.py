import loadlog

from gevent import socket


class AConnectToServer:
    def __init__(self, person):
        self.person = person

    def run(self, ip, port,log=loadlog):
        self.log = log
        """returns:
            param[0]:True if success, False if fail
            param[1]: 0
            param[2]: error message"""
        try:
            self.person['socket'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.person['socket'].connect((ip, port))
            if self.person['socket']:
                if self.log:
                    self.log.debug("AConnectToServer successfully. Connect IP = %s, port = %d" % (ip, port))
                return True, 0, "AConnectToServer successfully. Connect IP = %s, port = %d" % (ip, port)
            else:
                if self.log:
                    self.log.error("AConnectToServer Failed. account %s Connect IP = %s, port = %d" %
                                   (self.person['account'], ip, port))
                return False, 0, "AConnectToServer failed. IP = %s, port = %d" % (ip, port)
        except Exception as e:
            return False, 0, "AConnectToServer failed. IP = %s, port = %d" % (ip, port)