#!/usr/bin/env python

"""
Example to demonstrate the difference when stdout is or is not re-directed
in pydevd

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""

#import pdb; pdb.set_trace()
#import pydevd; pydevd.settrace("127.0.0.1")
#import pydevd; pydevd.settrace("127.0.0.1", True, True)

print("Hello")
print("World")
foo = "foo"
bar = "bar"
