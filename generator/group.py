import getopt
import json
import os
import sys

import conftest
from generator.random_string import random_string
from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

file = os.path.join(conftest.get_data_folder(), f)

test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(n)]

with open(file, "w") as f:
    f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
