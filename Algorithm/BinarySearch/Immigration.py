def solution(n, times):
    answer = 0
    min_time = times[0]
    max_time = times[0]*n
    while True:
        count = 0
        mid = (min_time+max_time)//2
        for i in times:
            count += mid//i
        if count >= n:
            max_time = mid
        elif count < n:
            min_time = mid
        if min_time == max_time - 1:
            answer = max_time
            break
    return answer
