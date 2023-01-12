# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    '''
    하나의 루트를 선택, 다른 루트의 시작지점이
    해당 루트 범위 안에 있으면 삭제 
    sort + queue
    '''
    routes.sort()
    start = []
    end = []
    for i in routes:
        start.append(i[0])
        end.append(i[1])

    count = 0
    for idx, i in enumerate(routes):
        end_idx = i[1]
        try:
            if routes[idx+1][0] < end_idx:
                continue
            else:
                count += 1
        except:
            count += 1
            pass

    print(count)
    return count


routes = [[-100, 100], [10, 20], [30, 40]]
solution(routes)
