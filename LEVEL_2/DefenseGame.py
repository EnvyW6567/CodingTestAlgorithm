# https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 우선순위 큐
import queue

def solution(n, k, enemy):
    invincibleRound = queue.PriorityQueue()
    answer = 0
    enemyNum = 0
    for e in enemy:
        if len(invincibleRound.queue) < k:
            invincibleRound.put(e)
            answer += 1
        else: # 무적권 다 썼을때 가장 작은 것을 꺼내고 put e
            if invincibleRound.queue[0] < e:
                enemyNum += invincibleRound.get()
                invincibleRound.put(e)
            else:
                enemyNum += e
            if enemyNum > n:
                break
            answer += 1
    return answer

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
solution(n, k, enemy)