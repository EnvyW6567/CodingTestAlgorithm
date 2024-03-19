import math

cantor = [1, 1, 0, 1, 1]


def solution(n, l, r):
    start, end = l, r
    answer = 0

    n_count = n
    while n_count > 0:
        denominator = pow(5, n_count)
        cantor_start = [math.floor(start / denominator), start % denominator]
        cantor_end = [math.floor(end / denominator), end % denominator]
        if cantor_start[0] != cantor_end[0]:
            for i in range(cantor_start[0] + 1, cantor_end[0]):
                answer += cantor[i] * pow(4, n_count)
            print(n_count, cantor_start, cantor_end, denominator, answer)
            start_count = s_cantor(n_count, start, 0)
            end_count = e_cantor(n_count, end, 0)
            print("start, end count : ", start_count, end_count)
            break
        n_count -= 1


def s_cantor(n, cur_cantor, count):
    denominator = pow(5, n)
    if math.floor(cur_cantor / denominator) == 0:
        for i in range(math.floor(cur_cantor / (denominator / 5))):
            count += cantor[i] * pow(4, n - 1)
            print(count)
        count = s_cantor(n - 1, cur_cantor, count)
    return count


def e_cantor(n, cur_cantor, count):
    denominator = pow(5, n)
    print("recursion: ", cur_cantor, denominator)
    if math.floor(cur_cantor / denominator) == 0:
        for i in range(math.floor(cur_cantor / (denominator / 5)) + 1, 5):
            count += cantor[i] * pow(4, n - 1)
            print(count)
        count = s_cantor(n - 1, cur_cantor, count)
    return count


solution(5, 100, 1500)
