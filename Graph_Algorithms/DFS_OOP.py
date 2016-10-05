class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.Adj = {}
        self.time = 0
        self.color = {}
        self.distance = {}
        self.parent = {}
        self.queue = []
        self.visit_time = {}
        self.finish_time = {}

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


    def DFS(self):
        """Depth First Search of a graph """
        for u in self.Adj:
            self.color[u] = 'white'
            self.parent[u]=None
        for u in self.Adj:
            if self.color[u] == 'white':
                self.DFS_VISIT(u)
                # print(self.color)
        print(self.parent)
        print(self.color)
        print(self.visit_time)
        print(self.finish_time)

    def DFS_VISIT(self,u):
        self.time += 1
        self.color[u]='grey'
        self.visit_time[u]=self.time
        for v in self.Adj[u]:
            if self.color[v] == 'white':
                self.color[v]='grey'
                self.parent[v]=u
                self.DFS_VISIT(v)
        self.color[u]='black'
        self.time += 1
        self.finish_time[u]=self.time


f=open('Console_Input.txt','r')

q=int(f.readline().strip())
for _ in range(q):
    n,m=tuple(map(int,f.readline().strip().split()))
    G=Graph(n,m)
    for i in range(m):
        u,v=tuple(f.readline().strip().split())
        G.add_edge(u,v)

    # s=f.readline().strip()
    G.printGraph()
    G.DFS()
f.close()


"""
Example DFS:

u-->['v', 'x']
w-->['y', 'z']
x-->['v']
v-->['y']
z-->['z']
y-->['x']
{'u': None, 'w': None, 'v': 'u', 'x': 'y', 'y': 'v', 'z': 'w'}
{'u': 'black', 'w': 'black', 'v': 'black', 'x': 'black', 'y': 'black', 'z': 'black'}
{'u': 1, 'w': 9, 'x': 4, 'v': 2, 'z': 10, 'y': 3}
{'u': 8, 'w': 12, 'v': 7, 'x': 5, 'z': 11, 'y': 6}
"""
