Adj={}
def add_edge(Adj,u,v): #Adj is Adj list of graph
    if u not in Adj:
        Adj[u]=[]
        Adj[u].append(v)
    else:Adj[u].append(v)


def remove_edge(Adj,u,v):
    Adj[u].remove(v)

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


add_edge(Adj,'a','b')
add_edge(Adj,'a','d')
add_edge(Adj,'b','a')
add_edge(Adj,'b','c')
add_edge(Adj,'b','e')
add_edge(Adj,'c','b')
add_edge(Adj,'c','e')
add_edge(Adj,'d','a')
add_edge(Adj,'d','e')
add_edge(Adj,'e','b')
add_edge(Adj,'e','c')
add_edge(Adj,'e','d')

# for i in Adj:
#     print(i,Adj[i],sep='-->')


BFS(Adj,'b')
