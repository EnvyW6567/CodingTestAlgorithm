import sys
import random


def randomize(iter):
    r = [i for i in range(iter)]
    for i in range(iter):
        k = random.randint(0, iter-1)
        tmp = r[i]
        r[i] = r[k]
        r[k] = tmp
    return r


randomArr = randomize(100)
# 배열
print("찾을 숫자를 입력하세요 (0~99) : ", end='')
b = int(sys.stdin.readline())
for i in range(100):
    if randomArr[i] == b:
        print(f'{i} 번 째에 있습니다')
        break
