from os import *
from sys import *
from collections import *
from math import *


def BFS(vertex, edges):
    # Write your solution here
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph 
    
    bfs_nodes = list()
    visited = [False] * vertex
    Q = list()
    adj_lists = [None] * vertex
    
    for i in range(len(edges[0])):
        # edges contains two lists
        # first list contains the origin vertices of the edges
        # second list contains the destination vertices of the edges
        u, v = edges[0][i], edges[1][i]
        if adj_lists[u] is None:
            adj_lists[u] = list()
        adj_lists[u].append(v)
    
    for i in range(vertex):
        if adj_lists[i] is None:
            adj_lists[i] = list()

    Q.append(0)
    visited[0] = True
    
    while len(Q) > 0:
        currentNode = Q.pop(0)
        bfs_nodes.append(currentNode)
        for v in adj_lists[currentNode]:
            if not visited[v]:
                Q.append(v)
                visited[v] = True
    
    return bfs_nodes