from collections import defaultdict


def solution(id_list, report, k):
    reporter = defaultdict(list)
    report_count = defaultdict(int)
    out = []
    for i in report:
        a = list(map(str, i.split()))
        if a[1] not in reporter[a[0]]:
            report_count[a[1]] += 1
            reporter[a[0]].append(a[1])
    for i in id_list:
        if report_count[i] >= k:
            out.append(i)
    answer = [0 for _ in range(len(id_list))]
    for idx, i in enumerate(id_list):
        for j in out:
            if j in reporter[i]:
                answer[idx] += 1
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
solution(id_list, report, k)
