"""
2
4
1 2
3 4
5 6
1 6
4
1 2
3 4
5 6
7 8
"""
import sys

def get_friends(friends):
    while True:
        flag = False
        for i in range(len(friends)):
            for j in range(i + 1, len(friends)):
                for x in friends[j]:
                    if x in friends[i]:
                        friends[i].extend(friends[j])
                        friends[j] = []
                        flag = True
                        break
        if not flag:
            break
    return max([len(set(i)) for i in friends])
def num():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        friends = []
        for j in range(n):
            x, y = map(int, sys.stdin.readline().strip().split(" "))
            friends.append([x, y])
        print get_friends(friends)
    pass

num()

