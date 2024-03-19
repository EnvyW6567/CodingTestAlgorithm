index = {
    'java': 0, 'python': 8, 'cpp': 16,
    'backend': 0, 'frontend': 4,
    'junior': 0, 'senior': 2,
    'pizza': 0, 'chicken': 1
}
column = {
    0: [8, 16],
    1: [4],
    2: [2],
    3: [1]
}


def solution(info, query):
    answer = []
    applicants, requires = [[] for _ in range(24)], [[] for _ in range(24)]
    for i in info:
        applicant = i.split(" ")
        score = applicant.pop()
        idx = 0
        for a in applicant:
            idx += index[a]
        applicants[idx].append(int(score))

    for idx, applicant in enumerate(applicants):
        applicants[idx] = sorted(applicant)

    for require in query:
        require = require.split(" and ")
        soul_food, score = require.pop().split(" ")
        require.append(soul_food)
        available = get_available(require)
        passed = 0
        for a in available:
            passed += len(applicants[a]) - binary_search(applicants[a], int(score) - 1)

        answer.append(passed)
    return answer


def qualify(require, applicant):
    if require == applicant or require == '-':
        return True
    try:
        if int(require) < int(applicant):
            return True
    except ValueError:
        return False


def get_available(require):
    available = [0]
    for c, r in enumerate(require):
        tmp_available = available[:]
        if r == '-':
            available_column = column[c]
            for ac in available_column:
                for ta in tmp_available:
                    available.append(int(ta + ac))
        else:
            for idx, a in enumerate(available):
                a += index[r]
                available[idx] = a
    return available


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
)
