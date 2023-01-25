from collections import defaultdict

def solution(str):
    answer = []
    dict = defaultdict(int)

    for idx, s in enumerate(str):
        
        if dict[s] == 0:
            answer.append(-1)
            dict[s] = idx
        else:
            answer.append(idx - dict[s])
            dict[s] = idx

    return answer

str = "foobaro"
ans = solution(str)
print(ans)