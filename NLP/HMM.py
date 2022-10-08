
import re
import time

class HMM():
    #状态符号的集合S，输出符号的集合K
    def __init__(self,S,K):
        self.S = S[:]
        self.K = K[:]
        self.a = len(S)
        self.b = len(K)
        #状态转移矩阵 Aij表示状态Si转移到Sj的概率
        self.A = [[1/self.a for j in range(self.a)]for i in range(self.a)]
        #符号发射矩阵 Bij表示状态Si时输出Kj的概率
        self.B = [[0 for j in range(self.b)]for i in range(self.a)]
        #初始状态矩阵 pi(i)表示初始状态为Si的概率
        self.pi = [1/self.a for i in range(self.a)]

    '''
    #采用有监督样本训练A,B,pi
    #采用最大似然估计，输入观测序列的集合dataSetO和状态序列的集合dataSetQ
    def train_has_label(self,dataSetO,dataSetQ):
        print("开始训练")
        n1 = len(dataSetQ)
        n2 = len(dataSetO)
        if(n1!=n2):
            return
        for x in range(n1):
            print(x)
            Q = dataSetQ[x]
            O = dataSetO[x]
            T = len(Q)
            #最大似然估计
            for j in range(self.a):
                self.pi[j] += self.Kronecker(Q[0],self.S[j])/n1
            for i in range(self.a):
                for j in range(self.a):
                    fenzi = 0
                    fenmu = 0
                    for t in range(T-1):
                        fenzi += self.Kronecker(Q[t],self.S[i])*self.Kronecker(Q[t+1],self.S[j])
                        fenmu += self.Kronecker(Q[t],self.S[i])
                    if(fenmu!=0):
                        self.A[i][j] += (fenzi/fenmu)/n1

            for j in range(self.a):
                for k in range(self.b):
                    fenzi = 0
                    fenmu = 0
                    for t in range(T):
                        fenzi += self.Kronecker(Q[t],self.S[j]) * self.Kronecker(O[t],self.K[k])
                        fenmu += self.Kronecker(Q[t],self.S[j])

                    if (fenmu != 0):
                        self.B[j][k] += (fenzi/fenmu)/n1
        print(self.B)
        print(self.A)
        print(self.pi)
        print("训练完成")
    '''

    # 采用有监督样本训练B
    # 采用最大似然估计，输入观测序列的集合dataSetO和状态序列的集合dataSetQ
    def train_B(self,dataSetO,dataSetQ):
        print("开始训练B")
        n1 = len(dataSetQ)
        for x in range(n1):
            try:
                Q = dataSetQ[x]
                O = dataSetO[x]
                T = len(Q)
                for t in range(T):
                    j = self.S.index(Q[t])
                    k = self.K.index(O[t])
                    self.B[j][k] += 1
            except:
                continue
        for i in range(self.a):
            sumB = sum(self.B[i])
            if(sumB!=0):
                for j in range(self.b):
                    self.B[i][j] = self.B[i][j]/sumB

        print("B训练完成")

    # 采用有监督样本训练A,pi
    # 采用最大似然估计，状态序列的集合dataSetQ
    def train_A_and_pi(self,dataSetQ):
        print("开始训练A,pi")
        n1 = len(dataSetQ)
        for x in range(n1):
            try:
                Q = dataSetQ[x]
                T = len(Q)
                #最大似然估计
                #找出Q[0]的索引
                j = self.S.index(Q[0])
                self.pi[j] += 1
                for t in range(T-1):
                    i = self.S.index(Q[t])
                    j = self.S.index(Q[t+1])
                    self.A[i][j] += 1
            except:
                continue
        sumPi = sum(self.pi)
        for i in range(self.a):
            self.pi[i] = self.pi[i] / sumPi
        for i in range(self.a):
            sumA = sum(self.A[i])
            if(sumA!=0):
                for j in range(self.a):
                    self.A[i][j] = self.A[i][j]/sumA
        print("训练完成A,pi")

    #科罗奈克函数
    def Kronecker(self,a,b):
        if(a==b):
            return 1
        else:
            return 0


    #维特比算法求解路径，输入一个序列，即K中元素组成的序列，输出最佳的S的序列
    def viterbi(self,one_list):
        print(one_list)
        T =  len(one_list)
        #初始化viterbi变量
        viterbiX = [[0 for i in range(self.a)]for j in range(T)]
        for i in range(self.a):
            viterbiX[0][i] = self.pi[i] * self.B[i][self.K.index(one_list[0])]
        # 初始化路径
        path = [[0 for i in range(self.a)]for j in range(T)]
        for i in range(self.a):
            path[0][i] = 0
        #动态规划计算
        for t in range(1,T,1):
            for j in range(self.a):
                #找出最大值
                maxVi = -1
                max_i = -1
                for i in range(self.a):
                    Vi = viterbiX[t-1][i] * self.A[i][j]
                    if(Vi>maxVi):
                        maxVi = Vi
                        max_i = i
                #更新维特比变量
                viterbiX[t][j] = maxVi * self.B[j][self.K.index(one_list[t])]
                #记录路径
                path[t][j] = max_i
        #找出T时最大的维特比变量
        maxQVi = -1
        max_Q = -1
        for i in range(self.a):
            if(viterbiX[T-1][i]>maxQVi):
                maxQVi = viterbiX[T-1][i]
                max_Q = i
        #路径回溯，找出状态序列
        list_q = [self.S[max_Q]]
        qt = max_Q
        for t in range(T-2,-1,-1):
            qt = path[t+1][qt]
            list_q.append(self.S[qt])
        #顺序反转
        list_q.reverse()
        return list_q



def load_index(index_path,test_a,word):
    #汉字为状态序列，拼音为观察序列
    dataSetQ = []
    QkindList = set()
    dataSetO = []
    OkindList = set()

    listcharSet = test_a[:]
    listcharSet.extend(word)


    with open(index_path,'r',encoding='utf-8-sig') as f:
        for line in f.readlines():
            line_list = line.strip("\n").split(" ")
            for char in line_list[1]:
                 for str in listcharSet:
                     if(char in str):
                         dataSetO.append([line_list[0]])
                         OkindList.add(line_list[0])
                         dataSetQ.append([char])
                         QkindList.add(char)
                         break


    return dataSetQ,dataSetO,list(QkindList),list(OkindList)


def load_data(dataSet_path,maxNum=300000):
    list_str =[]
    with open(dataSet_path, 'r', encoding='utf-8-sig') as f:
        for line in f.readlines():
            str = line.strip("_!_").split("_!_")[3]
            #只保留中文
            str = ''.join(re.findall(r'[\u4e00-\u9fa5]', str))
            list_str.append(str)
            if(len(list_str)>=maxNum):
                break
    return list_str

#加载测试集
def load_test_data(test_data_path):
    dataSet =[]
    labels = []
    i = 0
    with open(test_data_path, 'r', encoding='ANSI') as f:
        for line in f.readlines():
            str = line.strip("\n")
            if(i%2==1):

                dataSet.append(str)
            else:
                labels.append(str)
            i+=1
    return dataSet,labels


if __name__ == "__main__":
    t1 =time.time()
    words,pinyin = load_test_data(r"E:\文件\NLP\测试集.txt")

    #训练A使用
    test_a = load_data(r"E:\文件\NLP\toutiao_cat_data.txt",20000)
    #训练B使用
    dataSetQ,dataSetO,QkindList,OkindList=load_index(r"E:\文件\NLP\pinyin2hanzi.txt",test_a,words)
    t2 = time.time()
    print("数据集加载时间：",t2-t1)
    hmm = HMM(QkindList,OkindList)
    #训练转移概率
    hmm.train_A_and_pi(test_a)


    #训练发射概率
    hmm.train_B(dataSetO,dataSetQ)

    t3 = time.time()
    print("训练时间：", t3 - t2)
    #测试
    conut = 0
    sum_conut = 0
    for i in range(len(pinyin)):
        yprec_words = hmm.viterbi(pinyin[i].strip(" ").lower().split(" "))
        for j in range(len(yprec_words)):
            sum_conut+=1
            if(yprec_words[j]==words[i][j]):
                conut+=1
        print(yprec_words)
    t4 = time.time()
    print("维特比算法平均耗时:",(t4 - t3)/len(pinyin))
    print("正确率")
    print(conut/sum_conut)