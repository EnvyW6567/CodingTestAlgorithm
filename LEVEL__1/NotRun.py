from collections import defaultdict
import numpy as np


def solution(N, stages):
    count = 0
    stg_dic = defaultdict(int)
    rate = [0 for _ in range(N+2)]
    for i in stages:
        stg_dic[i] += 1
    for i in range(N+1, 0, -1):
        count += stg_dic[i]
        if stg_dic[i] == 0:
            rate[i] = 0
        else:
            rate[i] = stg_dic[i]/count
    rate = np.array(rate)
    answer = np.argsort(rate)[::-1]
    return answer
