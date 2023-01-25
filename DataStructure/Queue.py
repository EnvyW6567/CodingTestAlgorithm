class Queue:
    def __init__(self, length):
        self.queue = []

    def enqueue(self, data):
        self.queue[len(self.queue)] = data

    def dequeue(self):
        data = self.queue[0]
        for i in range(len(self.queue)-1):
            self.queue[i] = self.queue[i+1]
        self.queue[len(self.queue)-1] = None
        return data

    def isEmpty(self):
        if len(self.queue) == 0:
            return False
        else:
            return True
