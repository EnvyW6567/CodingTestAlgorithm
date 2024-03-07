# https://school.programmers.co.kr/learn/courses/30/lessons/258711
from collections import defaultdict

def solution(edges):
    stickGraph = []
    eightGraph = []
    addedNode = None

    graph, destEdgeCount, existNode = toGraph(edges)

    graph, destEdgeCount, existNode, addedNode = findAddedNodeAndUpdateGraph(graph, destEdgeCount, existNode)
    stickGraph, eightGraph = findStickAndEightGraph(existNode, destEdgeCount)
    answer = [addedNode, 0, len(stickGraph), len(eightGraph)]

    for startNode in stickGraph:
        graph = graphCircuit(graph, startNode)

    for startNode in eightGraph:
        graph = graphCircuit(graph, startNode)

    while(len(graph.keys()) != 0):
        answer[1] += 1
        startNode, _ = next(iter(graph.items()))
        graph = graphCircuit(graph, startNode)

    return answer

def toGraph(edges):
    graph = defaultdict(list)
    destEdgeCount = defaultdict(int)
    existNode = set()

    for edge in edges:
        start, destination = edge
        existNode.add(start)
        existNode.add(destination)
        graph[start].append(destination)
        destEdgeCount[destination] += 1

    return graph, destEdgeCount, existNode

def graphCircuit(graph, startNode):
    while(startNode in graph):
        nextNode = graph[startNode].pop()
        if (len(graph[startNode]) == 0):
            del graph[startNode]
        startNode = nextNode

    return graph

def findAddedNodeAndUpdateGraph(graph, destEdgeCount, existNode): 
    for key in graph.keys():
        if destEdgeCount[key] == 0:
            if len(graph[key]) > 1:
                addedNode = key

    for destNode in graph[addedNode]:
        destEdgeCount[destNode] -= 1
    
    del graph[addedNode]
    existNode.discard(addedNode)

    return graph, destEdgeCount, existNode, addedNode

def findStickAndEightGraph(existNode, destEdgeCount):
    stickGraph = []
    eightGraph = []

    for node in existNode:
        if destEdgeCount[node] == 2:
            eightGraph.append(node)
        elif destEdgeCount[node] == 0:
            stickGraph.append(node)

    return stickGraph, eightGraph

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8], [2, 13], [13, 2]]
solution(edges)