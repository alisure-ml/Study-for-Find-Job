import sys
from collections import deque

MAX_VALUE = 0x7fffffff


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    pass


def bfs(maze, begin, end):
    n, m = len(maze), len(maze[0])
    dist = [[MAX_VALUE for _ in range(m)] for _ in range(n)]
    pre = [[None for _ in range(m)] for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    sx, sy = begin.x, begin.y
    gx, gy = end.x, end.y

    dist[sx][sy] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        curr = queue.popleft()
        find = False
        for i in range(4):
            nx, ny = curr.x + dx[i], curr.y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and dist[nx][ny] == MAX_VALUE:
                dist[nx][ny] = dist[curr.x][curr.y] + 1
                pre[nx][ny] = curr
                queue.append(Point(nx, ny))
                if nx == gx and ny == gy:
                    find = True
                    break
        if find:
            break
    return dist[gx][gy]


n, m = map(int, list(sys.stdin.readline().strip().split(" ")))


maze = []
for i in range(n):
    m_list = list(sys.stdin.readline().strip())
    maze.append(m_list)
    pass

fdis = 0
for i1 in range(n):
    for j1 in range(m):
        if maze[i1][j1] == "#":
            continue
        for i2 in range(n):
            for j2 in range(m):
                if maze[i2][j2] == "#":
                    continue
                begin = Point(i1, j1)
                end = Point(i2, j2)
                dis = bfs(maze, begin, end)
                if fdis < dis < MAX_VALUE:
                    fdis = dis
print fdis

"""
3 3
...
.##
...
"""