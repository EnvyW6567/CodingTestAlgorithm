def change(a, b, heap):
    tmp = heap[a]
    heap[a] = heap[b]
    heap[b] = tmp
    return heap

# queue에서 가장 우선순위 요소 return
def peek(heap):
    return heap[0]

# queue에 새로운 요소 추가
def enqueue(heap, input):
    heap.append(input)
    node = len(heap) - 1
    heap = heapify_up(heap, node)

    return heap

# queue에 최상위 요소 삭제 및 return
def dequeue(heap):
    res = heap[0]
    heap[0] = heap.pop()
    heap = heapify_down(heap, 0)

    return res, heap 

# heap의 속성을 유지하는 작업
def heapify_down(heap, node):

    leftN = node * 2 + 1 # 왼쪽 자식 노드
    rightN = node * 2 + 2 # 오른쪽 자식 노드
    heapNode = node
    if leftN < len(heap) and heap[node] < heap[leftN]:
        heapNode = leftN

    if rightN < len(heap) and heap[node] < heap[rightN]:
        heapNode = rightN

    if not heapNode == node:
        heap = change(heapNode, node, heap)
        heap = heapify_down(heap, heapNode)
        return heap
    return heap

def heapify_up(heap, node):

    pNode = int((node-1)/2)
    if heap[pNode] < heap[node]:
        heap = change(pNode, node, heap)
        heap = heapify_up(heap, pNode)
        return heap
    return heap

heap = [4,3,2,1]
print(enqueue(heap, 5))
print(enqueue(heap, 7))
print(enqueue(heap, 6))
print(enqueue(heap, 10))
print(enqueue(heap, 13))
print(enqueue(heap, 11))