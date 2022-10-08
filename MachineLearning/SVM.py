import math
import numpy
import random
import time
import matplotlib.pyplot as plt

def kernelTrans(X, A, kTup):
    """
    Function：   核转换函数

    Input：      X：数据集
                A：某一行数据
                kTup：核函数信息

    Output： K：计算出的核向量
    """
    #获取数据集行列数
    m, n = numpy.shape(X)
    #初始化列向量
    K = numpy.mat(numpy.zeros((m, 1)))
    #根据键值选择相应核函数
    #lin表示的是线性核函数
    if kTup[0] == 'lin': K = X * A.T
    #rbf表示径向基核函数
    elif kTup[0] == 'rbf':
        for j in range(m):
            A = A.astype('float64')
            X=X.astype('float64')
            deltaRow = X[j,:] - A
            K[j] = deltaRow * deltaRow.T
        #对矩阵元素展开计算
        for i in range(numpy.shape(K)[0]):
            for j in range(numpy.shape(K)[1]):
                K[i,j]=math.exp(K[i,j]/(-1*kTup[1]**2))

    #如果无法识别，就报错
    else:
        raise NameError('Houston We Have a Problem -- That Kernel is not recognized')
    #返回计算出的核向量
    return K

class optStructK():
    """
    Function：   存放运算中重要的值

    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                kTup：速度参数

    Output： X：数据集
                labelMat：类别标签
                C：常数C
                tol：容错率
                m：数据集行数
                b：常数项
                alphas：alphas矩阵
                eCache：误差缓存
                K：核函数矩阵
    """
    def __init__(self, dataMatIn, classLabels, C, toler, kTup):
        self.X =  dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = numpy.shape(dataMatIn)[0]
        self.alphas = numpy.mat(numpy.zeros((self.m, 1)))
        self.b = 0
        self.eCache = numpy.mat(numpy.zeros([self.m, 2]))

        """ 主要区分 """
        self.K = numpy.mat(numpy.zeros([self.m, self.m]))
        for i in range(self.m):
            self.K[:,i] = kernelTrans(self.X, self.X[i,:], kTup)
        """ 主要区分 """

def calcEkK(oS, k):
    """
    Function：   计算误差值E

    Input：      oS：数据结构
                k：下标

    Output： Ek：计算的E值
    """

    """ 主要区分 """
    #计算fXk，整个对应输出公式f(x)=w`x + b
    #fXk = float(multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k,:].T)) + oS.b
    fXk = float(numpy.multiply(oS.alphas, oS.labelMat).T*oS.K[:, k] + oS.b)
    """ 主要区分 """

    #计算E值
    Ek = fXk - float(oS.labelMat[k])
    #返回计算的误差值E
    return Ek

def selectJK(i, oS, Ei):
    """
    Function：   选择第二个alpha的值

    Input：      i：第一个alpha的下标
                oS：数据结构
                Ei：计算出的第一个alpha的误差值

    Output： j：第二个alpha的下标
                Ej：计算出的第二个alpha的误差值
    """
    #初始化参数值
    maxK = -1; maxDeltaE = 0; Ej = 0
    #构建误差缓存
    oS.eCache[i] = [1, Ei]
    #构建一个非零列表，返回值是第一个非零E所对应的alpha值，而不是E本身
    validEcacheList = numpy.nonzero(oS.eCache[:, 0].A)[0]
    #如果列表长度大于1，说明不是第一次循环
    if (len(validEcacheList)) > 1:
        #遍历列表中所有元素
        for k in validEcacheList:
            #如果是第一个alpha的下标，就跳出本次循环
            if k == i:
                continue
            #计算k下标对应的误差值
            Ek = calcEkK(oS, k)
            #取两个alpha误差值的差值的绝对值
            deltaE = abs(Ei - Ek)
            #最大值更新
            if (deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        #返回最大差值的下标maxK和误差值Ej
        return maxK, Ej
    #如果是第一次循环，则随机选择alpha，然后计算误差
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEkK(oS, j)
    #返回下标j和其对应的误差Ej
    return j, Ej

def updateEkK(oS, k):
    """
    Function：   更新误差缓存

    Input：      oS：数据结构
                j：alpha的下标

    Output： 无
    """
    #计算下表为k的参数的误差
    Ek = calcEkK(oS, k)
    #将误差放入缓存
    oS.eCache[k] = [1, Ek]

def innerLK(i, oS):
    """
    Function：   完整SMO算法中的优化例程

    Input：      oS：数据结构
                i：alpha的下标

    Output： 无
    """
    #计算误差
    Ei = calcEkK(oS, i)
    #如果标签与误差相乘之后在容错范围之外，且超过各自对应的常数值，则进行优化
    if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        #启发式选择第二个alpha值
        j, Ej = selectJK(i, oS, Ei)
        #利用copy存储刚才的计算值，便于后期比较
        alphaIold = oS.alphas[i].copy(); alpahJold = oS.alphas[j].copy();
        #保证alpha在0和C之间
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS. alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        #如果界限值相同，则不做处理直接跳出本次循环
        if L == H:
            print("L==H")
            return 0

        """ 主要区分 """
        #最优修改量，求两个向量的内积（核函数）
        #eta = 2.0 * oS.X[i, :]*oS.X[j, :].T - oS.X[i, :]*oS.X[i, :].T - oS.X[j, :]*oS.X[j, :].T
        eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j]
        """ 主要区分 """

        #如果最优修改量大于0，则不做处理直接跳出本次循环，这里对真实SMO做了简化处理
        if eta >= 0: print("eta>=0"); return 0
        #计算新的alphas[j]的值
        oS.alphas[j] -= oS.labelMat[j]*(Ei - Ej)/eta
        #对新的alphas[j]进行阈值处理
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        #更新误差缓存
        updateEkK(oS, j)
        #如果新旧值差很小，则不做处理跳出本次循环
        if (abs(oS.alphas[j] - alpahJold) < 0.00001): print("j not moving enough"); return 0
        #对i进行修改，修改量相同，但是方向相反
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alpahJold - oS.alphas[j])
        #更新误差缓存
        updateEkK(oS, i)

        """ 主要区分 """
        #更新常数项
        #b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[i, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[i, :]*oS.X[j, :].T
        #b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[j, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[j, :]*oS.X[j, :].T
        b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, i] - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.K[i, j]
        b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, j] - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.K[j, j]
        """ 主要区分 """

        #谁在0到C之间，就听谁的，否则就取平均值
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[i]): oS.b = b2
        else: oS.b = (b1 + b2) / 2.0
        #成功返回1
        return 1
    #失败返回0
    else: return 0

def smoPK(dataMatIn, classLabels, C, toler, maxIter, kTup = ('lin', 0)):
    """
    Function：   完整SMO算法

    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                maxIter：最大的循环次数
                kTup：速度参数

    Output： b：常数项
                alphas：数据向量
    """
    #新建数据结构对象
    oS = optStructK(numpy.mat(dataMatIn), numpy.mat(classLabels).transpose(), C, toler, kTup)
    #初始化迭代次数
    iter = 0
    #初始化标志位
    entireSet = True; alphaPairsChanged = 0
    #终止条件：迭代次数超限、遍历整个集合都未对alpha进行修改
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        #根据标志位选择不同的遍历方式
        if entireSet:
            #遍历任意可能的alpha值
            for i in range(oS.m):
                #选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerLK(i, oS)
                print("fullSet, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            #迭代次数累加
            iter += 1
        else:
            #得出所有的非边界alpha值
            nonBoundIs = numpy.nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            #遍历所有的非边界alpha值
            for i in nonBoundIs:
                #选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerLK(i, oS)
                print("non-bound, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            #迭代次数累加
            iter += 1
        #在非边界循环和完整遍历之间进行切换
        if entireSet: entireSet = False
        elif (alphaPairsChanged == 0): entireSet =True
        print("iteration number: %d" % iter)
    #返回常数项和数据向量
    return oS.b, oS.alphas

def selectJrand(i, m):
    """
    Function：   随机选择

    Input：      i：alpha下标
                m：alpha数目

    Output： j：随机选择的alpha下标
    """
    #初始化下标j
    j = i
    #随机化产生j，直到不等于i
    while (j == i):
        j = int(random.uniform(0,m))
    #返回j的值
    return j

def clipAlpha(aj, H, L):
    """
    Function：   设定alpha阈值

    Input：      aj：alpha的值
                H：alpha的最大值
                L：alpha的最小值

    Output： aj：处理后的alpha的值
    """
    #如果输入alpha的值大于最大值，则令aj=H
    if aj > H:
        aj = H
    #如果输入alpha的值小于最小值，则令aj=L
    if L > aj:
        aj = L
    #返回处理后的alpha的值
    return aj


def calcWs(alphas, dataArr, classLabels):
    """
    Function：   计算W

    Input：      alphas：数据向量
                dataArr：数据集
                classLabels：类别标签

    Output： w：w*x+b中的w
    """
    #初始化参数
    X = numpy.mat(dataArr); labelMat = numpy.mat(classLabels).transpose()
    #获取数据行列值
    m,n = numpy.shape(X)
    #初始化w
    w = numpy.zeros((n,1))
    #遍历alpha，更新w
    for i in range(m):
        w += numpy.multiply(alphas[i]*labelMat[i],X[i,:].T)
    #返回w值
    return w

def jiexitxt(filename):
    dataSet = []
    labels=[]
    with open(filename, 'r', encoding='UTF-8') as io:
        txterwei = io.readlines()
        for line in txterwei:
            line = line.strip('\ufeff')
            # 剔除开头结尾的空字符
            line = line.strip()
            # 在以\t分界转化为列表
            linelist = line.split('\t')
            # 将列表内容转变为int
            for i in range(len(linelist)):
                linelist[i] = float(linelist[i])
            # 将这个列表加入list
            dataSet.append(linelist[:-1])
            labels.append(linelist[-1])
    return dataSet,labels

#计算数据并且画出图像
def draw(dataSet,labels,w,b):
    error=0
    result=numpy.array(numpy.dot(dataSet,w)) + b[0,0]
    print(result)

    '''    if (int(result[i])>1 and labels[i]=='1') or (int(result[i])<-1 and labels[i]=='-1'):
            continue
        else:
            error+=1
    print('错误率：',error/dataSet.shape[1])'''




start_0=time.clock()
start=time.clock()
dataSet,labels=jiexitxt('D:\works\shujv\TestSetRBF.txt')
used=time.clock()-start
print('读取文件时间为：',used)

dataSet=numpy.matrix(dataSet)




start=time.clock()
os=optStructK(dataSet,labels,0.6,0.001,('rbf',40))
used=time.clock()-start
print('文件高维转化时间为：',used)

start=time.clock()
b,alp=smoPK(dataSet,labels,0.6,0.001,50,('rbf',40))
used=time.clock()-start
print('b，alp计算时间为：',used)

start=time.clock()
w=calcWs(alp,dataSet,labels)
used=time.clock()-start
print('w求解时间为：',used)


print('最优化w',w)
print('最优化b',b)

end=time.clock()
print('程序运行时间：',(end-start_0)/60,'分钟')
draw(dataSet,labels,w,b)