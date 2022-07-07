# Author: Meher Kalra
# Date: 10 March 2022
# Purpose: to write the breadth first search function on the graph

from collections import deque

# function with parameters start and goal vertices
def bfs(start, goal):
    frontier = deque()
    backpointer = {}
    frontier.append(start)
    backpointer[start] = None
    while len(frontier) > 0:
        v = frontier.popleft()

        for adj in v.adjacency_list:
            if adj not in backpointer:
                frontier.append(adj)
                backpointer[adj] = v

        if goal in backpointer:
            break

# list of vertices
    path = []
    x = goal

    while x:
        path.append(x)
        x = backpointer[x]

    return path
