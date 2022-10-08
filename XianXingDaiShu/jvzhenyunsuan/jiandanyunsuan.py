
def jvzhenadd(jvzhen_a,jvzhen_b):     #传入两个二维数组，求矩阵的和
    hang_a=len(jvzhen_a)
    hang_b=len(jvzhen_b)
    lie_a=len(jvzhen_a[0])
    lie_b=len(jvzhen_b[0])
    jvzhen_c=[[0 for i in range(lie_a)]for j in range(hang_a)]
    if hang_a !=hang_b or lie_a !=lie_b:
        print('不是同型矩阵不能相加')
    else:
        for i in range(hang_a):
            for j in range(lie_a):
                jvzhen_c[i][j]=jvzhen_a[i][j]+jvzhen_b[i][j]
    return jvzhen_c                                             #返回结果

def jvzhenchengshu(jvzhen_a,shu):   #输入矩阵和要进行乘数的数，进行矩阵的乘数
    jvzhen_c = [[0 for i in range(len(jvzhen_a[0]))] for j in range(len(jvzhen_a))]
    for i in range(len(jvzhen_a)):
        for j in range(len(jvzhen_a[0])):
            jvzhen_c[i][j]=shu * jvzhen_a[i][j]
    return jvzhen_c


def jvzhenchengfa(jvzhen_a,jvzhen_b):   #矩阵乘法
    def hangchenglie(jvzhen_a, jvzhen_b, i, j):  # 输入M*N和N*S型矩阵，运算如下表达式
        c = 0  # C[i+1,j+1] =∑（n,k=1）A[i+1,k] * B[k,j+1] 并返回 C[i+1,J+1]
        for m in range(len(jvzhen_a[0])):
            c = c + jvzhen_a[i][m] * jvzhen_b[m][j]
        return c
    hang_a = len(jvzhen_a)
    hang_b = len(jvzhen_b)
    lie_a = len(jvzhen_a[0])
    lie_b = len(jvzhen_b[0])
    jvzhen_c=[[0 for i in range(lie_b)]for j in range(hang_a)]
    if lie_a != hang_b:
        print('矩阵 A 的列数和 B 的行数不相同，不能进行乘法运算')
    else:
        for i in range(hang_a):
            for j in range(lie_b):
                jvzhen_c[i][j]=hangchenglie(jvzhen_a,jvzhen_b,i,j)
    return jvzhen_c

def jvzhenzhuanzhi(jvzhen):     #求矩阵的转置
    jieguo=[[0 for i in range(len(jvzhen))]for i in range(len(jvzhen[0]))]
    for i in range(len(jvzhen)):
        for j in range(len(jvzhen[0])):
            jieguo[j][i]=jvzhen[i][j]
    return jieguo

def shurujvzhen():  #输入数据的函数，返回一个矩阵
    jieshu=0
    hang=int(input('请输入行数'))
    lie=int(input('请输入列数'))
    chucun=[[0 for i in range(lie)]for j in range(hang)]
    for i in range(hang):
        for j in range(lie):
            chucun[i][j]=int(input('请输入第'+str(i+1)+'行，第'+str(j+1)+'列的数'))
    for i in range(hang):
        print(str(chucun[i])+'\n')
    return chucun

jvzhen=shurujvzhen()
jieguo=jvzhenchengfa(jvzhen,jvzhen)
for i in range(8):
    jieguo=jvzhenchengfa(jieguo,jvzhen)
for j in jieguo:
    print(j)
