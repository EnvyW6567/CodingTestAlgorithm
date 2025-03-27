# https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    answer = 0
    count = 0
    for i in range(len(str(storey)) - 1, -1, -1):
        if int(str(storey)[i]) > 5:
            answer += 10 - int(str(storey)[i])
            storey += (10 - int(str(storey)[i])) * (10 ** count)
        else:
            answer += int(str(storey)[i])
            storey -= int(str(storey)[i]) * (10 ** count)
        print(answer, storey)
        count += 1


solution(5555)
