import numpy as np
#朴素贝叶斯算法（各个特征值相互独立）
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
    labels=list[0]
    return dataSet,labels

#贝叶斯分类器（输入：特征值的名字=值）
def Bayes(dataSet,labels,**tezhengzhi):

    #将这个字典变为两个列表（classlabels表示储存的特征值的名字，data表示储存的特征值的值）
    classlabels=[]
    data=[]
    for key,value in tezhengzhi.items():
        classlabels.append(key)
        data.append(value)

    # 储存classlabels中特征值存在的列数
    indexs = []
    for tezheng in classlabels:
        indexs.append(labels.index(tezheng))

    #计算分母
    '''prob_fenmu=1.0
    j = 0
    for i in indexs:
        classList=[hang[i]for hang in dataSet]
        classCount = {}
        for vote in classList:
            if vote not in classCount.keys():
                classCount[vote] = 1
            else:
                classCount[vote] += 1
        prob_i=classCount[data[j]]/len(classList)
        prob_fenmu=prob_fenmu * prob_i
        j+=1'''
    fenmugeshu=0
    for hang in dataSet:
        j=0
        count = 0
        for i in indexs:
            if hang[i]==data[j]:
                count+=1
            j+=1
        if count==len(data):
            fenmugeshu+=1
    prob_fenmu=fenmugeshu/len(dataSet)
    print(fenmugeshu)


    lasts=[hang[-1] for hang in dataSet]
    lastset=set(lasts)
    prob_list=[]
    for last in lastset:
        list=[]
        for hang in dataSet:
            if hang[-1]==last:
                list.append(hang)
        prob_g=len(list)/len(dataSet)
        prob_fenzi=1.0
        j = 0
        for i in indexs:
            count=0
            for hang in list:
                if hang[i]==data[j]:
                    count+=1
            prob_fenzi_i=count/len(list)
            prob_fenzi=prob_fenzi * prob_fenzi_i
            j+=1
        prob=(prob_fenzi * prob_g)/prob_fenmu
        prob_list.append([last,prob])

    return prob_list

def printProbList(problist,labels):

    for prob_hang in problist:
        print('此时 ',labels[-1],' 为 ',prob_hang[0], '时的概率为：',prob_hang[1])

    problmax=0.0
    problabel=None
    for hang in problist:
        if hang[1]>problmax:
            problmax=hang[1]
            problabel=hang[0]

    print('在此条件下最佳的选择为：',problabel,'，概率为：',problmax)

labels=['帅不帅','性格好不好','身高','上进与否','嫁与否']
dataSet=[['帅','不好','矮','不上进','不嫁'],
        ['不帅','好','矮','上进','不嫁'],
        ['帅','好','矮','上进','嫁'],
        ['不帅','好','高','上进','嫁'],
        ['帅','不好','矮','上进','不嫁'],
        ['不帅','不好','矮','不上进','不嫁'],
        ['帅','好','高','不上进','嫁'],
        ['不帅','好','高','上进','嫁'],
        ['帅','好','高','上进','嫁'],
        ['不帅','不好','高','上进','嫁'],
        ['帅','好','矮','不上进','不嫁'],
        ['帅','好','矮','不上进','不嫁']]

list=Bayes(dataSet,labels,帅不帅='不帅',性格好不好='不好',身高='矮',上进与否='不上进')
printProbList(list,labels)