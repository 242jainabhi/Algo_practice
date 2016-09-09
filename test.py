'''import sys
sys.setrecursionlimit(10000000)'''

class Graph:
    def __init__(self):
        self.Adj = {}
        self.visited = {}   
        self.count = 0
        self.parent = {}
        self.stack=[]
        self.No_of_Nodes={}

    def add_edge(self,u,v):
        """Adds edge to the graph"""
        if u not in self.Adj:
            self.Adj[u]=set()
            self.Adj[u].add(v)
        else: self.Adj[u].add(v)


    def printGraph(self):
        """Prints the Adjacency List representation of the graph"""
        for i in self.Adj:
            print(i,self.Adj[i],sep='-->')


    def Transpose(self):
        """Transpose of a Graph (Adjacency list Representation)"""
        g=Graph()
        for i in self.Adj:
            g.Adj[i]=[]

        for i in self.Adj:
            for j in self.Adj[i]:
                if j in g.Adj:
                    g.Adj[j].append(i)
                else:
                    g.Adj[j]=[]
                    g.Adj[j].append(i)
        return g

    def Order_Nodes(self,u):
        self.visited[u] = True
        for v in self.Adj[u]:
            if self.visited[v] == False:
                self.Order_Nodes(v)
        self.stack.insert(0,u)

    def DFS_VISIT(self,s,u):
        self.visited[u] = True
        for v in self.Adj[u]:
            if self.visited[v] == False:
                self.No_of_Nodes[s] += 1
                self.DFS_VISIT(s,v)

    
f=open('SCC.txt','r')
arr=f.readlines()
G=Graph()
vertices=set()

for i in arr:
    u,v=tuple(i.strip().split())
    vertices.add(u)
    vertices.add(v)
    
for i in vertices:
    G.Adj[i]=set()

for i in arr:
    u,v=tuple(i.strip().split())
    G.add_edge(u,v)

#print(G.printGraph())
#print('\nTranspose')
GT=G.Transpose()
#print(GT.printGraph())

#DFS on G_Transpose
for i in GT.Adj:
    GT.visited[i] = False

for i in GT.Adj:
    if GT.visited[i] == False:
        GT.Order_Nodes(i)

#print(GT.stack)

for i in G.Adj:
    G.visited[i] = False
    
for i in GT.stack:
    if G.visited[i] == False:
        G.No_of_Nodes[i] = 1
        G.DFS_VISIT(i,i)
        G.count += 1

print("The no. of SCC: ",G.count)
for i in G.No_of_Nodes:
    print(i,G.No_of_Nodes[i],sep=':')
