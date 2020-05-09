"""
2 3
"""
import sys


def num():
    m, n = map(int, sys.stdin.readline().strip().split(" "))
    r = ((m ** n) - m * (m - 1) ** (n - 1)) % 100003
    print r

num()
