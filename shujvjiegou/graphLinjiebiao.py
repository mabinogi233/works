import collections  #引入集合
import queue

g = collections.OrderedDict()   #类似图的邻接表表示(也可以用字典表示)
g['A'] = ['B', 'C', 'D']
g['B'] = ['A', 'E']
g['C'] = ['A', 'F']
g['D'] = ['A', 'G', 'H']
g['E'] = ['B', 'F']
g['F'] = ['E', 'C']
g['G'] = ['D', 'H', 'I']
g['H'] = ['G', 'D']
g['I'] = ['G']

def DFSTraverse(g): #深度优先遍历
    visited = {}

    def DFS(v):
        print(v)
        visited[v] = True

        for adj in g[v]:
            if not visited.get(adj):
                DFS(adj)

    for v in g:
        if not visited.get(v):
            DFS(v)



def BFSTraverse(g): #广度优先遍历
    visited = {}
    q = queue.Queue()

    for v in g:
        if not visited.get(v):
            print(v)
            visited[v] = True  # 先访问再入队
            q.put(v)

        while not q.empty():
            e = q.get()

            for adj in g[e]:
                if not visited.get(adj):
                    print(adj)
                    visited[adj] = True
                    q.put(adj)





