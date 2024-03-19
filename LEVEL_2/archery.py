from itertools import combinations


def solution(n, info):
    apeaches = info
    answer = [0 for i in range(11)]
    apeach_score, ryan_score = 0, 0
    exps = []
    for idx, apeach in enumerate(apeaches):
        if n > apeach:
            if apeach > 0:
                exps.append([(10 - idx) * 2, apeach + 1, idx])
            else:
                exps.append([10 - idx, 1, idx])
        apeach_score += 10 - idx if apeach > 0 else 0

    max_score, max_target = 0, ()
    for score_num in range(n, 0, -1):
        for possible in combinations(exps, score_num):
            score, required_arrow = 0, 0
            for p in possible:
                score += p[0]
                required_arrow += p[1]
            if max_score < score and required_arrow <= n:
                max_score = score
                max_target = possible

    if max_score <= apeach_score:
        return [-1]

    for target in max_target:
        answer[target[2]] = target[1]

    if sum(answer) < n:
        answer[10] += n - sum(answer)
    return answer

solution(3, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])
