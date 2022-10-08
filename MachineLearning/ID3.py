from math import log
import operator

#计算dataSet数据集的香农熵（dataSet为二维列表）熵越大，数据越混乱
def claShannonEnt(dataSet):
    #获取二维列表的行数
    lenght=len(dataSet)
    #创建一个字典，储存各个目标变量出现的次数
    zidian={}

    #目标变量存在二维数组最后一列，循环读取每一条数据
    for line in dataSet:
        #读取标签值（目标变量）
        currentLabels=line[-1]
        #将各个目标变量出现的次数存入字典
        if currentLabels in zidian.keys():
            zidian[currentLabels]+=1
        else:
            zidian[currentLabels]=1

    #计算这个数据集的香农熵
    ShannonEnt=0.0
    for key in zidian.keys():
        prob=zidian[key]/lenght
        ShannonEnt -= prob*log(prob,2)

    return ShannonEnt

#以特征值axis列的数据==value划分列表dataSet（划分后没有axis这个特征值，防止重复划分同一特征值）
def splitDataSet(dataSet,axis,value):
    #保持原数据集不变
    retdataSet=[]
    for line in dataSet:
        if line[axis]==value:
            newdataSet=line[:axis]
            #扩展列表
            newdataSet.extend(line[axis+1:])
            retdataSet.append(newdataSet)

    #返回划分好的二维列表
    return retdataSet

#根据香农熵变化最大的特征值选取最优解
def chooseBestsplit(dataSet):

    #计算原始数据集的香农熵
    baseShannon=claShannonEnt(dataSet)

    #创建要返回的特征值的列数
    bestaxis=-1

    #储存划分最好的香农熵
    bestinfoGain=0.0

    #在所有特征值中循环（列数减一（因为最后一列是标签））
    for i in range(len(dataSet[0])-1):
        #生成一个列表，保存第i列的特征值
        numlist=[lie[i] for lie in dataSet]

        #用集合set去重，获取所有能取到的特征值
        valueset=set(numlist)

        #用于保存新的香农熵
        newShannonEnt=0.0

        #以第i列的特征值分类，再求每个子集的香农熵
        #若第i行的特征值只为long short middle三种，则划分三个子集，第一个子集的元素第i列特征值全为long……
        for value in valueset:
            subDataSet=splitDataSet(dataSet,i,value)

            #分别计算每个子集的香农熵（这个子集占全集的比例prob * 子集的香农熵）
            prob=len(subDataSet)/len(dataSet)
            newShannonEnt += prob*claShannonEnt(subDataSet)

        #计算以第i列特征值分类的香农熵改变量（在这里一定为正）
        infoGain=baseShannon-newShannonEnt

        #选择香农熵改变量最大的特征值所在的列
        if infoGain>bestinfoGain:
            bestinfoGain=infoGain
            bestaxis=i

    #返回这个列
    return bestaxis


#生成决策树
def createTree(dataSet,labels):

    #创建一个classList储存每一条数据的标签
    classList=[hang[-1] for hang in dataSet]

    #如果所有元素标签一致（同一类）
    if classList.count(classList[0])==len(classList):
        return classList[0]

    #如果所有特征值都用完了而且还有记录没有被分类
    if len(dataSet[0])==1:
        #创建一个字典，统计各个标签出现的次数
        classCount={}
        for vote in classList:
            if vote not in classCount.keys():
                classCount[vote]=1
            else:
                classCount[vote]+=1

        #对标签出现次数排序，items()将这个字典拆为元组，对这些元组按第二个域（元素）排序，True表示降序，(这些元组只有两个域，labels和出现次数)
        sortedclassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)

        #返回出现次数最多的标签为分类标签
        return sortedclassCount[0][0]

    else:
        #计算按第几列的特征值划分最优
        bestaxis=chooseBestsplit(dataSet)

        #获取这一列特征值的标签（特征值的含义）
        bestaxislabel=labels[bestaxis]

        #生成树
        myTree={bestaxislabel:{}}

        #删除这个特征值标签(防止后面计算局部最优解出错)
        del(labels[bestaxis])

        #创建一个包含这一列特征值所有取值可能的集合
        uniquevalue=set([hang[bestaxis] for hang in dataSet])

        #按照每一个特征值可能的取值划分这列特征值
        for value in uniquevalue:
            myTree[bestaxislabel][value]=createTree(splitDataSet(dataSet,bestaxis,value),labels[:])

        #返回这个字典(树)
        return myTree



'''list=[['yes','yes','yes'],['yes','yes','yes'],['yes','no','no'],['no','yes','no'],['no','yes','no']]
label=['No surfacing','Flippers']
zidian=createTree(list,label)
print(zidian)'''

#将txt读取为二维列表
def jiexitxt(filename):
    list = []
    with open(filename,'r',encoding='UTF-8') as io:
        txterwei=io.readlines()

        for line in txterwei:
            line = line.strip('\ufeff')
            # 剔除开头结尾的空字符
            line = line.strip()
            # 在以\t分界转化为列表
            linelist = line.split('\t')
            #将这个列表加入list
            list.append(linelist)
        
        dataSet=list[1:]
        
        labels=list[0][:-2]

        judge=list[0][-1]

    return dataSet,labels,judge


def main():
    filename=input('请输入待分类文件的绝对路径')
    list = [['yes', 'yes', '1'], ['yes', 'yes', '1'], ['yes', 'no', '0'], ['no', 'yes', '0'], ['no', 'yes', '0']]
    labels = ['No surfacing', 'Flippers']
    #dataSet,labels,judge=jiexitxt(filename)
    #print('按 ',judge,' 类分类')
    Tree=createTree(list,labels)
    print(Tree)


main()




