# https://www.acmicpc.net/problem/1043
# 거짓말

# N 사람수, M 파티 수
from collections import defaultdict


def find_all_truth_knowers(relations, truth_knowers, member):
    if member not in truth_knowers:
        return truth_knowers

    for r_member in relations[member]:
        if r_member not in truth_knowers:
            truth_knowers[r_member] = True
            truth_knowers = find_all_truth_knowers(relations, truth_knowers, r_member)

    return truth_knowers


def solution(truths, parties):
    answer = 0
    truth_knowers = {}
    members_dict = {}
    relations = defaultdict(list)

    if not truths:
        return len(parties)

    for knower in truths:
        truth_knowers[knower] = True

    for members in parties:
        for i in range(len(members)):
            members_dict[members[i]] = True
            for j in range(i + 1, len(members)):
                relations[members[i]].append(members[j])
                relations[members[j]].append(members[i])

    for member in members_dict:
        truth_knowers = find_all_truth_knowers(relations, truth_knowers, member)

    for members in parties:
        lie = True
        for member in members:
            if member in truth_knowers:
                lie = False  # 진실을 말해야 함
                break

        if lie:
            answer += 1

    return answer


N, M = map(int, input().split())

t = list(map(int, input().split()))
t = t[1:]
p = []

for _ in range(M):
    m = list(map(int, input().split()))
    p.append(m[1:])

print(solution(t, p))
