# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):

    answer = converse_to_proper(p)
    print(answer)

    return answer


def converse_to_proper(brackets):
    if len(brackets) == 0:
        return ''
    u, v = split_balanced_brackets(brackets)
    if not validate_proper_brackets(u):
        new_brackets = '(' + converse_to_proper(v) + ')'
        reversed_brackets = reverse_brackets(u[1: len(u) - 1])
        return new_brackets + reversed_brackets
    else:
        return u + converse_to_proper(v)


def split_balanced_brackets(brackets):
    left, right = 0, 0
    for idx, bracket in enumerate(brackets):
        if bracket == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return brackets[:idx + 1], brackets[idx + 1:]


def validate_proper_brackets(brackets):
    proper = 0
    for bracket in brackets:
        if bracket == "(":
            proper += 1
        else:
            proper -= 1
        if proper < 0:
            return False
    if proper == 0:
        return True
    return False


def reverse_brackets(brackets):
    reversed_brackets = ''
    for bracket in brackets:
        if bracket == '(':
            reversed_brackets += ')'
        else:
            reversed_brackets += '('
    return reversed_brackets


solution("()))((()")
