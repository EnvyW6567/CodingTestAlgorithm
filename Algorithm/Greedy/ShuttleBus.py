from collections import defaultdict, deque


def solution(n, t, m, timetable):
    # n : 셔틀 운행 횟수 , t : 셔틀 운행 간격, m : 셔틀 내 수용인원
    time = []
    for i in timetable:
        hour, minute = map(int, i.split(':'))
        time.append(hour*60+minute)
    time.sort()

    q = deque(time)
    bus = defaultdict(list)

    for i in range(n):
        bustime = 540+t*i
        buscount = 0
        while len(q) > 0 and q[0] <= bustime and m > buscount:
            bus[i].append(q.popleft())
            buscount += 1

    if len(bus[n-1]) == m:  # 마지막 버스에 사람이 꽉 차있을 때
        answer = max(bus[n-1]) - 1
    elif len(bus[n-1]) >= 0:  # 마지막 버스에 사람이 다 안찼을 때
        answer = 540+t*(n-1)
    hour = format(answer//60, '02')
    minute = format(answer % 60, '02')
    ans = str(hour) + ":" + str(minute)
    print(ans)
    return ans


n = 3
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03", "08:02",
             "08:03", "08:02", "08:03", "08:02", "08:03", "08:02", "08:03", "08:12", "08:13", "08:14", "08:15", "08:19", "08:19"]
solution(n, t, m, timetable)
