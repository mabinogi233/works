

class mapLin():#邻接矩阵描绘图
    def __init__(self,dian,edges):   #建立一个图，dian为点的列表，edges为边的二维列表(数字集)
        self.dian=dian
        self.n=len(self.dian)
        self.edges=edges    #无向图[[1,2],[2,3][3,4]]  有向图[[1,2,5],[2,3,6][3,4,5]] 表示从第一个到第二个的路径
                                                                                        # ，权值为第三个数
    def getvexs(self):#获取点组成的数字集
        vexs=[i for i in range(len(self.dian))]
        return vexs


    def getnum(self,value):#获取值为value的元素的数组序号组成的列表
        j=0
        jieguo=[]
        for i in range(self.n):
            if self.dian[i]==value:
                jieguo.append(i)
                j=1
        if j==0:
            return None
        else:
            return jieguo

    def Findvalue(self,num):#根据数组集的序号获取对应元素
        return self.dian[num]

    def CreateWugrape(self,vexs):#以邻接矩阵描绘这个无向图，vexs为点数，edges为边的关系
        edges=self.edges
        A=[[0 for i in range(len(vexs))]for j in range(len(vexs))]
        for i in range(len(edges)):
            a=edges[i][0]
            b=edges[i][1]
            A[a][b]=1
            A[b][a]=1
        self.A=A
        return A

    def CreateYougrape(self,vexs):#以邻接矩阵描绘这个有向图，vexs为点集，edges为边的关系egdes[2]储存路径权值
        edges=self.edges
        A=[[float('inf') for i in range(self.n)]for j in range(self.n)]
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            A[a][b] = edges[i][2]
            A[b][a] = edges[i][2]               # 用于生成带权无向图
        for i in range(self.n):
            A[i][i]=0
        self.A=A
        return A

    def DispGraph(self):#打印这个邻接矩阵A
        for i in range(self.n):
            print(self.A[i])

    def AddaVex(self,value):#将值为value的点加入图,添加后需要重新绘制图
        self.dian.append(value)
        self.n+=1

    def InsertWuEdge(self,bian):#对无向图中加入一条边 eg:[1,2],添加后需要重新绘制图
        self.edges.append(bian)

    def InsertYouEdges(self,bian):    #对有向图中加入一条边 eg:[1,2,6],添加后需要重新绘制图
        self.edges.append(bian)

    def DegreeWu(self,v):#找无向图中数组序号为v的点的度
        sum_1=sum(self.A[v])
        return sum_1

    def DegreeYou(self,v):#找有向图中数组序号为v的点的度
        ru=0
        chu=0
        for i in range(self.n):
            if self.A[v][i]!=0 and self.A[v][i]!=float('inf'):
                chu+=1
        for i in range(self.n):
            if self.A[i][v]!=0 and self.A[v][i]!=float('inf'):
                ru+=1
        return ru+chu

dian=[1,2,3,4,5]
edges=[[0,1,1],[0,3,2],[1,3,4],[1,2,3],[2,4,6],[3,4,7]]
map=mapLin(dian,edges)
map.AddaVex(6)
map.InsertYouEdges([2,5,10])
map.CreateYougrape(map.getvexs())


def Floyd(g):  # 多源最短路径Floyd算法
    def DispApath(A, path, k):  # 输出A[k]和path[k]
        print('开始输出A', k)
        for i in range(len(g)):
            print(A[i])
        print('开始输出path',k)
        for i in range(len(g)):
            print(path[i])
        print('输出完成')

    def DispAllPath(g, A, path):  # 输出所有的最短路径和长度
        apath = [-1 for j in range(len(g))]  # 存放一条最短路径的中间顶点
        d = 0  # 存放其顶点个数
        for i in range(len(g)):
            for j in range(len(g)):
                if A[i][j] != float('inf') and i != j:
                    print('顶点 ', i, ' 到 ', j, ' 的最短路径长度为 ', A[i][j])
                    k = path[i][j]  # 添加终点
                    d = 0
                    apath[d] = j
                    while k != -1 and k != i:  # 添加中间点
                        d += 1
                        apath[d] = k
                        k = path[i][k]
                    d += 1
                    apath[d] = i
                    print(apath[d])  # 输出起点
                    for s in range(d - 1, -1, -1):  # 输出中间点
                        print(apath[s])

    A = [[0 for i in range(len(g))] for j in range(len(g))]
    path = [[0 for i in range(len(g))] for j in range(len(g))]
    for i in range(len(g)):  # 对A和path置初始值（求A（-1）），{A（k）[i][j]}表示从i到j经过编号不大于k的点的最短路径长度
        for j in range(len(g)):
            A[i][j] = g[i][j]
            if i != j and g[i][j] < float('inf'):
                path[i][j] = i  # i和j之间有一条边
            else:
                path[i][j] = -1  # i和j之间没有边

    DispApath(A, path, -1)  # 输出A(-1)便于调试
    for k in range(len(g)):  # 求A(K)[i][j]
        for i in range(len(g)):
            for j in range(len(g)):
                if A[i][j] > A[i][k] + A[k][j]:  # 找到最短路径
                    A[i][j] = A[i][k] + A[k][j]  # 修改最短路径长度
                    path[i][j] = path[k][j]  # 修改最短路径为经过顶点k
        DispApath(A, path, k)  # 输出A和path便于调试
    DispAllPath(g, A, path)  # 输出最短路径和长度


Floyd(map.A)