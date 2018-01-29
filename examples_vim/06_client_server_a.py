#!/usr/bin/env python

"""
Example to demonstrate multi-host debugging.

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""

import socket
import sys


class Server(object):

    """
    Reports lengths of the messages
    """

    def __init__(self, addr, port):
        self.__addr = addr
        self.__port = int(port)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.__addr, self.__port)
        print("starting up on %s" % str(server_address))
        sock.bind(server_address)
        sock.listen(1)
        while True:
            print("waiting for a connection")
            connection, client_address = sock.accept()
            try:
                print("connection from %s" % str(client_address))
                data = ""
                while True:
                    #import pydevd; pydevd.settrace("127.0.0.1", True, True)
                    _data = connection.recv(16)
                    if not _data:
                        print("connection from %s closed" % str(client_address))
                        break
                    data += _data
                    if '\n' in _data:
                        for msg in data.splitlines():
                            connection.sendall(str(len(msg)))
                        data = ""
            finally:
                connection.close()


class Client(object):

    """
    Testing client which sends messages and makes sure server returns
    correct lengths.
    """

    def __init__(self, addr, port):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((addr, int(port)))

    def send(self, msg):
        self.__sock.sendall(msg)
        exp = len(msg)
        act = int(self.__sock.recv(1024))
        assert exp == act, "Expected: %s, Actual: %s" % (exp, act)


def test(addr, port):
    client = Client(addr, port)
    #import pydevd; pydevd.settrace("127.0.0.1", True, True)
    client.send("Foo\n")
    client.send("Bar")
    client.send("Foo\nBar")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Provide 3 arguments {c|s} $addr $port")
        sys.exit(-1)
    elif sys.argv[1].startswith("s"):
        Server(*sys.argv[2:4]).run()
    else:
        test(*sys.argv[2:4])
