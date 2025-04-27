# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math
from collections import defaultdict


def solution(fees, records):
    cars = {}
    cars_time = defaultdict(int)

    for record in records:
        time_str, car_num_str, in_out = record.split()
        hour, minute = map(int, time_str.split(":"))
        car_num = int(car_num_str)

        time = hour * 60 + minute

        if in_out == "IN":
            cars[car_num] = [True, time]
        else:
            cars_time[car_num] += time - cars[car_num][1]
            cars[car_num] = [False, 0]

    car_nums = list(cars.keys())
    car_nums.sort()

    base_time, base_fee, unit_time, unit_fee = fees

    answer = []
    for car_num in car_nums:
        is_in, in_time = cars[car_num]
        time = cars_time[car_num]

        if is_in:
            time += 23 * 60 + 59 - in_time

        if time <= base_time:
            answer.append(base_fee)

        else:
            fee = math.ceil((time - base_time) / unit_time) * unit_fee + base_fee
            answer.append(fee)

    return answer
