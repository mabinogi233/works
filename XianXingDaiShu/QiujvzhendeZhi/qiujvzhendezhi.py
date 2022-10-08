from itertools import combinations
import math
import numpy as np
from numpy import array
def qiuzishi(jvzhen_a,k):       #求一个矩阵的 k 阶子式
    hang=len(jvzhen_a)
    lie=len(jvzhen_a[0])
    bianliang=min(hang,lie)
    if k > bianliang:                   #判断k与行和列的关系  k <= min(行，列)
        print('不存在 ',k,' 子式')
    else:
        # 找出行和列的全部组合，并以列表的形式存入列表中
        hang_1 = [i for i in range(hang)]
        lie_1=[i for i in range(lie)]
        hangzuhe=[]
        liezuhe=[]
        zuhe=[]
        jieguo=[]
        for i in combinations(hang_1,k):
            hangzuhe.append(list(i))
        for i in combinations(lie_1, k):
            liezuhe.append(list(i))
        for i in range(len(hangzuhe)):
            for j in range(len(liezuhe)):
                list_1=[hangzuhe[i],liezuhe[j]]
                zuhe.append(list_1)
        #以组合的行数和列数选取元素，并存入列表
        def xuanquyuansu(list,jvzhen,k):    #按list中的行和列选取jvzhen中的元素
            list_1=[[0 for i in range(k)]for j in range(k)]
            for i in range(k):
                for j in range(k):
                    list_1[i][j]=jvzhen[list[0][i]][list[1][j]]
            return list_1
        for i in range(len(zuhe)):
            list_2=xuanquyuansu(zuhe[i],jvzhen_a,k)
            jieguo.append(list_2)
    return jieguo               #返回一个包含所有k阶子式的三维数组

def jisuanzishi(zishi):        #传入一个包含所有k阶子式的三维数组，计算这些子式的值
    jieguo=[]
    k=len(zishi[0][0])
    for i in range(len(zishi)):
        shu=xunhuan(zishi[i])
        shu=math.fabs(shu)
        jieguo.append(shu)
    a=[jieguo,k]           #返回一个包含结果的数组和 k 阶
    return a

def xunhuanqiuzhi(jvzhen):      #输入一个矩阵，求矩阵的秩
    hang = len(jvzhen)
    lie = len(jvzhen[0])
    bianliang = min(hang, lie)
    k=0
    for i in range(bianliang,-1,-1):   #倒序循环
        zishi=qiuzishi(jvzhen,i)
        jieguo=jisuanzishi(zishi)
        jieguoshuzu=jieguo[0]
        k=jieguo[1]
        if sum(jieguoshuzu)!=0:
            break
    return k        #返回矩阵的秩

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

def huajian(list2=[]): #传入一个二维数组，按余子式展开
    a=0
    list1=[]
    yuzi=[]
    jieshu=len(list2)-1
    for i in range(len(list2)):
        a=list2[0][i]
        a=a*((-1)**(0+1+i+1))
        yuzi.append(a)
        chucun=list2[:]
        del chucun[0]
        np.array(chucun)
        a=np.delete(chucun,i,axis=1)
        b=a.tolist()
        list1.append(b)
    shuzu=[yuzi,list1]
    return shuzu

def jisuanerjie(list): #传入二维数组并计算(求解一阶行列式)
    yuzi=list[0]
    hanglieshi=list[1]
    sum=0
    for i in range(len(list[0])):
        hanglieshi_1=hanglieshi[i][0][0]
        yuzi_1=yuzi[i]
        sum = sum+yuzi_1*hanglieshi_1
    return sum

def diguiqiujie(list): #输入一个huajian处理的结果，处理huajian函数的结果，传入一个数组，包含余子式和n-1阶数组，并返回一个相同类型的数组
    jieguo=[]
    yuzisum=[]
    hanglieshi=[]
    yuzishi=list[0]
    for i in range(len(list[1])):
        list1=huajian(list[1][i])
        for j in range(len(list1[0])):
            yuzi=yuzishi[i]*list1[0][j]
            yuzisum.append(yuzi)
            hanglieshi.append(list1[1][j])
    jieguo=[yuzisum,hanglieshi]
    return jieguo

def xunhuan(list): #输入二维数组，返回结果
    sum=0
    if len(list[0])==1:
        sum=list[0][0]
    elif len(list[0])==2:
        list4=huajian(list)
        sum=jisuanerjie(list4)
    else:
        list1 = huajian(list)
        while True:
            list2=diguiqiujie(list1)
            if len(list2[1][0][0])==1:
                sum=jisuanerjie(list2)
                break
            else:
                list1=list2
    return sum
jvzhen=shurujvzhen()
zhi=xunhuanqiuzhi(jvzhen)
print('该矩阵的秩为 ',zhi)