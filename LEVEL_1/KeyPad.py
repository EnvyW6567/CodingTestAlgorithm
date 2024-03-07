def solution(numbers, hand):
    pad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1],
           6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1], 10: [3, 0], 11: [3, 2]}
    fin = []
    cur_l = 10
    cur_r = 11
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            cur_l = i
            fin.append('L')
        elif i == 3 or i == 6 or i == 9:
            cur_r = i
            fin.append('R')
        else:
            if abs(pad[i][0]-pad[cur_l][0]) + abs(pad[i][1]-pad[cur_l][1]) > abs(pad[i][0]-pad[cur_r][0]) + abs(pad[i][1]-pad[cur_r][1]):
                cur_r = i
                fin.append('R')
            elif abs(pad[i][0]-pad[cur_l][0]) + abs(pad[i][1]-pad[cur_l][1]) < abs(pad[i][0]-pad[cur_r][0]) + abs(pad[i][1]-pad[cur_r][1]):
                cur_l = i
                fin.append('L')
            else:
                if hand == "right":
                    fin.append('R')
                    cur_r = i
                else:
                    fin.append('L')
                    cur_l = i
    answer = ''.join(fin)
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
