import numpy as np
import random
import csv

from sklearn import datasets

def sigmoid(x):
    return 1/(1+np.exp(-x))

class bp():
    #输入层神经元个数x_len，隐层神经元个数h_len，输出层的个数y_len
    def __init__(self,x_len,h_len,y_len):
        #随机初始化参数
        self.w1 = np.random.randint(0,100,(h_len,x_len)).astype('float64')/100
        self.b1 = np.random.randint(0,100,(h_len,1)).astype('float64')/100
        self.w2 = np.random.randint(0,100,(y_len,h_len)).astype('float64')/100
        self.b2 = np.random.randint(0, 100, (y_len, 1)).astype('float64')/100
        #目前只可使用sigmoid为激活函数
        self.f = sigmoid

    #训练 a为学习率 n为迭代次数
    def train(self,dataSet,y_true,a=0.05,n=3):
        for j in range(n):
            for i in range(len(dataSet)):
                # 行向量变列向量
                x = np.array([dataSet[i]]).transpose()
                # 正向求y预测
                # 隐层输入
                x1 = np.dot(self.w1, x) - self.b1
                # 隐层输出
                h = self.f(x1)
                # 输出层输入
                x2 = np.dot(self.w2, h) - self.b2
                # 输出层输出
                y_prec = self.f(x2)
                # 计算输出层梯度
                g = np.multiply(np.multiply(y_prec, 1 - y_prec), (np.array([y_true[i]]).transpose() - y_prec))
                # 计算隐层梯度
                e = np.multiply(np.multiply(h, 1 - h), np.dot(self.w2.transpose(), g))
                # 计算更新步长
                w2_change = a * (np.dot(g, h.transpose()))
                w1_change = a * (np.dot(e, x.transpose()))
                b2_change = -1 * a * g
                b1_change = -1 * a * e
                # 更新参数
                self.w1 += w1_change
                self.w2 += w2_change
                self.b1 += b1_change
                self.b2 += b2_change

    #运行
    def run(self,dataSet):
        y_true_list = []
        for i in range(len(dataSet)):
            # 行向量变列向量
            x = np.array([dataSet[i]]).transpose()
            # 正向求y预测
            # 隐层输入
            x1 = np.dot(self.w1, x) - self.b1
            # 隐层输出
            h = self.f(x1)
            # 输出层输入
            x2 = np.dot(self.w2, h) - self.b2
            # 输出层输出
            y_prec = self.f(x2)
            y_true_list.append(list(y_prec))
        return y_true_list


#加载数据集
def load_iris_bp():
    iris = datasets.load_iris()
    dataSet = list(iris['data'])
    label = iris['target']
    #将label变为二维数组（每一行三个数，若为（0,0,1）表示其为第三类，(0,1,0)表示其为第二类别，即输出层单元数为三）
    label_bp = []
    for item in list(label):
        if(item==0):
            # 第一类
            label_bp.append([1,0,0])
        elif (item == 1):
            # 第二类
            label_bp.append([0, 1, 0])
        elif (item == 2):
            # 第三类
            label_bp.append([0, 0, 1])
        else:
            #未知则随机分配
            ran = random.randint(0,2)
            if(ran==0):
                label_bp.append([1, 0, 0])
            if (ran == 1):
                label_bp.append([0, 1, 0])
            if (ran == 2):
                label_bp.append([0, 0, 1])
    label_name = iris['target_names']
    return dataSet,label,label_bp,label_name

#将BP网络的输出变为类别
def print_iris_bp(bp_output):
    y = []
    # 将BP网络的输出变为类别
    for one in bp_output:
        #找出最大输出元素的下标，即为类别（0，1，2）
        if(one[0]==max(one[0],one[1],one[2])):
            y.append(0)
        if (one[1] == max(one[0], one[1], one[2])):
            y.append(1)
        if((one[2]==max(one[0],one[1],one[2]))):
            y.append(2)
    return y

def good_conut(y,y_true):
    #计算正确的个数，返回正确率
    conut = 0
    for i in range(len(y_true)):
        if(y[i]==y_true[i]):
            conut +=1
    return conut/len(y_true)


#自助法采样得到验证集,m为验证集样本个数
def bootstrapping(dataSet,label,m):
    checkDataSet = []
    checkLabel = []
    for i in range(m):
        #随机有放回的取m次
        x = random.randint(0,len(dataSet)-1)
        checkDataSet.append(dataSet[x])
        checkLabel.append(label[x])
    return checkDataSet,checkLabel

def run_by_iris():
    #加载数据
    dataSet,label,label_bp,label_name = load_iris_bp()
    # 加载验证集
    checkDataSet, checkLabel = bootstrapping(dataSet, label, 50)
    #建立模型,隐藏个数随机迭代，取正确率最高的隐层个数
    n=10 #n为次数

    max_true_precent = 0
    bpGood = None
    h_len_max = 0
    for i in range(n):
        h_len = random.randint(3,20)
        bp_iris = bp(4,h_len,3)
        bp_iris.train(dataSet,label_bp,0.05,100)
        #验证
        y_prec = bp_iris.run(checkDataSet)
        #获取正确率
        y = print_iris_bp(y_prec)
        true_precent = good_conut(y,checkLabel)
        #若正确率更高，则替换
        if(true_precent>max_true_precent):
            max_true_precent = true_precent
            bpGood = bp_iris
            h_len_max = h_len

    #输出预测值和真实值
    print("真实标签值")
    print(checkLabel)
    print("预测标签")
    print(print_iris_bp(bpGood.run(checkDataSet)))
    #输出标签的含义
    print("标签0对应的类别：",label_name[0])
    print("标签1对应的类别：", label_name[1])
    print("标签2对应的类别：", label_name[2])
    # 输出正确率
    print("正确率")
    print(max_true_precent)


#加载酒类质量数据集
def load_uci_winequality(path):
    count = 0
    dataSet = []
    label = []
    label_bp = []
    label_name =[]
    with open(path,'r',encoding='utf-8') as f:
        csvf = csv.reader(f)
        for i in csvf:
            one_list = i[0].split(";")
            if(count!=0):
                list_j=[]
                for j in range(len(one_list)-1):
                    list_j.append(float(one_list[j]))
                dataSet.append(list_j)
                label.append(int(one_list[-1]))
                if(int(one_list[-1])==3):
                    label_bp.append([1, 0, 0, 0, 0, 0])
                elif (int(one_list[-1]) == 4):
                    label_bp.append([0, 1, 0,0,0,0])
                elif (int(one_list[-1]) == 5):
                    label_bp.append([0, 0, 1,0,0,0])
                elif (int(one_list[-1]) == 6):
                    label_bp.append([0, 0, 0,1,0,0])
                elif (int(one_list[-1]) == 7):
                    label_bp.append([0, 0, 0,0,1,0])
                elif (int(one_list[-1]) == 8):
                    label_bp.append([0, 0, 0,0,0,1])
                else:
                    # 未知则随机分配
                    ran = random.randint(3, 8)
                    if (ran == 3):
                        label_bp.append([1, 0, 0,0,0,0])
                    if (ran == 4):
                        label_bp.append([0, 1, 0,0,0,0])
                    if (ran == 5):
                        label_bp.append([0, 0, 1,0,0,0])
                    if (ran == 6):
                        label_bp.append([0, 0, 0,1,0,0])
                    if (ran == 7):
                        label_bp.append([0, 0, 0,0,1,0])
                    if (ran == 8):
                        label_bp.append([0, 0, 0,0,0,1])
                count+=1
            else:
                label_name = one_list
                count+=1
    #酒的质量为3-8共6种可能
    return normalize(dataSet),label,label_bp,label_name


#将BP网络的输出变为类别
def print_winequality_bp(bp_output):
    y = []
    # 将BP网络的输出变为类别
    for one in bp_output:
        #找出最大输出元素的下标，即为类别（3,4,5,6,7,8）
        if(one[0] == max(one[0],one[1],one[2],one[3],one[4],one[5])):
            y.append(3)
        if (one[1]==max(one[0],one[1],one[2],one[3],one[4],one[5])):
            y.append(4)
        if(one[2] == max(one[0],one[1],one[2],one[3],one[4],one[5])):
            y.append(5)
        if (one[3] == max(one[0], one[1], one[2], one[3], one[4], one[5])):
            y.append(6)
        if (one[4] == max(one[0], one[1], one[2], one[3], one[4], one[5])):
            y.append(7)
        if (one[5] == max(one[0], one[1], one[2], one[3], one[4], one[5])):
            y.append(8)
    return y

#归一化
def normalize(dataSet):
    dataSet2 = np.array(dataSet)
    dataSet3 = dataSet2 / dataSet2.max(axis=0)
    dataSet4 = []
    for line in dataSet3:
        dataSet4.append(list(line))
    return dataSet4


def run_by_winequality():
    #加载数据
    dataSet,label,label_bp,label_name=load_uci_winequality(r"E:\文件\机器学习\机器学习数据集\winequality-red.csv")
    # 加载验证集
    checkDataSet, checkLabel = bootstrapping(dataSet, label, 2000)
    #建立模型,隐藏个数随机迭代，取正确率最高的隐层个数
    n=20 #n为次数

    max_true_precent = 0
    bpGood = None
    h_len_max = 0

    for i in range(n):
        h_len = random.randint(6,16)
        bp_wine = bp(11,h_len,6)
        bp_wine.train(dataSet,label_bp,0.1,150)
        #验证
        y_prec = bp_wine.run(checkDataSet)
        #获取正确率
        y = print_winequality_bp(y_prec)
        true_precent = good_conut(y,checkLabel)
        #若正确率更高，则替换
        if(true_precent>max_true_precent):
            max_true_precent = true_precent
            bpGood = bp_wine
            h_len_max = h_len
    #输出预测值和真实值
    print("真实质量")
    print(checkLabel)
    print("预测质量")
    print(print_winequality_bp(bpGood.run(checkDataSet)))
    # 输出正确率
    print("正确率")
    print(max_true_precent)


if __name__ == "__main__":
    run_by_winequality()


