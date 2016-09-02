"""
 All Graph Algorithms at one place
"""

class Graph:
    pass

def add_edge(Adj,u,v): #Adj is Adj list of graph
    if u not in Adj:
        Adj[u]=[]
        Adj[u].append(v)
    else:Adj[u].append(v)

def remove_edge(Adj,u,v):
    Adj[u].remove(v)

def printGraph(Adj):
    for i in Adj:
        print(i,Adj[i],sep='-->')

def BFS(Adj,S):
    color = {}
    distance = {}
    parent = {}
    for u in Adj:
        color[u] = 'white'
    distance[S] = 0
    parent[S]=None
    queue = [S]
    while len(queue) != 0:
        u=queue.pop(0)
        for v in Adj[u]:
            if color[v] == 'white':
                color[v] = 'grey'
                distance[v] = distance[u]+1
                parent[v] = u
                queue.append(v)
        color[u] = 'black'
    print(distance)
    print(parent)
    print(color)

color = {}
parent = {}
def DFS(Adj):

    for u in Adj:
        color[u] = 'white'
        parent[u]=None
    for u in Adj:
        if color[u] == 'white':
            DFS_VISIT(Adj,u)
    print(parent)
    print(color)

def DFS_VISIT(Adj,u):
    color[u]='grey'
    for v in Adj[u]:
        if color[v] == 'white':
            color[v]='grey'
            parent[v]=u
            DFS_VISIT(Adj,v)
    color[u]='black'


def Transpose(Adj):
    Trans_Adj={}
    for i in Adj:
        Trans_Adj[i]=[]

    for i in Adj:
        for j in Adj[i]:
            Trans_Adj[j].append(i)

    return Trans_Adj
