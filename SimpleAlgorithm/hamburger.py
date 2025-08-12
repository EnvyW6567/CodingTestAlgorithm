#https://school.programmers.co.kr/learn/courses/30/lessons/133502
def made(ingredientStack):
    for _ in range(4):
        ingredientStack.pop()
    return ingredientStack


def solution(ingredient):

    answer = 0
    ingredientStack = []
    isBurger = []
    for i in ingredient:
        ingredientStack.append(i)
        while len(ingredientStack) > 3:
            if ingredientStack[len(ingredientStack)-4:] == [1, 2, 3, 1]:
                answer += 1
                ingredientStack = made(ingredientStack)
            else: break

    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))