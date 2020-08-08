import heapq
import sys

"""
3
0 0 1 1
2 2 3 3
4 4 5 5
"""


def get_min_dis(adj, num):
    min_dis = 0
    visit_node = [0]
    edges = []
    for j in range(num):
        if adj[0][j] >= 0:
            heapq.heappush(edges, [adj[0][j], 0, j])
        pass
    k = 1
    while k < num:
        w, vi, vj = heapq.heappop(edges)
        if vj not in visit_node:
            min_dis += w
            visit_node.append(vj)
            for i in range(num):
                if adj[vj][i] >= 0:
                    heapq.heappush(edges, [adj[vj][i], vj, i])
            k = k + 1
        pass
    return min_dis


def get_adj(n, pos):
    matrix = [[-1] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = -1
            else:
                pi, pj = pos[i], pos[j]
                ci = (pi[0] + pi[2]) / 2, (pi[1] + pi[3]) / 2
                cj = (pj[0] + pj[2]) / 2, (pj[1] + pj[3]) / 2
                a = abs(ci[0] - cj[0]) + abs(ci[1] - cj[1])
                b = (abs(pi[2] - pi[0]) + abs(pj[3] - pj[1])) / 2
                c = (abs(pi[3] - pi[1]) + abs(pj[2] - pj[0])) / 2
                matrix[i][j] = a - b - c
            pass
        pass
    return matrix


n = int(sys.stdin.readline().strip())

position = []
for i in range(n):
    b = map(int, list(sys.stdin.readline().strip().split(" ")))
    position.append(b)

adj = get_adj(n, position)
result = get_min_dis(adj, n)
print(result)
