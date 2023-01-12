def solution(key, lock):
    # 키 개수가 자물쇠 구멍 개수보다 작을경우
    kCount, lCount = 0, 0
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                kCount += 1
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                lCount += 1

    if lCount > kCount:
        answer = False

    for i in r
    answer = True
    return answer
