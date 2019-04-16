from math import sqrt


def solve(a, b, c):
    print('Equation ' + a.__str__() + 'x^2 + ' + b.__str__() + 'x + '+ c.__str__() + ' = 0')
    d = b * b - 4 * a * c
    if d < 0:
        print('No solutions')
    elif 0 == d:
            x = -b / (2 * a)
            print("One solution " + x.__str__())
    elif 0 < d:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("Two solutions - " + x1.__str__() + " and " + x2.__str__())
    else:
        print("Something went wrong")


solve(1, 2, 3)
solve(2, 4, 15)
solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)
