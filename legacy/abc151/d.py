def main():
    import sys
    input = sys.stdin.readline

    H, W = map(int, input().split())
    S = [list(input().split()[0]) for i in range(H)]

    from collections import deque

    dist = [0]*(H*W)
    for s in range(H*W):
        search_list = deque([s])
        visited_set = set([])
        d = [0] * (H*W)
        while search_list:
            now = search_list.popleft()
            visited_set.add(now)
            h = now // W
            w = now % W
            if S[h][w] == '#':
                continue
            for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_h = h+i
                new_w = w+j
                new_s = new_h * W + new_w
                if new_h in [-1, H] or new_w in [-1, W]:
                    continue
                elif new_s in search_list:
                    continue
                elif new_s in visited_set:
                    continue
                elif S[new_h][new_w] == '#':
                    continue
                else:
                    d[new_s] = d[now]+1
                    search_list.append(new_s)
        dist[s] = max(d)
    print(max(dist))


if __name__ == "__main__":
    main()
