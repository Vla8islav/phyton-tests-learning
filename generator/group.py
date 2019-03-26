import json
import os
import random
import string

import conftest
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' * 5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]

file = os.path.join(conftest.get_data_folder(), "groups.json")

with open(file, "w") as f:
    f.write(json.dumps(test_data, default=lambda x: x.__dict__))
