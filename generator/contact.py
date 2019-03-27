import getopt
import os
import sys

import conftest
from generator.random_string import random_string
from generator.serialize import serialize_and_write
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

file = os.path.join(conftest.get_data_folder(), f)

test_data = [
    Contact(name=random_string("FirstName", 10), last_name=random_string('lastname', 10),
            middle_name=random_string('middleName', 10), email=random_string('232322', 10),
            email2=random_string('12121@243.ru', 10), email3=random_string('7777@vfd.re', 10),
            phone_fax=random_string('34234', 10), phone_home=random_string('3243242', 10),
            phone_mobile=random_string('+7(916) 111-22-33', 10), phone_work=random_string('321312', 10))
    for i in range(n)]

serialize_and_write(file, test_data)


