import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    # 신규 노드 생성
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def getDataIndex(self, data):
        idx = 0
        curNode = self.head
        while curNode:
            if curNode.data == data:
                return idx
            idx += 1
            curNode = curNode.next
        return None

    def insertNodeAtIndex(self, idx, node):
        curNode = self.head
        curIdx = 0
        prevNode = None

        # 리스트 맨 앞에 추가할 경우
        if idx == 0:
            if self.head:
                nextNode = self.head
                self.head = node
                self.head.next = nextNode
            else:
                self.head = node

        # 주어진 idx에 추가할 경우
        else:
            while curIdx < idx:
                if curNode:
                    prevNode = curNode
                    curNode = curNode.next
                else:
                    break
                curIdx += 1
            if curIdx == idx:
                node.next = curNode
                prevNode.next = node
            else:
                return -1

    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            return -1

    def deleteAtIndex(self, idx):
        curIdx = 0
        curNode = self.head
        prevNode = None
        nextNode = self.head.next
        if idx == 0:
            self.head = nextNode
        else:
            while curIdx < idx:
                if curNode.next:
                    prevNode = curNode
                    curNode = curNode.nextNode
                    nextNode = nextNode.next
                else:
                    break
                curIdx += 1
            if curIdx == idx:
                prevNode.next = nextNode
            else:
                return -1

    def clear(self):
        self.head = None

    def print(self):
        curNode = self.head
        dataStr = ""
        while curNode:
            string += str(curNode.data)
            if curNode:
                string += " => "
            curNode = curNode.next
        print(dataStr)
