def solution(word):
    answer = 0
    vowels = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U'}
    stack = []

    while True:
        if ''.join(stack) == word:
            return answer

        if len(stack) < 5:
            stack.append('A')
        else:
            while stack[-1] == 'U':
                stack.pop()
            stack[len(stack) - 1] = vowels[stack[-1]]
        answer += 1


print(solution("AAAAE"))
