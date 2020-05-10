def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    visited = [0]
    visited_set = set([0])
    now = 0
    ind = 0
    my_append = visited.append
    my_add = visited_set.add
    for _ in range(K):
        a = A[now]-1
        if a in visited_set:
            ind = visited.index(a)
            break
        else:
            my_add(a)
            my_append(a)
            now = a

    loop_visited = visited[ind:]
    ans_ind = (K-ind) % len(loop_visited)

    print(loop_visited[ans_ind]+1)


if __name__ == "__main__":
    main()
