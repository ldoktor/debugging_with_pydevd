#!/usr/bin/env python

"""
Example to demonstrate the possible issues with redirecting stdout/stderr
in pydevd

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""


import os
import sys


class Paginator(object):

    """
    Paginator that uses less to display contents on the terminal.
    """

    def __init__(self):
        self.pipe = os.popen("less -FRX", "w")

    def __del__(self):
        self.close()

    def close(self):
        """Cleanup the paginator"""
        try:
            self.pipe.close()
        except Exception:
            pass

    def write(self, msg):
        """Forward data to the paginator"""
        try:
            self.pipe.write(msg)
        except Exception:
            pass

    def flush(self):
        """Force-flush data"""
        if not self.pipe.closed:
            self.pipe.flush()



if __name__ == "__main__":
    _STDOUT = sys.stdout
    _STDERR = sys.stderr
    try:
        sys.stdout = sys.stderr = Paginator()
        print("A long line that hopefully enables pagination: %s" % "." * 100)
        print("bar")
        #import pydevd; pydevd.settrace("127.0.0.1")
        #import pydevd; pydevd.settrace("127.0.0.1", True, True)
        print("baz")
    finally:
        if isinstance(sys.stdout, Paginator):
            _PAGINATOR = sys.stdout
            sys.stdout = _STDOUT
            sys.stderr = _STDERR
            _PAGINATOR.close()
