#!/usr/bin/env python

"""
Example to walk through the import process

* as a bonus demonstrate why pylint warns about mutable objects used as
  default variables

Copyright: Red Hat, Inc. 2018
Author: Lukas Doktor <ldoktor@redhat.com>
License: GPLv3+
"""

from pprint import pprint

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import my_module

pprint(locals())
pprint(dir(my_module))

# And now why you shouldn't be using mutable objects?
params1 = my_module.bar.don_use_mutable_objects_as_default_parmas()
print(params1)
params1["foo"] = "bar"
bar2 = my_module.Bar()
params2 = bar2.don_use_mutable_objects_as_default_parmas()
print(params2)
params2["One or two beers are literally"] = "12 beers"
print(my_module.bar.don_use_mutable_objects_as_default_parmas())
