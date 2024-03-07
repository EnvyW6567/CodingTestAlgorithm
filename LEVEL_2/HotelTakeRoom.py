# https://school.programmers.co.kr/learn/courses/30/lessons/155651
import queue

def solution(book_time):
    bookListMinute = bookTimeTransSortedMinute(book_time)
    endTime = queue.PriorityQueue()
    answer = 0
    for book in bookListMinute:
        start, end = book
        while(len(endTime.queue) > 0 and start >= endTime.queue[0]):
            endTime.get()
        endTime.put(end + 10)
        if answer < len(endTime.queue):
            answer = len(endTime.queue)
    print(answer)
    return answer

def bookTimeTransSortedMinute(book_time):
    bookMinute = []
    for bt in book_time:
        start, end = bt
        bookMinute.append([splitHourAndMinute(start), splitHourAndMinute(end)])
        bookMinuteSorted = sorted(bookMinute, key = lambda x: x[0])
    return bookMinuteSorted

    
def splitHourAndMinute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


book_item = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
solution(book_item)