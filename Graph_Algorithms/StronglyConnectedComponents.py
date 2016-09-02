#Strongly Connected Components

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

