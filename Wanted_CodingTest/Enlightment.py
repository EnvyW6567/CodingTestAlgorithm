import sys

N = sys.stdin.readline()

stone = list(map(int, sys.stdin.readline().split()))
maxL = 0
curL = 0
for dir in stone: # left
    if dir == 1:
        curL += 1
    else:
        if curL > 0:
            curL -= 1

    if maxL < curL:
        maxL = curL
maxR = 0
curR = 0
for dir in stone: # right
    if dir == 2:
        curR += 1
    else:
        if curR > 0:
            curR -= 1

    if maxR < curR:
        maxR = curR
if maxR > maxL:
    print(maxR) 
else:
    print(maxL)