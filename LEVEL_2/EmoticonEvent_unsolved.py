# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product
import math
possiblePrice = []

def solution(users, emoticons):
    answer = []
    potentialPlusUsers = []
    minSale = {}
    discounts = [10, 20, 30, 40, 100]
    # 잠재적인 플러스 사용자 구분
    emoticonPriceSum = sum(emoticons)
    for user in users:
        sale, price = user
        if emoticonPriceSum * (100 - int(math.ceil(sale/10) * 10))/100 >= price:
            potentialPlusUsers.append(user)
    
    for combination in product(discounts, repeat=len(emoticons)):
        possiblePrice = int(sum(price * (100 - discount)/100 for price, discount in zip(emoticons, combination)))
        minSale[possiblePrice] = min(combination)
        
    max = 0 
    for possiblePrice in minSale.keys():
        count = 0
        for user in potentialPlusUsers:
            sale, price = user
            if minSale[possiblePrice] >= sale and possiblePrice >= price:
                count += 1
                print(user, minSale[possiblePrice], possiblePrice)
        if max < count:
            max = count
        print("-----------------")
    print(max)
    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)