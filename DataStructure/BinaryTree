class Node:
    def __init__(self, value=None, valueL=None, valueR=None):
        self.value = value
        self.left = valueL
        self.right = valueR


class BinaryTree:
    def __init__(self):
        self.root = None

    # 트리 삽입 과정
    def push(self, value):
        node = Node(value=value)
        tmpNode = self.root

        if self.root:
            ptrNode = self.root
            while ptrNode:
                tmpNode = ptrNode
                if node.value < ptrNode.value:
                    ptrNode = ptrNode.left
                else:
                    ptrNode = ptrNode.right
            if node.value < tmpNode.value:
                tmpNode.left = node
            else:
                tmpNode.right = node
        else:
            self.root = node
            return

    def removeNode(self, value):
        tmp = self.root
        self.pop(tmp, value)

    # 재귀를 통한 탐색 및 pop 함수
    def pop(self, node, value):
        if node == None:
            return -1
        elif node.value > value:
            node.left = self.pop(node.left, value)
        elif node.value < value:
            node.right = self.pop(node.right, value)
        else:
            tmp = node
            if node.left == None and node.right == None:
                del node
                node = None
            elif node.right == None:
                node = node.left
                del tmp
            elif node.left == None:
                node = node.right
                del tmp
            else:
                tmp = self.searchMaxNode(node.left)
                node.value = tmp.value
                node.left = self.pop(node.left, tmp.value)
        return node
