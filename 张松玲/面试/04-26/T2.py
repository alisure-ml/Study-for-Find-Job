"""
2 3
"""
import sys


def num():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        a, b, c = map(int, sys.stdin.readline().strip().split(" "))
        if (2*b*c-2*a)**2 - 4*b*b*c*c <= 0:
            print 0
        else:
            x1, x2 = 0
            area = (x2 ** 3 - x1 ** 3) * 2 * a/3 - b *(x2-x1)**2 - c * (x2-x1)
            print area

num()
