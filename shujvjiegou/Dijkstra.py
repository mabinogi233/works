
def Dijkstra(g,v):  #单源最短路径算法，（动态规划）v为原点，g为图的邻接矩阵
    def Dispdistpath(dist, path):
        print(dist)
        print(path)

    def DispAllPath(g, dist, path, S, v):  # 输出从顶点v出发的所以最短路径
        k = 0
        apath = [0] * len(g)  # 存放最短路径的逆，和其顶点个数
        for i in range(len(g)):  # 循环输出从顶点v到i的路径
            if S[i] == 1 and i != v:
                print('从 ', v, ' 到 ', i, ' 的最短路径长度为 ', dist[i])
            d = 0
            apath[d] = i  # 添加路径上的终点
            k = path[i]
            if k == -1:  # 无路径
                print('无路径')
            else:  # 有路径
                while k != v:
                    d += 1
                    apath[d] = k
                    k = path[k]
                d += 1
                apath[d] = v  # 添加路径上的起点
                print('路径为', apath[d])  # 输出路径的起点
                for j in range(d - 1, -1, -1):  # 输出路径的其他顶点
                    print(apath[j])

    dist=[0]*len(g)
    path=[0]*len(g)
    S=[0]*len(g)
    mindis=0
    u=0
    for i in range(len(g)):
        dist[i]=g[v][i]     #距离初始化
        S[i]=0              #S[]置为空
        if g[v][i]<float('inf'):    #路径初始化
            path[i]=v       #顶点v到i有边时，置i的前一个顶点为v
        else:
            path[i]=-1      #顶点v到顶点i没有边时，置顶点i的前一个顶点为-1
    Dispdistpath(dist,path,len(g))#输出dist和path数组，便于调试
    S[v]=1                      #原点编号v放入S
    for i in range(len(g)-1):   #循环向S中添加S-1个顶点
        mindis=float('inf')
        for j in range(len(g)):#选取不在S中且具有最小距离的顶点u
            if S[j]==0 and dist[j]<mindis:
                u=j
                mindis=dist[j]
        print('将顶点加入S中 ',u)
        S[u]=1  #将u加入s中
        for j in range(len(g)): #修改不在s中的顶点的距离
            if S[j]==0 :
                if g[u][j]<float('inf') and dist[u]+g[u][j]<dist[j]:
                    dist[j]=dist[u]+g[u][j]
                    path[j]=u
        Dispdistpath(dist,path) #便于调试
    DispAllPath(g,dist,path,S,v)    #输出所以最短路径和长度






