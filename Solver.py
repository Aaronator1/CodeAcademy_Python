import math

__author__ = 'aaronmsmith'

class Solver:
    def demo(self):
        a=int(input("a "))
        b=int(input("b "))
        c=int(input("c "))
        d=b ** 2 - 4 * a * c
        answer= a * b * c
        print(answer)

Solver().demo()
