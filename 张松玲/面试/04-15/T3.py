#coding=utf-8
"""
5 2 3 1 0 0
1 20 2 3
2 30 3 4 5 
3 50 4
4 60
5 80
"""
import sys


def f():
    ns = map(int, sys.stdin.readline().strip().split())
    n, c = ns[0], ns[1:]

    is_na = False
    d, ni_s = [], []
    for i in range(n):
        ni = map(int, sys.stdin.readline().strip().split())
        ni_s.append(ni)

        # 未给出调用栈大小
        if c[i] + 2 != len(ni):
            is_na = True
            break

        # 1
        if c[i] > 0:
            h = False
            d_new = []
            for d_i, d_o in enumerate(d):
                if d_o[-1] == ni[0]:
                    h = True
                    d_add = []
                    for ni_o in ni[2:]:
                        d_n = [_ for _ in d_o]
                        d_n.append(ni_o)
                        d_add.append(d_n)
                        pass
                    d_new.append([d_i, d_add])
                pass
            if len(d_new) > 0:
                for d_new_o in d_new:
                    d.extend(d_new_o[1])
            if not h:
                for ni_o in ni[2:]:
                    d.append([ni[0], ni_o])
            pass
        pass

    if is_na:
        print "NA"

    # 是否循环
    is_r = False
    for d_o in d:
        if len(set(d_o)) != len(d_o):
            is_r = True
    if is_r:
        print "R"

    # 求最大值
    value = max([sum([ni_s[d_o_o - 1][1] for d_o_o in d_o]) for d_o in d])
    print value
    pass


if __name__ == '__main__':
    f()
    pass
