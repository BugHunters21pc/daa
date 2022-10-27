# Floyd Warshall Algorithm in python
import copy

# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance=copy.deepcopy(G)

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)

print(G)

#method 2
INF = 999999999
v = 4

def shortestpath(graph,v):
    g = graph
    for k in range(v):
        for i in range(v):
            for j in range(v):
                g[i][j] = min(g[i][j],g[i][k]+g[k][j])
    return g



graph = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]

path = shortestpath(graph ,v)


for i in range(v):
    for j in range(v):
        if path[i][j]==INF:
            print('inf',end=' ')
        else:
            print(path[i][j],end=' ')
   
    if j==v-1:
        print()
