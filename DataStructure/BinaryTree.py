class Node:
    def __init__(self, value=None, value_l=None, value_r=None):
        self.value = value
        self.left = value_l
        self.right = value_r


class BinaryTree:
    def __init__(self):
        self.root = None

    # 트리 삽입 과정
    def push(self, value):
        node = Node(value=value)
        tmp_node = self.root

        if self.root:
            ptr_node = self.root
            while ptr_node:
                tmp_node = ptr_node
                if node.value < ptr_node.value:
                    ptr_node = ptr_node.left
                else:
                    ptr_node = ptr_node.right
            if node.value < tmp_node.value:
                tmp_node.left = node
            else:
                tmp_node.right = node
        else:
            self.root = node
            return

    def remove_node(self, value):
        tmp = self.root
        self.pop(tmp, value)

    # 재귀를 통한 탐색 및 pop 함수
    def pop(self, node, value):
        if node is None:
            return -1
        elif node.value > value:
            node.left = self.pop(node.left, value)
        elif node.value < value:
            node.right = self.pop(node.right, value)
        else:
            tmp = node
            if node.left is None and node.right is None:
                del node
                node = None
            elif node.right is None:
                node = node.left
                del tmp
            elif node.left is None:
                node = node.right
                del tmp
            else:
                tmp = self.searchMaxNode(node.left)
                node.value = tmp.value
                node.left = self.pop(node.left, tmp.value)
        return node
