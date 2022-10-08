import math
def panduanjvzhenxiangdeng(jvzhen_a,jvzhen_b):      # 判断两个矩阵是否相等
    hang_a = len(jvzhen_a)
    hang_b = len(jvzhen_b)
    lie_a = len(jvzhen_a[0])
    lie_b = len(jvzhen_b[0])
    c=0
    if hang_a != hang_b or lie_a != lie_b:
        print('不是同型矩阵一定不相等')
    else:
        for i in range(hang_a):
            for j in range(lie_a):
                c= c + math.fabs(jvzhen_a[i][j] - jvzhen_b[i][j]) # fabs()用于取绝对值
        if c==0:
            print('矩阵 A 和 矩阵 B 相等')
        else:
            print('矩阵 A 和 矩阵 B 不相等')

def qiufujvzhen(jvzhen_a):              #求一个矩阵 A 的负矩阵 -A
    for i in range(len(jvzhen_a)):
        for j in range(len(jvzhen_a[0])):
            jvzhen_a[i][j] = (-1) * jvzhen_a[i][j]
    return jvzhen_a


