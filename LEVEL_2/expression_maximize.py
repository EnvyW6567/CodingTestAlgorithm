# https://school.programmers.co.kr/learn/courses/30/lessons/67257
import re
from itertools import product, permutations


def solution(expression):
    answer = 0
    ops = ['+', '-', '*']
    numbers_list, operators_list = [], []
    tokens = re.findall(r'\d+|\D', expression)
    for token in tokens:
        if token.isdigit():
            numbers_list.append(int(token))
        else:
            operators_list.append(token)

    for ops in list(permutations(ops, 3)):
        numbers = numbers_list[:]
        operators = operators_list[:]
        for op in ops:
            stack = []
            for idx, operator in enumerate(operators):
                if op == operator:
                    result = calculate(operator, numbers[idx], numbers[idx + 1])
                    numbers[idx + 1] = result
                    stack.append(idx)
            for i, idx in enumerate(stack):
                del numbers[idx - i]
                del operators[idx - i]

        if answer < abs(numbers[0]):
            answer = abs(numbers[0])
    print(answer)
    return answer


def calculate(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b


solution("100-200*300-500+20")
