def solution(people, hats):
    answer = 0
    people = sorted(people)
    hats = sorted(hats)

    for p in people:
        for idx, h in enumerate(hats):
            if p - h < -3:
                del hats[idx]
            elif p - h <= 3:
                answer += 1
                break
            else:
                break

    return answer


print(solution([4, 8, 2], [6, 10, 7]))
