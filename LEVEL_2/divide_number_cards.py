# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math


def solution(arrayA, arrayB):
    gcd_A = get_gcd(arrayA)
    gcd_B = get_gcd(arrayB)
    if gcd_A == 1 and gcd_B == 1:
        return 0
    else:
        answer = 0
        if gcd_A > 1:
            if validate(arrayB, gcd_A):
                answer = gcd_A
        if gcd_B > 1:
            if validate(arrayA, gcd_B) and answer < gcd_B:
                answer = gcd_B

    print(gcd_A, gcd_B, answer)
    return answer


def get_gcd(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd


def validate(arr, gcd):
    for num in arr:
        if num % gcd == 0:
            return False
    return True


solution([10, 20], [13, 17])
