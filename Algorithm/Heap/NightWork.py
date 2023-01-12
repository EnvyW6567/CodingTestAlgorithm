def solution(n, works):

    works.sort(reverse=True)
    print(works)
    idx = 0
    for _ in range(n):

        works[idx] -= 1
        # 맨 끝에 도달하거나
        if idx == len(works)-1:
            if works[idx] == 0:
                break
            idx = 0
            continue

        # 현재 값이 다음 값보다 클 경우
        elif works[idx] >= works[idx+1]:
            idx = 0
            continue

        idx += 1

    answer = 0
    for i in works:
        answer += i*i
    return answer


works = [1, 5, 4, 3, 3]
n = 10
solution(n, works)
