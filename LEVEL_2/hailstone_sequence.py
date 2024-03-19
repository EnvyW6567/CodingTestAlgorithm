def solution(k, ranges):
    answer = []
    collatz = [k]

    while k > 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1
        collatz.append(int(k))

    for r in ranges:
        start, end = r[0], len(collatz) - 1 + r[1]
        if start > end:
            answer.append(-1)
            continue

        integral = 0
        for i in range(start, end):
            integral += (collatz[i] + collatz[i + 1]) / 2
        answer.append(integral)

    return answer


solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]])
