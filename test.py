import Graph

Adj={}

# def add_edge(Adj,u,v): #Adj is Adj list of graph
#     if u not in Adj:
#         Adj[u]=[]
#         Adj[u].append(v)
#     else:Adj[u].append(v)
#
#
# def remove_edge(Adj,u,v):
#     Adj[u].remove(v)
#
# def BFS(Adj,S):
#     color = {}
#     distance = {}
#     parent = {}
#     for u in Adj:
#         color[u] = 'white'
#     distance[S] = 0
#     parent[S]=None
#     queue = [S]
#     while len(queue) != 0:
#         u=queue.pop(0)
#         for v in Adj[u]:
#             if color[v] == 'white':
#                 color[v] = 'grey'
#                 distance[v] = distance[u]+1
#                 parent[v] = u
#                 queue.append(v)
#         color[u] = 'black'
#     print(distance)
#     print(parent)
#     print(color)


Graph.add_edge(Adj,'a','b')
Graph.add_edge(Adj,'a','d')
Graph.add_edge(Adj,'b','a')
Graph.add_edge(Adj,'b','c')
Graph.add_edge(Adj,'b','e')
Graph.add_edge(Adj,'c','b')
Graph.add_edge(Adj,'c','e')
Graph.add_edge(Adj,'d','a')
Graph.add_edge(Adj,'d','e')
Graph.add_edge(Adj,'e','b')
Graph.add_edge(Adj,'e','c')
Graph.add_edge(Adj,'e','d')

Graph.printGraph(Adj)

Graph.BFS(Adj,'c')
