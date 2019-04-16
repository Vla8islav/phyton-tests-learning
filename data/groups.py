import random
import string

import pytest

from generator.random_string import random_string
from model.group import Group


test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]
