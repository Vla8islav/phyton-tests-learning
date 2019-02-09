__author__ = 'vladislav'


def hello():
    print('Hello world')


def percent(x, y):
    """What percentage of x is y"""
    per = (y / x) * 100
    return per


def print_percent(x, y):
    """Printing what percentage of x is y"""
    print(str(y) + " is " + str(percent(x,y)) + "% of " + str(x))


hello()
hello()
hello()
print_percent(1, 6.0)
print_percent(100, 6.0)
print_percent(45, 6.0)
print_percent(15, 4)
