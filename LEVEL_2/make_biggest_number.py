# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = []
    number = [int(i) for i in number]
    while k > 0:
        max, max_idx = 0, 0
        for i in range(0, k + 1):
            if max < number[i]:
                max = number[i]
                max_idx = i
        number = number[max_idx + 1:]
        answer.append(max)
        k -= max_idx
    for n in number:
        answer.append(n)
    answer = ''.join(map(str, answer))
    return answer


print(solution('1111111111111', 4))
