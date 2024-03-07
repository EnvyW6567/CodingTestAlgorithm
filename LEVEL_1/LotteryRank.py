def solution(lottos, win_nums):
    count = 7
    none = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                count -= 1
        else:
            none += 1
    if count == 7:
        low = 6
    else:
        low = count
    if none == 6:
        high = 1
    else:
        high = low-none
    answer = []
    answer.append(high)
    answer.append(low)
    return answer
