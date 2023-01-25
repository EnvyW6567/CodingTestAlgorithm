import sys


class circleQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.cq = [0 for _ in range(5)]

    def enqueue(self, input):
        if self.isFull():
            print("현재 원형 큐는 포화상태입니다.")
        else:
            self.rear = (self.rear+1) % len(self.cq)
            self.cq[self.rear] = input

    def dequeue(self):
        if self.isEmpty():
            print("현재 원형 큐는 비어있습니다.")
        else:
            self.front = (self.front+1) % len(self.cq)
            print(f'{self.cq[self.front]}(이)가 출력되었습니다')

    def isFsull(self):
        if (self.rear+1) % len(self.cq) == self.front:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False


q = circleQueue()

while True:
    print("1. 삽입 2. 출력 3. 종료")
    a = int(sys.stdin.readline())
    if a == 1:
        qi = int(sys.stdin.readline())
        q.enqueue(qi)
    elif a == 2:
        q.dequeue()
    elif a == 3:
        break
    else:
        print('올바른 값을 입력하세요.')
