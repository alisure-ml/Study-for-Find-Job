import sys

"""
1
3 2
1 2 5
10 11 6
12 12 7
"""


def f2(list_in, k, y, x):
    list_r = []
    now_v = list_in[y][x]

    start, end = x - k, x + k + 1
    start = start if start > 0 else 0
    end = end if end < len(list_in) else len(list_in)
    for i in range(start, end):
        if list_in[y][i] > now_v and x != i:
            list_r.append([y, i])

    start, end = y - k, y + k + 1
    start = start if start > 0 else 0
    end = end if end < len(list_in) else len(list_in)
    for i in range(start, end):
        if list_in[i][x] > now_v and y != i:
            list_r.append([i, x])

    return list_r


def f1(list_in, k, y, x):
    now_v = list_in[y][x]
    list_r = f2(list_in, k, y, x)
    if len(list_r) == 0:
        return now_v

    list_b = []
    for r_one in list_r:
        v = f1(list_in, k, r_one[0], r_one[1])
        list_b.append(v)
        pass
    return now_v + max(list_b)


if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for t_i in range(t):
        line = sys.stdin.readline().strip()
        n, k = map(int, line.split())
        now_list = []
        for i in range(n):
            line = sys.stdin.readline().strip()
            value = map(int, line.split())
            now_list.append(value)
            pass

        print f1(now_list, k, 0, 0)
        pass
    pass
