#   k - 近邻算法(应用的数据类型为numpy的array不是matrix)
import numpy
import operator

# 创建一个分类器
# 输入一个向量inX，计算与dataSet中各个数据的距离，标签向量为labels(list类型)，k为选取最近的点的个数
def classify(inX,dataSet,labels,k):

    # 获取dataSet的长度
    datasitelen=dataSet.shape[0]

    # inX在行上重复datasitelen次，在列上重复一次，形成一个与dataSet同型的矩阵，再减去矩阵dataSet,获得每一个分量的差值
    diff=numpy.tile(inX,(datasitelen,1))-dataSet

    #diff每一个分量平方
    diff=diff**2

    #每一行求和返回一个距离值（jvDistance一个datasitelen * 1矩阵）
    jvDistance=diff.sum(axis=1)

    #这个矩阵开根号，结果为inX和dataSet每一个行向量的距离（jvDistance一个datasitelen * 1矩阵）
    distance=jvDistance**0.5

    #返回的sortedDistance就是包含distance矩阵中从小到大的元素的索引（返回的是数组值从小到大的索引值）
    sortedDistance=distance.argsort()

    #建立一个空字典，放置距离最小的向量的标签
    classCount={}

    #循环k次，寻找k个最接近的元素
    for i in range(k):
        #获取前k小的向量的标签
        votelabels=labels[int(sortedDistance[i])]
        #用字典储存这些标签出现的次数，若标签不存在则储存0+1，存在则 +1
        classCount[votelabels]=classCount.get(votelabels,0)+1

    #items()将这个字典拆为元组，对这些元组按第二个域（元素）排序，True表示降序，(这些元组只有两个域，第labels和出现次数)
    sortedclassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)

    #返回出现次数最多的元素的标签,sortedclassCount中储存的是列表嵌套元组
    return sortedclassCount[0][0]


#读取文本文档中的数据，并转化为矩阵dataSet和对应的labels
def filematrix(filename):

    #创建文件的io流
    inputio=open(filename,encoding='UTF-8')

    #读取文件的每一行，并且组成一个字符串，这个列表可以一行一行读取的字符串
    filelist=inputio.readlines()

    #获取字符串的行数(特征值的行数，因此要减一)
    hangshu=len(filelist)

    #获取字符串的列数(先取第一行，剔除开头结尾的空字符，在以\t分界转化为列表，再获取列表的长度)
    lieshu=len(filelist[0].rstrip().split('\t'))-1

    #创建一个hang * lie的零矩阵，用于储存循环得到的数据
    dataMat=numpy.zeros((hangshu,lieshu))

    #创建一个储存目标变量的列表
    classLabels=[]

    #循环的索引值，初始为0
    i=0

    #循环，储存每一行的数据进入classLabels和dataSet
    for line in filelist:
        line = line.strip('\ufeff')
        #剔除开头结尾的空字符
        line=line.strip()
        #在以\t分界转化为列表
        linelist=line.split('\t')
        #将特征值存入dataMat（第一列为目标变量）

        dataMat[i,:]=linelist[1:]
        #将目标向量（int化）存入classLabels
        classLabels.append(int(linelist[0]))
        #索引值加一
        i+=1

    #返回特征值矩阵和目标变量列表
    return dataMat,classLabels

#归一化特征值（全部用0-1的数表示），公式为newvalue=oldvalue-min/max-min
def autoNorm(dataSet):

    #求每一列的最大值和最小值，返回值为一个【1x列数】的行矩阵
    minValue=dataSet.min(0)
    maxValue=dataSet.max(0)

    #获取dataSet的行数和列数
    hangshu=dataSet.shape[0]
    lieshu=dataSet.shape[1]

    #将max-min扩展为与dataSet同型的矩阵再用除法（除法表示每一个元素分别相除）
    linshibianliang=numpy.zeros(numpy.shape(dataSet))
    linshibianliang=dataSet-numpy.tile(minValue,(hangshu,1))
    linshibianliang=linshibianliang / numpy.tile(maxValue-minValue,(hangshu,1))

    return linshibianliang,maxValue-minValue,minValue

#测试数据
def textdata():
    #读取测试数据和目标变量
    textSet,textclassLabels=filematrix('D:\works\shujv\Filmtext.txt')

    #读取已经准确分类的数据和目标变量
    dataSet,classlabels=filematrix('D:\works\shujv\Film.txt')

    #归一化数据
    textSet,range_1,min=autoNorm(textSet)
    dataSet,range_2,min_1=autoNorm(dataSet)

    #错误次数初始为零
    errorcount=0

    #总测试次数为textdSet的行数
    count=textSet.shape[0]

    #循环测试完这些数据
    for i in range(count):
        result=classify(textSet[i],dataSet,classlabels,10)
        if result != textclassLabels[i]:
            errorcount +=1
        print('分类结果为:',result,'，正确结果为：',textclassLabels[i])
    #计算错误率
    print('错误率为:',errorcount/count)

#运行过后加入数据集
def adddata(inX,result):
    with open('D:\works\shujv\Film.txt','a',encoding='UTF-8') as io:
        io.write('\n')
        io.write(str(result)+'\t')
        for i in range(len(inX)):
            io.write(str(inX[i])+'\t')


def main():
    k = True
    print('程序开始')
    while k:
        a=int(input('请输入 num_voted_users 的数量'))
        b=int(input('请输入budget的数目'))
        c=int(input('请输入movie_facebook_likes的人数'))
        inX=numpy.array([a,b,c])
        dataSet,classlabels=filematrix('D:\works\shujv\Film.txt')
        dataSet,range_1,min=autoNorm(dataSet)
        inY=inX-min
        inY=inX/range_1
        result=classify(inY,dataSet,classlabels,2)
        print('分类结果为 ',result)
        boor=input('是否加入数据集')
        if boor=='是':
            adddata(inX,result)
        panduan=input('是否继续？')
        if panduan=='否':
            k=False
    print('程序结束')

main()