from numpy import *

INFINITY = 65535                        #代表无穷大
vexs = array([[0,10,INFINITY,INFINITY,INFINITY,11,INFINITY,INFINITY,INFINITY],#邻接矩阵
        [10,0,18,INFINITY,INFINITY,INFINITY,16,INFINITY,12],
        [INFINITY,18,0,22,INFINITY,INFINITY,INFINITY,INFINITY,8],
        [INFINITY,INFINITY,22,0,20,INFINITY,INFINITY,16,21],
        [INFINITY,INFINITY,INFINITY,20,0,26,INFINITY,7,INFINITY],
        [11,INFINITY,INFINITY,INFINITY,26,0,17,INFINITY,INFINITY],
        [INFINITY,16,INFINITY,24,INFINITY,17,0,19,INFINITY],
        [INFINITY,INFINITY,INFINITY,16,7,INFINITY,19,0,INFINITY],
        [INFINITY,12,8,21,INFINITY,INFINITY,INFINITY,INFINITY,0]])

lengthVex = len(vexs)                   #邻接矩阵大小
beginEdge = []
endEdge = []
weight = []
group = []
for i in arange(lengthVex):             #生成边集数组
    group.append([i])
    for j in arange(i+1,lengthVex):
        if(vexs[i, j]>0 and vexs[i, j]<INFINITY):
            beginEdge.append(i)         #每条边的起点
            endEdge.append(j)           #每条边的终点
            weight.append(vexs[i, j])   #每条边的权值

m=0
n=0
lengthEdge = len(weight)                #边的条数
sum = 0
for i in arange(lengthEdge):            #遍历每条边
    I = (argsort(weight))[0]
    for j in arange(lengthVex):
        if(beginEdge[I]) in group[j]:
            m = j
        if(endEdge[I]) in group[j]:
            n = j
    if m != n:                          #判断当前这条边是否属于不同的连通分量，如果是，将其合并
        group[m] = group[m] + group[n]
        group[n] = []
        sum = sum + weight[I]
        print('边 ',beginEdge[I],' ',endEdge[I],' 权值为 ',weight[I])
    del weight[I]                       #删除遍历过的边以及顶点
    del beginEdge[I]
    del endEdge[I]
print("The length of the minimum cost spanning tree is: ",sum)


