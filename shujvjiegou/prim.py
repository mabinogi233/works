def prim(g,v):#带权无向图以v为根的最小生成树（prim算法）
    lowcost=[]
    closest=[]
    min=0
    k=0
    for i in range(len(g)):#对两个列表赋予初始值
        lowcost[i]=g[v][i]
        closest[i]=v
    for i in range(len(g)):#构造n-1条边，n为顶点数
        min=float('inf')
        k=-1
        for j in range(len(g)):     #在V-U中找出距离V最近的顶点k
            if lowcost[j]!=0 and lowcost[j]<min:
                min=lowcost[j]
                k=j
        print('边 ',closest[k] ,'',k,' 权值为 ',min)
        lowcost[k]=0#k已加入U
        for j in range(len(g)):#修正两个数组
            if g[k][j]!=0 and g[k][j]<lowcost[j]:
                lowcost[j]=g[k][j]
                closest[j]=k

