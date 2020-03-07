def main():

    A, B = map(int, input().split())
    v_A = int(A / 0.08)
    if (100*A) % (100*0.08) != 0:
        v_A += 1
    v_B = int(B / 0.1)
    if (100*B) % (100*0.1) != 0:
        v_B += 1
    v_A2 = int((A+1) / 0.08)
    v_B2 = int((B+1) / 0.1)

    A_cand = [i for i in range(v_A, v_A2)]
    B_cand = [i for i in range(v_B, v_B2)]

    # print(A_cand)
    # print(B_cand)
    ab_cand = set(A_cand) & set(B_cand)
    if len(ab_cand) == 0:
        print(-1)
    else:
        print(min(ab_cand))
    # print(ab_cand)


if __name__ == '__main__':
    main()
