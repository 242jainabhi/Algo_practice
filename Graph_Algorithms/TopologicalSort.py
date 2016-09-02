topology=[]
color={}
parent={}
Adj={'under':['pants','shoes'],
     'pants':['shoes','belt'],
     'belt':['jacket'],
     'shirt':['belt','tie'],
     'tie':['jacket'],
     'socks':['shoes'],
     'watch':[],
     'jacket':[],
     'shoes':[]
}

def DFS(Adj):
    for u in Adj:
        color[u] = 'white'
        parent[u]=None
    for u in Adj:
        if color[u] == 'white':
            DFS_VISIT(Adj,u)
    print(parent)
    print(color)
    return topology


def DFS_VISIT(Adj,u):
    color[u]='grey'
    for v in Adj[u]:
        if color[v] == 'white':
            color[v]='grey'
            parent[v]=u
            DFS_VISIT(Adj,v)
    color[u]='black'
    topology.insert(0,u)


print(DFS(Adj))


