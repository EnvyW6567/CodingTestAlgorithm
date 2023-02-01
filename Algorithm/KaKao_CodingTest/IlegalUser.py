# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations, combinations

def compare(comp, targ):
    if len(comp) != len(targ):
        return False
    for idx in range(len(comp)):
        if comp[idx] != "*" and comp[idx] != targ[idx]:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    user = [[]for _ in range(len(banned_id))]
    for i, comp in enumerate(banned_id):
        for targ in user_id:
            if compare(comp, targ):
                user[i].append(targ)

    candidate = []
    for l in user:
        for word in l:
            if word not in candidate:
                candidate.append(word)

    permu = list(permutations(candidate, len(banned_id)))
    bannedList = []
    for p in permu:
        count = 0
        for idx, id in enumerate(p):
            if id in user[idx]:
                count += 1
        if count == len(banned_id):
            lp = list(p)
            lp.sort()
            if lp not in bannedList:
                bannedList.append(lp)
                answer += 1
    
    return answer



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
