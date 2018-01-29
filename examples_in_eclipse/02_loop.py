#!/usr/bin/env python

"""
Example to demonstrate F5, F6, F7, F8 and CTRL+F2
in Eclipse debugger.

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""


def say(msg):
    """
    Prints $msg
    :param msg: Message to be printed
    """
    print(msg)

def multi_say(iterations, msg):
    """
    Says $msg $iterations times
    :param iterations: How many times to repeat the $msg
    :param msg: Message to be printed
    """
    for _ in range(iterations):
        say(msg)

if __name__ == "__main__":
    multi_say(10, "Hello World")
