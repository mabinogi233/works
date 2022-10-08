
def duidiaolie(jvzhen,i,j): #对调矩阵i,j两列
    linshibianliang=[0 for i in range(len(jvzhen))]
    for a in range(len(jvzhen)):
        linshibianliang[a]=jvzhen[a][j]
    for a in range(len(jvzhen)):
        jvzhen[a][j]=jvzhen[a][i]
    for a in range(len(jvzhen)):
        jvzhen[a][i]=linshibianliang[a]
    return jvzhen

def duidiaohang(jvzhen,i,j):    #对调矩阵i，j两行
    linshibianliang=jvzhen[j]
    jvzhen[j]=jvzhen[i]
    jvzhen[i]=linshibianliang
    return jvzhen

def chengshulie(jvzhen,k,i):    #@对矩阵第i列乘 k
    i=i-1
    for j in range(len(jvzhen)):
        jvzhen[j][i]=k * jvzhen[j][i]
    return jvzhen

def chengshuhang(jvzhen,k,i):    #对矩阵第i行乘 k
    for j in range(len(jvzhen[0])) :
        jvzhen[i][j]=jvzhen[i][j] * k
    return jvzhen

def chenglie(jvzhen,i,j,k):     #将第i列乘k 再加到第j列
    for a in range(len(jvzhen)):
        jvzhen[a][j]=jvzhen[a][j] + jvzhen[a][i] * k
    return jvzhen

def chenghang(jvzhen,i,j,k):       #将第i行乘k 再加到第j行
    for a in range(len(jvzhen[0])):
        jvzhen[j][a]=jvzhen[j][a] + jvzhen[i][a] * k
    return jvzhen

def huajianhangjieti(jvzhen):   #将一个矩阵化简为行阶梯形矩阵
    def  lingjvzhen(jvzhen_2):                              #判断零矩阵
        sum=0
        for i in range(len(jvzhen_2)):
            for j in range(len(jvzhen_2[0])):
                sum=sum+abs(jvzhen_2[i][j])
        return sum

    a=lingjvzhen(jvzhen)
    if a==0:
        print('零矩阵')
    else:
        feiling=[]
        for i in range(len(jvzhen)):        #找出一个非零元
            for j in range(len(jvzhen[0])):
                if jvzhen[i][j] !=0:
                    feiling.append(i)
                    feiling.append(j)
                    break
            if feiling!=[]:
                break
        for i in range(len(jvzhen[0])):     #将这个非零元所在列乘1加到每一列
            jvzhen=chenglie(jvzhen,feiling[1],i,1)
        for j in range(len(jvzhen)):        #将这个非零元所在行乘1加到每一行
            jvzhen=chenghang(jvzhen,feiling[0],j,1)
        for i in range(min(len(jvzhen),len(jvzhen[0]))):    #化简为行阶梯
            a=jvzhen[i][i]
            if a==0:
                for j in range(i+1,len(jvzhen)):
                    a=jvzhen[j][i]
                    if a !=0:
                        break
            if a==0:
                continue
            for j in range(i+1,len(jvzhen)):
                b =  - (jvzhen[j][i]/a) #需要定义分数
                chenghang(jvzhen,i,j,b)
    return jvzhen

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

jvzhen_1=shurujvzhen()
jvzhen_2=huajianhangjieti(jvzhen_1)
for i in jvzhen_2:
    print(i)






