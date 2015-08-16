__author__ = 'aaronmsmith'


def distance_from_zero(arg):
    if type(arg)==int or type(arg)==float:
        return abs(arg)
    else:
        return "nope"

print distance_from_zero(-4.2)