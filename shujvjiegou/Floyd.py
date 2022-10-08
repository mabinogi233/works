def Floyd(g):  # 多源最短路径Floyd算法
    def DispApath(A, path, k):  # 输出A[k]和path[k]
        print('开始输出A', k)
        for i in range(len(g)):
            print(A[i])
        print('开始输出path[k]')
        for i in range(len(g)):
            print(path[i])
        print('输出完成')

    def DispAllPath(g, A, path):  # 输出所有的最短路径和长度
        apath = [-1 for j in range(g)]  # 存放一条最短路径的中间顶点
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
