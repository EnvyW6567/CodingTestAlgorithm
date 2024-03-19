import math


def solution(s):
    answer = len(s)
    for divide_len in range(1, math.floor(len(s) / 2) + 1):
        cur_str = ""
        same_count_list = []
        same_count = 0
        str_length = len(s) % divide_len
        for i in range(math.floor(len(s) / divide_len)):
            split_str = s[i * divide_len:(i + 1) * divide_len]
            if split_str == cur_str or i == 0:
                same_count += 1
            else:
                same_count_list.append(same_count)
                same_count = 1
            cur_str = split_str
        same_count_list.append(same_count)

        str_length += calc_str_length(same_count_list, divide_len)
        if answer > str_length:
            answer = str_length
    print(answer)
    return answer


def calc_str_length(same_count_list, divide_length):
    str_length = 0
    for count in same_count_list:
        if count == 1:
            str_length += divide_length
        else:
            str_length += (divide_length + len(str(count)))

    return str_length


solution("ababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdabababcdcdab")
