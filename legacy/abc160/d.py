


def main():
    N, X, Y = map(int, input().split())

    G = [0]*N
    D = [0]*N
    for i in range(N):
        if i == 0:
            G[0] = [1]
        elif i == N-1:
            G[N-1] = [N-2]
        else:
            G[i] = [i-1, i+1]
        if i+1 == X:
            G[i].append(Y-1)
        if i+1 == Y:
            G[i].append(X-1)

        D[i] = [1 if j in G[i] else N for j in range(N)]

    import numpy as np
    D =np.array(D)

    for k in range(N):
        tmp = np.tile(D[:,k],(N,1))
        tmp_D = tmp + tmp.T
        D = np.min([D, tmp_D], axis=0)

    for i in range(1,N):
        tmp = (D==i).sum()
        if i ==2:
            tmp = tmp - N
        print(tmp//2)
    

if __name__ == '__main__':
    main()
