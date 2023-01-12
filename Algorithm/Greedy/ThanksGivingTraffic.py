def solution(lines):
    t = []
    answer = 0
    # count = [1 for _ in range(len(lines))]
    for idx, traffic in enumerate(lines):
        start, end = timeSlice(traffic)
        t.append([start, end])
    for idx, k in enumerate(t):
        count = 1
        for j in range(idx+1, len(t)):
            # 시작 지점이 안에 있을 경우
            if k[1] > t[j][0]-1000:
                count += 1
            # 시작 지점이 더 작고 끝나는 지점이 더 클 때
            # elif k[0] >= t[j][0] and k[1] <= t[j][1]:
            #     count[j] += 1
        answer = max(answer, count)
    return(answer)


def timeSlice(traffic):
    traffic = traffic.split(' ')
    time = list(map(float, traffic[1].split(':')))
    proc = float(traffic[2].strip('s'))
    end = (time[0]*3600 + time[1]*60 + time[2])*1000
    start = end - proc*1000 + 1

    return start, end
