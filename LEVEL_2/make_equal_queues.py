# https://school.programmers.co.kr/learn/courses/30/lessons/118667
def solution(queue1, queue2):
    sum_queue = sum(queue1 + queue2)
    answer = 0

    if sum_queue % 2 == 1:
        return -1

    queue = queue1 + queue2
    start, end = 0, len(queue1) - 1  # start ~ end 합
    sum_range = sum(queue[start:end + 1])

    while start <= end < len(queue):
        if sum_range == sum_queue / 2:  # 범위와 범위 바깥의 합이 같을 때
            return answer

        if sum_range < sum_queue / 2:  # 합의 절반 보다 작을 때, 범위 증가
            end += 1
            answer += 1
            if end < len(queue):
                sum_range += queue[end]
        else:  # 합의 절반 보다 클 때, 범위 감소
            sum_range -= queue[start]
            start += 1
            answer += 1
    return -1


print(solution(	[1, 2, 1, 2], [1, 10, 1, 2]))
