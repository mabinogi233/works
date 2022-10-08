import math
import sklearn.datasets

#通用决策树模板
#author：Liuwenze
#可以通过重写

class decision_Tree:

    def __init__(self,dataSet,labels,algroithm):
        self.labels = labels
        self.treeMap = self.create_tree(dataSet,labels,algroithm)

    # 判断是否只有一种类型的数据
    def conut_sim(self,dataSet):
        list_unqiue = []
        for line in dataSet:
            if (line[-1] not in list_unqiue):
                list_unqiue.append(line[-1])
        return len(list_unqiue) == 1

    # 计数dataSet中出现次数最多的标签
    def conut_max(self,dataSet):
        dict_conut = {}
        for line in dataSet:
            if (str(line[-1]) not in dict_conut):
                dict_conut[str(line[-1])] = 1
            else:
                dict_conut[str(line[-1])] += 1
        max_key = ""
        max_values = -1
        for key, values in dict_conut.items():
            if (values > max_values):
                max_key = key

        return max_key

    # 根据指定的标签划分数据集
    def divide_dataSet(self,dataSet, labels, divide_label):
        # key 为 divide_label的不同取值，value为divide_label = 相同值(key)的集合
        dict_by_divide_label = {}
        label_index = labels.index(divide_label)

        # 每一行的数据
        for line in dataSet:
            if (line[label_index] not in dict_by_divide_label):
                dict_by_divide_label[line[label_index]] = []
                new_line = line[:]
                del new_line[label_index]
                dict_by_divide_label[line[label_index]].append(new_line)
            else:
                new_line = line[:]
                del new_line[label_index]
                dict_by_divide_label[line[label_index]].append(new_line)
        # 返回划分好的数据集组成的字典
        return dict_by_divide_label

    # 此函数用于选择划分的标签，对于不同
    def get_divide_label(self,dataSet, labels,algroithm):
        #选择ID3算法划分
        if(algroithm=="ID3" or algroithm=="id3"):
            return self.id3(dataSet,labels)
        else:
            return labels[0]

    def create_tree(self,dataSet, labels,algroithm):
        if (self.conut_sim(dataSet)):
            # 不需要分类
            # 返回任意一条数据的结果（所有数据结果唯一）
            return str(dataSet[0][-1])
        if (len(labels) == 0):
            # 特征值为空
            # 返回dataSet中出现最多的标签
            return self.conut_max(dataSet)

        # 根据特定的函数计算出需要划分的标签
        divide_label = self.get_divide_label(dataSet, labels,algroithm)

        # 不满足划分条件
        if (divide_label == None):
            return self.conut_max(dataSet)

        # 划分dataSet
        divide_dataSet_dict = self.divide_dataSet(dataSet, labels, divide_label)
        # 构造子树
        treeMap = {}
        treeMap[divide_label] = {}
        for key, child_dataSet in divide_dataSet_dict.items():
            # 删除划分好的标签
            new_labels = labels[:]
            del new_labels[labels.index(divide_label)]
            # print(key,child_dataSet)
            treeMap[divide_label][key] = self.create_tree(child_dataSet, new_labels,algroithm)
        return treeMap

    #上述部分为通用部分，下面为划分算法部分，本实验只实现了ID3算法

    #*******************************************************************************************
    #ID3划分，最小的熵值改变量的阈值默认为0.001
    def id3(self,dataSet,labels,min_change=0.001):
        #计算数据集熵值
        dataSetShannonEnt = self.getShannonEnt(dataSet)

        bestLabel = -1
        #取一个很小的值
        max_change_shannonEnt = -1000

        #计算每个label对应的划分后的熵的总和
        for label in labels:
            #划分数据集
            divide_dataSets = self.divide_dataSet(dataSet,labels,label)
            #储存划分后的熵值
            main_shannonEnt = 0
            # 分别计算每个子集的熵（这个子集占全集的比例prob * 子集的熵）
            for key,newdataSet in divide_dataSets.items():
                prob = len(newdataSet)/len(dataSet)
                main_shannonEnt+=prob*self.getShannonEnt(newdataSet)
            #计算改变量并取相反数（将熵值的变化量变为正数）
            change_shannonEnt = dataSetShannonEnt - main_shannonEnt
            if(change_shannonEnt>max_change_shannonEnt):
                max_change_shannonEnt = change_shannonEnt
                bestLabel = label

        #小于阈值，不做划分，返回None
        if(max_change_shannonEnt<=min_change or bestLabel==-1):
            return None
        else:
            return bestLabel

    # 计算dataSet数据集的香农熵
    def getShannonEnt(self,dataSet):
        # 获取二维列表的行数
        lenght = len(dataSet)
        # 创建一个字典，储存各个目标变量出现的次数
        zidian = {}
        # 目标变量存在二维数组最后一列，循环读取每一条数据
        for line in dataSet:
            # 读取标签值（目标变量）
            currentLabels = line[-1]
            # 将各个目标变量出现的次数存入字典
            if currentLabels in zidian.keys():
                zidian[currentLabels] += 1
            else:
                zidian[currentLabels] = 1
        # 计算这个数据集的香农熵
        ShannonEnt = 0.0
        for key in zidian.keys():
            prob = zidian[key] / lenght
            ShannonEnt -= prob * math.log(prob, 2)
        return ShannonEnt

    #*******************************************************************************************

    #输出树的结构
    def printTree(self):
        self.print_unqiue(self.treeMap,0)

    def printDict(self):
        print(self.treeMap)

    def print_unqiue(self,treemap,deep):
        if(type(treemap)==type({})):
            for key in treemap.keys():
                for i in range(deep):
                    print("\t",end='')
                print(key)
                dict_by_key = treemap[key]
                for shuxing in dict_by_key.keys():
                    for i in range(deep+1):
                        print("\t", end='')
                    print(shuxing)
                    self.print_unqiue(dict_by_key[shuxing],deep+1)
        else:
            for i in range(deep):
                print("\t", end='')
            print(treemap)

    # *******************************************************************************************

    #决策树验证一条数据
    def fit_one_data(self,line_data,treemap):
        for key in treemap.keys():
            dict_by_key = treemap[key]
            label_index = self.labels.index(key)
            shuxing = line_data[label_index]
            newTreeMap = dict_by_key[shuxing]
            if(type(newTreeMap)==type("str")):
                return newTreeMap
            else:
                return self.fit_one_data(line_data,newTreeMap)

    #决策树验证数据集
    def fit_data(self,datas):
        biaoqian= []
        for data in datas:
            label = self.fit_one_data(data,self.treeMap)
            biaoqian.append(label)
        return biaoqian


#*******************************************************************************************

def loadData():
    dataSet = []
    labels = []
    biaoqian_true = []
    with open(r"E:\文件\机器学习\机器学习数据集\melon.txt", 'r', encoding='utf-8')as f:
        i = 0
        for line in f.readlines():
            if (i == 0):
                # 表示读第一行属性的标签
                labels = (line.strip("\n").split(","))[:]
                del labels[9]
                del labels[0]
            else:
                list_line = line.strip("\n").split(",")
                data_line = list_line[:]
                # 处理含糖量(连续数据转化为离散数据)
                if (0 <= float(list_line[8]) < 0.2):
                    data_line[8] = '不甜'
                elif (0.2 <= float(list_line[8]) < 0.4):
                    data_line[8] = '微甜'
                elif (0.4 < float(list_line[8]) < 0.6):
                    data_line[8] = '较甜'
                else:
                    data_line[7] = '很甜'
                # 处理密度(连续数据转化为离散数据)
                if (0 <= float(list_line[7]) < 0.2):
                    data_line[7] = '较小'
                elif (0.2 <= float(list_line[7]) < 0.4):
                    data_line[7] = '适中'
                elif (0.4 < float(list_line[7]) < 0.6):
                    data_line[7] = '稍大'
                else:
                    data_line[7] = '较大'
                # 删除序号
                del data_line[0]
                dataSet.append(data_line)
                biaoqian_true.append(data_line[-1])
            i += 1
    return dataSet,labels,biaoqian_true


def get_zhengquelv(biaoqian_true,biaoqian_pred):
    count = 0
    for i in range(len(biaoqian_true)):
        if(biaoqian_true[i]==biaoqian_pred[i]):
            count+=1
    return count/len(biaoqian_true)


def load_iris():
    iris = sklearn.datasets.load_iris()
    label_name = iris['target_names']
    dataSet_lianxv = list(iris['data'])
    dataSet_lisan = []
    label = iris['target']
    maxx = 0
    minx = 1000
    i = 0
    for line in dataSet_lianxv:
        yangben = []
        if (list(line)[3] > maxx):
            maxx = list(line)[3]
        if (list(line)[3] < minx):
            minx = list(line)[3]
            # 连续转离散 4-5 5-6 6-7 7-8 8-9 一类
        if (4<list(line)[0]<=5):
            yangben.append('4-5')
        elif (5<list(line)[0]<=6):
            yangben.append('5-6')
        elif (6<list(line)[0]<=7):
            yangben.append('6-7')
        elif (7<list(line)[0]<=8):
            yangben.append('7-8')
        elif (8<list(line)[0]<=9):
            yangben.append('8-9')
        else:
            yangben.append('null')

        if (2<=list(line)[1]<=3):
            yangben.append('2-3')
        elif (3<list(line)[1]<=4):
            yangben.append('3-4')
        elif (4<list(line)[1]<=5):
            yangben.append('4-5')
        else:
            yangben.append('null')

        if (1<list(line)[2]<=2.5):
            yangben.append('1-2.5')
        elif (2.5<list(line)[2]<=4):
            yangben.append('2.5-4')
        elif (4<list(line)[2]<=5.5):
            yangben.append('4-5.5')
        elif (5.5<list(line)[2]<=7):
            yangben.append('5.5-7')
        else:
            yangben.append('null')

        if (0<list(line)[3]<=1):
            yangben.append('0-1')
        elif (1<list(line)[3]<=2):
            yangben.append('1-2')
        elif (2<list(line)[3]<=3):
            yangben.append('2-3')
        else:
            yangben.append('null')
        yangben.append(str(label[i]))
        i+=1
        dataSet_lisan.append(yangben)
    shuxing = ['A','B','C','D']
    biaoqqian_true = []
    for i in list(label):
        biaoqian_true.append(str(i))
    return dataSet_lisan,shuxing,biaoqian_true


if __name__ == "__main__":
    dataSet,labels,biaoqian_true = load_iris()
    #加载数据集
    # dataSet,labels,biaoqian_true = loadData()
    print("数据集展示")
    print(labels)
    for line in dataSet:
        print(line)
    print(biaoqian_true)
    #创建决策树
    id3tree = decision_Tree(dataSet=dataSet,labels=labels,algroithm="ID3")
    #输出决策树
    print("决策树：")
    id3tree.printTree()
    print("字典形式输出决策树：")
    id3tree.printDict()
    #加载验证集
    biaoqian_pred = id3tree.fit_data(dataSet)
    #通过预测的标签和真实的标签计算正确里
    print("预测的标签")
    print(biaoqian_pred)
    print("真实的标签")
    print(biaoqian_true)
    print("正确率")
    print(get_zhengquelv(biaoqian_true,biaoqian_pred))
