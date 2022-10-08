import numpy as np
from numpy import array
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

    for i in range(len(yuzi)):
        print(str(yuzi[i])+' * '+str(list1[i]))

    return shuzu            #返回一个列表包含

def chucun():  #输入数据的函数，返回一个二维数组
    jieshu=0
    jieshu=input('请输入阶数')
    jieshu=int(jieshu)
    chucun=[[0 for i in range(jieshu)]for j in range(jieshu)]
    for i in range(jieshu):
        for j in range(jieshu):
            chucun[i][j]=int(input('请输入第'+str(i+1)+'行，第'+str(j+1)+'列的数'))
    for i in range(jieshu):
        print(str(chucun[i])+'\n')
    return chucun

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

chucundeshujv=chucun()
sum=xunhuan(chucundeshujv)
print(sum)
