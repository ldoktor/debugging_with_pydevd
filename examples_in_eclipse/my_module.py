"""
To be imported module...

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""

class Foo(object):
    pass

class Bar(Foo):
    def don_use_mutable_objects_as_default_parmas(self, param={}):
        return param


foo = Foo()
bar = Bar()

if __name__ == "__main__":
    print("I am __main__")
