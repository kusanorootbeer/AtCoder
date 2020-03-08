
import numpy as np
import sys
from sys import stdin
input = stdin.readline

sys.setrecursionlimit(10)


def main():

    def get_dist(K, edges, N):
        roots = [[] for i in range(N)]
        for a, b in edges:
            roots[a-1] += [(b-1, 1)]
            roots[b-1] += [(a-1, 1)]
        dist = [-1]*N
        stack = []
        stack.append(K)
        dist[K] = 0
        while stack:
            label = stack.pop(-1)
            for i, c in roots[label]:
                if dist[i] == -1:
                    dist[i] = dist[label]+c
                    stack += [i]
        return dist

    N = int(input())
    edges = []
    for i in range(N-1):
        edges += [list(map(int, input().split()))]
    print(edges)
    distance = [[]]*N
    for i in range(N):
        distance[i] = get_dist(i, edges, N)
    print(distance)


if __name__ == '__main__':
    main()
