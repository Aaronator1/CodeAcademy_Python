__author__ = 'aaronmsmith'

def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(5,7)
smallest_number(5,7)
distance_from_zero(-10)