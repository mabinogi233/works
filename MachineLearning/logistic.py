import numpy
import math
import random
import cmath


def sigmoid(hangdata,inW):# hangdata和inW都是一维列表
    hangdata=numpy.matrix(hangdata)
    inW=numpy.matrix(inW).transpose()
    x=int((hangdata * inW)[0,0])
    z = 1 / (1 + math.e**(-x))
    return z

#输入dataSet,返回似然函数的自然对数（dataSet中每一行为一个行向量（一条数据特征值））dataSet最后一列为标签值
def linkehood():
    def linkhood_function(dataSet,inW): #inW是list类型，dataSet是二维list,dataSet最后一列是标签
        fw_result=0
        for hang in dataSet:
            y=dataSet[-1]
            hangdata=hang[:-1]
            z=sigmoid(hangdata,inW)
            fw_result += y * math.log(z,math.e) + (1-y) * math.log(1-z,math.e)
        return fw_result
    f=linkhood_function
    return f

#返回fw在inW=[w1,w2……wN]处的梯度向量（list类型）
def GetGrad(dataSet,inW):
    gradlist=[]
    for j in range(len(inW)):
        W=0
        for hang in dataSet:
            y=hang[-1]
            hangdata=hang[:-1]
            z=sigmoid(hangdata,inW)
            W+=(y-z) * hang[j]
        gradlist.append(W)
    return gradlist
#循环cishu次数次，梯度上升求使fw最大值时的向量w
def gradup(dataSet,a=0.001,cishu=800):
    inW=[1 for i in range(len(dataSet[0])-1)]
    for i in range(cishu):
        grad=GetGrad(dataSet,inW)
        inW=list(numpy.array(inW) + a * numpy.array(grad))
    return inW


#随机梯度上升
def RadomsGradUp(dataSet,cishu=500,a=0.001):
    inW=[1 for i in range(len(dataSet[0])-1)]
    for j in range(cishu):
        dataSetindex = [i for i in range(len(dataSet))]
        for i in range(len(dataSet)):
            a=0.01/(i+j+1)+0.0001
            readindex=int(random.uniform(0,len(dataSetindex)))
            datahang=dataSet[readindex]
            y = datahang[-1]
            x=datahang[:-1]
            z = sigmoid(x, inW)
            grad=(numpy.array(datahang[:-1]))*(y-z)
            inW=list(numpy.array(inW) + a * grad)
            del dataSetindex[readindex]
    return inW






def judge(hanglist,inW):
    z=sigmoid(hanglist,inW)
    if z<=0.5:
        return 0
    else:
        return 1


def jiexitxt(filename):
    dataSet = []
    with open(filename, 'r', encoding='UTF-8') as io:
        txterwei = io.readlines()
        for line in txterwei:
            line = line.strip('\ufeff')
            # 剔除开头结尾的空字符
            line = line.strip()
            # 在以\t分界转化为列表
            linelist = line.split('\t')
            #将列表内容转变为int
            if len(linelist)>0 and dataSet!=[]:
                for i in range(len(linelist)):
                    linelist[i]=int(linelist[i])
            # 将这个列表加入list
            dataSet.append(linelist)
    return dataSet

def main():
    classlabels=['否','是']
    print('程序开始')
    #dataSet=jiexitxt('D:\works\shujv\logistic.txt')
    dataSet = [['min','max','labels'],[-4, 228, 0], [-12, 58, 1], [-17, 28, 1], [-17, 82, 1], [-17, 82, 1], [7, 68, 1], [5, 8, 1]]
    print('数据加载成功')
    inW=RadomsGradUp(dataSet[1:])
    print('最优回归系数确定')
    labels=dataSet[0]
    while True:
        print('请输入',len(labels)-1,'个特征值，以空格分界')
        massage=input()
        massage=massage.split(' ')
        for i in range(len(massage)):
            massage[i]=int(massage[i])
        result=judge(hanglist=massage,inW=inW)
        print(classlabels[result])
        quitt=input('是否退出？')
        if quitt=='是':
            break
    print('程序结束')
main()