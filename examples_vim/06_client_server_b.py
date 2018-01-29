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
                unfinished = 0
                while True:
                    #import pydevd; pydevd.settrace("127.0.0.1", True, True)
                    _data = connection.recv(16)
                    if not _data:
                        print("connection from %s closed" % str(client_address))
                        break
                    lines = _data.split('\n')
                    out = []
                    if len(lines) > 1:
                        connection.sendall("%s\n"
                                           % (unfinished + len(lines[0])))
                        unfinished = 0
                    for line in lines[1:-1]:
                        connection.sendall("%s\n" % len(line))
                    if lines[-1]:
                        unfinished += len(lines[-1])
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
        self.__unfinished = 0
        print("Client will be using %s %s" % (addr, port))

    def send(self, msg):
        self.__sock.sendall(msg)
        lines = msg.split('\n')
        exp = []
        #import pydevd; pydevd.settrace("127.0.0.1", True, True)
        if len(lines) > 1:  # when not last line, contains \n
            exp.append(len(lines[0]) + self.__unfinished)
            self.__unfinished = 0
        for line in lines[1:-1]:
            exp.append(len(line))
        if lines[-1]:  # Last line does not contain \n
            self.__unfinished += len(lines[-1])
        exp = "\n".join(str(_) for _ in exp)
        if exp:
            exp += "\n"
        act = ""
        while not len(exp) <= len(act):
            _act = self.__sock.recv(1024)
            if not _act:
                print("connection closed")
                break
            act += _act
        assert exp == act, "Expected:\n%s\nActual:\n%s" % (exp, act)
        print("%r == %r" % (exp, act))


def test(addr, port):
    client = Client(addr, port)
    #import pydevd; pydevd.settrace("127.0.0.1", True, True)
    client.send("\n")
    client.send("\n")
    client.send("Foo\n")
    client.send("Bar")
    client.send("Foo\nBar\n")
    client.send("Foo\nBar")
    client.send("\nBaz\n")
    client.send("\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Provide 3 arguments {c,s} $addr $port")
        sys.exit(-1)
    elif sys.argv[1].startswith("s"):
        Server(*sys.argv[2:4]).run()
    else:
        test(*sys.argv[2:4])
