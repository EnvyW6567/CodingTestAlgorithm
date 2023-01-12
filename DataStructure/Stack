class Stack:
    def __init__(self, size):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            data = self.stack[len(self.stack)-1]
            self.stack[len(self.stack)-1] = None
            return data

    # top은 삭제 없이 데이터 접근
    def top(self):
        if self.isEmpty():
            data = self.stack[len(self.stack)-1]
            return data

    def push(self, data):
        self.stack[len(self.stack)] = data

    def isEmpty(self):
        if len(self.stack) == 0:
            print("스택이 비어있습니다.")
            return False
        else:
            return True


.
