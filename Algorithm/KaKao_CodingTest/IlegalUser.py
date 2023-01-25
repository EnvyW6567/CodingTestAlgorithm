# https://school.programmers.co.kr/learn/courses/30/lessons/64064

def compare(comp, targ):
    if len(comp) != len(targ):
        return False
    for idx in range(len(comp)):
        if comp[idx] != "*" and comp[idx] != targ[idx]:
            return False
    return True


# def combination(possible_list):
#     comb = []
#     for possible in possible_list:
#         for p in possible:

#     return comb


def solution(user_id, banned_id):
    answer = 0
    list = [[]for _ in range(len(banned_id))]
    for i, comp in enumerate(banned_id):
        for targ in user_id:
            if compare(comp, targ):
                print(comp, targ)
                list[i].append(targ)
    print(list)
    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*****", "*rodo", "*r*do", "******"]
print(solution(user_id, banned_id))
