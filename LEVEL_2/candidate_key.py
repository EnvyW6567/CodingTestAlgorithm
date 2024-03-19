from itertools import combinations


def solution(relation):
    possible_keys, candidate_keys = [], []
    column = [i for i in range(len(relation[0]))]
    for i in range(len(relation[0])):
        for key in combinations(column, i + 1):
            possible_keys.append(key)

    for pk in possible_keys:
        is_subset_candidate_key = False
        for ck in candidate_keys:
            if is_subset(ck, pk):
                is_subset_candidate_key = True
                break
        if is_subset_candidate_key:
            continue

        check_duplicate_map, is_candidate = {}, True
        for row in range(len(relation)):
            key = ""
            for p in pk:
                key += relation[row][p]
            if key in check_duplicate_map:
                is_candidate = False
                break
            check_duplicate_map[key] = 1
        if is_candidate:
            candidate_keys.append(pk)

    return len(candidate_keys)


def is_subset(a, b):
    return all(elem in b for elem in a)

solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
