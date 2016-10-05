class Graph:
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.Adj={}
        self.color = {}
        self.distance = {}
        self.parent = {}
        self.queue=[]

    def add_edge(self,u,v):
        """Adds edge to the graph"""
        if u not in self.Adj:
            self.Adj[u]=[]
            self.Adj[u].append(v)
        else: self.Adj[u].append(v)

    def remove_edge(self,u,v):
        """Remoces edge from the graph"""
        self.Adj[u].remove(v)

    def printGraph(self):
        """Prints the Adjacency List representation of the graph"""
        for i in self.Adj:
            print(i,self.Adj[i],sep='-->')

    def BFS(self,S):
        """Breadth first Search of a Graph"""
        for u in self.Adj:
            self.color[u] = 'white'

        self.distance[S] = 0
        self.parent[S]=None
        self.queue = [S]
        while len(self.queue) != 0:
            u=self.queue.pop(0)
            for v in self.Adj[u]:
                if self.color[v] == 'white':
                    self.color[v] = 'grey'
                    self.distance[v] = self.distance[u]+1
                    self.parent[v] = u
                    self.queue.append(v)
            self.color[u] = 'black'
        print(self.distance)
        print(self.parent)
        print(self.color)

    def DFS(self):
        """Depth First Search of a graph """
        for u in self.Adj:
            self.color[u] = 'white'
            self.parent[u]=None
        for u in self.Adj:
            if self.color[u] == 'white':
                self.DFS_VISIT(u)
        print(self.parent)
        print(self.color)

    def DFS_VISIT(self,u):
        self.color[u]='grey'
        for v in self.Adj[u]:
            if self.color[v] == 'white':
                self.color[v]='grey'
                self.parent[v]=u
                self.DFS_VISIT(v)
        self.color[u]='black'


f=open('Console_Input.txt','r')

q=int(f.readline().strip())
for _ in range(q):
    n,m=tuple(map(int,f.readline().strip().split()))
    # n,m=list(map(int,input().split()))
    G=Graph(n,m)
    for i in range(m):
        u,v=tuple(f.readline().strip().split())
        G.add_edge(u,v)
        G.add_edge(v,u)

    s=f.readline().strip()
    G.BFS(s)
    G.printGraph()
    # G.DFS()
f.close()
