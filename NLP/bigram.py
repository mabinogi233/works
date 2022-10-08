import time
import random
import sys



#二元划分bigram模型
class bigram:
    #初始化模型，输入index_file_path作为bigram模型索引文件的路径，索引储存所有词对的频率（ c<w(i-1),w(i)> ）
    # 索引结构，key-value，key为(w(i-1))，可以根据(w(i-1))找出其后出现的所有词(w(i))的出现次数
    # { w(i-1) ：{w(i1): c1 ,w(i2): c2 } , ……}
    def __init__(self,index_file_path="D:\\bigram.txt"):
        self.index_file_path = index_file_path
        self.saveIndex({},self.index_file_path)

    #训练模型，目的是得到所有词对的频率（ c<w(i-1),w(i)> ）
    def train(self,dataSet):
        #预处理
        line_by_sentence_dataSet = self.pred_product_DataSet(dataSet)
        #计算词对频率并更新索引
        self.update_index(line_by_sentence_dataSet)

    #句子预处理
    def pred_product_DataSet(self,dataSet):
        line_by_sntence_dataSet=[]
        for line in dataSet:
            if(line=="\n"):
                continue
            list_line = line.strip("\n").strip("\t").split("  ")
            #替换标记为句首标记
            list_line[0] = "<BOS>"
            #删除词性标记
            for i in range(len(list_line)):
                list_line[i] = (list_line[i].split("/"))[0]
            #添加句尾标记
            list_line.append("<EOS>")
            line_by_sntence_dataSet.append(list_line)
        return line_by_sntence_dataSet


    #更新索引
    def update_index(self,line_by_sntence_dataSet):
        #索引结构，key-value，key为(w(i-1))，可以根据(w(i-1))找出其后出现的所有词(w(i))的出现次数
        # { w(i-1) ：{w(i1): c1 ,w(i2): c2 } , ……}
        #line_by_sntence_dataSet的格式为 [<BOS> ,A ,B ,C ,D , ... , <EOS>]

        index_file_path = self.index_file_path
        #获取索引
        dict_index = self.getIndex(index_file_path)
        #更新索引
        for sentence in line_by_sntence_dataSet:
            #<EOS>标志没有后继词
            for i in range(len(sentence)-1):
                #索引中不存在这个词
                if(sentence[i] not in dict_index):
                    dict_index[sentence[i]]={}
                #此时索引中一定存在sentence[i]这个词（这个词作为w（i-1））
                #dict_index_in_word  =  {w(i1): c1 ,w(i2): c2 }
                dict_index_in_word = dict_index[sentence[i]]
                #获取这个词的下一个词，若下个词不在dict_index_in_word中，则初始化为0
                if(sentence[i+1] not in dict_index_in_word):
                    dict_index_in_word[sentence[i+1]]=str(0)
                #此时将词sentence[i+1]的出现次数+1 ,(格式为str)
                dict_index_in_word[sentence[i + 1]] = str(int(dict_index_in_word[sentence[i + 1]])+1)
                #处理完毕，恢复dict_index_in_word
                dict_index[sentence[i]]=dict_index_in_word
        #保存索引
        self.saveIndex(dict_index,index_file_path)


    #获取索引
    def getIndex(self,index_file_path):
        with open(index_file_path, 'r', encoding='utf-8') as f:
            dict = eval(f.read())
        return dict

    # 存储索引
    def saveIndex(self,dict,index_file_path):
        if isinstance(dict, str):
            dict = eval(dict)
        with open(index_file_path, 'w', encoding='utf-8') as f:
            f.write(str(dict))

    def fit(self,dataSety,xita=0.8):
        conut_i = 0
        ps = []
        for onedata in dataSety:
            ps.append(self.fit_one_data(onedata,xita))
            conut_i+=1
            if(conut_i%10==0):
                print("成功计算 "+str(conut_i)+" 条语句的概率")
        return ps

    #计算一条句子出现的概率，xita为加法平滑的参数，[0,1]，默认为0.8
    def fit_one_data(self,one_data,xita=0.8):
        p = 1
        #输入分词好的结果 eg：['迈向','充满','希望','的','新','世纪']
        data = one_data[:]
        data.insert(0,"<BOS>")
        data.append("<EOS>")
        #获取索引
        dict_index = self.getIndex(self.index_file_path)
        for i in range(len(data)-1):
            wi_1 = data[i]
            wi = data[i+1]
            #使用加法平滑
            #计算 p （ wi | wi_1） = （θ + c (wi_1,wi)） / （ c （wi_1） + θ*|V|）  θ属于[0,1]
            if(wi_1 not in dict_index):
                #对于未知词的处理（分母不存在）
                #近似认为未知词之后的词的出现频率均为θ
                # p = θ / dict_index的键的数目
                p *= xita / len(dict_index.keys())
                continue
            dict_wi_1 = dict_index[wi_1]
            V = 0
            c_wi_1__wi = xita
            c_wi_1__wi_sum = 0
            for word,conut in dict_wi_1.items():
                if(word==wi):
                    c_wi_1__wi += int(conut)
                c_wi_1__wi_sum+=(xita+int(conut))
            p_w = c_wi_1__wi/c_wi_1__wi_sum
            #乘入句子的概率
            p*=p_w
        return p

    #找出备选词语
    def find_word(self,one_sentence):
        index_file_path = self.index_file_path
        # 获取索引
        dict_index = self.getIndex(index_file_path)
        self.index = dict_index
        return self.find_one_word(one_sentence)

    #找出所有的切分方法
    def find_one_word(self,sentence):
        list_dict_index = [[0 for i in range(len(sentence))]for j in range(len(sentence))]
        list_dict = [["" for i in range(len(sentence))] for j in range(len(sentence))]
        for i in range(len(sentence)):
            for j in range(i,len(sentence),1):
                if(sentence[i:j+1] in self.index.keys()):
                    list_dict_index[i][j] = 1
                    list_dict[i][j]=sentence[i:j+1]

        self.list_dict=list_dict
        list_words = []
        self.find_by_word_dict(list_dict_index,0,[],list_words)
        return list_words

    #递归找到组合
    def find_by_word_dict(self,list_dict_index,i,list_p,list_words):
        if(i==len(list_dict_index)):
            list_words.append(list_p[:])
            #print(list_p)
            return
        for j in range(len(list_dict_index)):
            if(list_dict_index[i][j]==1):
                list_p.append(self.list_dict[i][j])
                self.find_by_word_dict(list_dict_index,j+1,list_p,list_words)
                del list_p[-1]

    #找出概率最大的切分策略
    def cut(self,sentence):
        list_cut = self.find_word(sentence)
        print("所有切分方法如下：")
        for i in list_cut:
            print(i)
        maxP = -1
        bestCut = []
        #选择概率最大的切分
        if(list_cut!=None):
            for one_cut in list_cut:
                p = self.fit_one_data(one_cut)
                if(p>maxP):
                    maxP = p
                    bestCut = one_cut
        print("最大概率：",maxP)
        print("最佳切分")
        return bestCut

def loadDataSet():
    conut_i = 0
    dataSet = []
    dataSety = []
    print("开始读取数据集")
    with open(r"D:\QQ\1091324348\FileRecv\\199801.txt", 'r', encoding='utf-8')as f:
        for line in f.readlines():
            ri = random.randint(1, 30)
            if (ri == 1 and conut_i<500):
                if (line == "\n"):
                    continue
                list_line = line.strip("\n").strip("\t").split("  ")
                # 删除时间戳
                del list_line[0]
                # 删除词性标记
                for i in range(len(list_line)):
                    list_line[i] = (list_line[i].split("/"))[0]
                dataSety.append(list_line)
                conut_i+=1
            else:
                dataSet.append(line)
    return dataSet,dataSety





if __name__ =="__main__":
    t1 = time.time()
    dataSet,dataSety = loadDataSet()
    t2 = time.time()
    print("数据集读取完毕 读取时间 = "+str(t2-t1)+"秒")
    testModel = bigram(r"D:\试验田\test_data\x.txt")
    t3 = time.time()
    print("模型创建完毕  创建时间 = "+str(t3-t2)+"秒")
    testModel.train(dataSet)
    t4 = time.time()
    print("模型训练完毕  训练时间 = "+str(t4-t3)+"秒")
    # p = testModel.fit(dataSety)
    print("切分测试")
    print(testModel.cut("系统测试"))
    '''
    print("开始输出预测结果")
    for i in range(len(p)):
        print("语句： ",end="")
        print(dataSety[i],end="")
        print("  的概率为：  ",end="")
        print(p[i])
    '''