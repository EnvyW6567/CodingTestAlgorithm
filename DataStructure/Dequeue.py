import sys


class DeQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.dq = [0 for _ in range(5)]

    def frontEnqueue(self, input):
        if self.isFull():
            print("현재 원형 큐는 포화상태입니다.")
        else:
            self.dq[self.front] = input
            self.front = (self.front-1+len(self.dq)) % len(self.dq)

    def rearEnqueue(self, input):
        if self.isFull():
            print("현재 원형 큐는 포화상태입니다.")
        else:
            self.rear = (self.rear+1) % len(self.dq)
            self.dq[self.rear] = input

    def frontDequeue(self):
        if self.isEmpty():
            print("현재 원형 큐는 비어있습니다.")
        else:
            self.front = (self.front+1) % len(self.dq)
            print(f'{self.dq[self.front]}(이)가 출력되었습니다')

    def rearDequeue(self):
        if self.isEmpty():
            print("현재 원형 큐는 비어있습니다.")
        else:
            print(f'{self.dq[self.rear]}(이)가 출력되었습니다')
            self.rear = (self.rear-1+len(self.dq)) % len(self.dq)

    def isFull(self):
        if (self.rear+1) % len(self.dq) == self.front:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False


q = DeQueue()

while True:
    print('1. Front Pop 2. Front Insert 3. Rear Pop 4. Rear Insert')
    a = int(sys.stdin.readline())
    if a == 1:
        q.frontDequeue()
    elif a == 2:
        b = int(sys.stdin.readline())
        q.frontEnqueue(b)
    elif a == 3:
        q.rearDequeue()
    elif a == 4:
        b = int(sys.stdin.readline())
        q.rearEnqueue(b)
    else:
        print('올바른 값을 입력하세요.')
