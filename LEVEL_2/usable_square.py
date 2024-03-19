import math


def solution(w, h):
    if w > h:
        w, h = switch(w, h
                      )
    repeat = math.gcd(w, h)
    repeat_x, repeat_y = int(w / repeat), int(h / repeat)
    partial_usable = 0
    print(repeat_x)
    inclination = h / w
    for x in range(repeat_x):
        partial_usable += math.floor(inclination * x)
    unusable = repeat_x * repeat_y - partial_usable * 2
    answer = w * h - unusable * repeat
    print(answer)
    return answer


def switch(w, h):
    return h, w


solution(99998449, 99998473)
