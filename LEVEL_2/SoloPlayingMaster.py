# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):
    cardGraph = {}
    visited = {}
    groupSize = [0]
    for boxNum, cardNum in enumerate(cards):
        cardGraph[boxNum + 1] = cardNum

    print(cardGraph)    
    while(len(cardGraph.keys()) > 0):
        boxNum, cardNum = cardGraph.popitem()
        count = 1
        while(cardNum in cardGraph):
            nextCardNum = cardGraph[cardNum]
            del cardGraph[cardNum]
            cardNum = nextCardNum
            count += 1
        groupSize.append(count)
    
    sortedGroupSize = sorted(groupSize, reverse = True)
    print(sortedGroupSize[0] * sortedGroupSize[1])
    return sortedGroupSize[0] * sortedGroupSize[1]
    

cards = [8,6,3,7,2,5,1,4]
solution(cards)