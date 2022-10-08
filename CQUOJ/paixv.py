import configparser  #用于从ini读取结构化文件数据
import random
import time

#定义了一个Country类，用于储存数据
class Country():
    def __init__(self,name,gdp):
        self.sName = name
        self.fGdp = gdp

#加载数据并打乱顺序（引用刘老师的代码）
def ReadIniFile(Inifilename):
    #从countries.ini读取全球GDP前15位至countries列表
    countries = []
    data = configparser.ConfigParser()#初始化
    data.read(Inifilename)#读取文件
    data = data["Countries"]
    iSize = int(data.get("countries.size", 0))
    for i in range(iSize):
        name = data.get("countries[{}].sName".format(i), "ERROR").strip()
        gdp = float(data.get("countries[{}].fGdp".format(i), "0"))
        countries.append(Country(name, gdp))
    print("Countries in random order:")

    return countries


#冒泡排序，输入country结点组成的列表
def MaoPaoPaiXv(ilist):
    #选择第i个元素
    for i in range(1,len(ilist)):
        #对第i个元素和这个元素之前的所有元素进行比较（不断将大的元素排到前面）
        for j in range(i,0,-1):
            #如果第j个元素大于第j-1个元素，则交换元素位置
            if ilist[j].fGdp > ilist[j-1].fGdp:
                ilist[j], ilist[j-1] = ilist[j-1], ilist[j]
    #返回这个列表
    return ilist


#插入排序，输入country结点组成的列表
def ChaRuPaiXv(ilist):
    #储存结果
    jieguo=[]
    #先加入第一个变量
    jieguo.append(ilist[0])
    #循环加入剩下的变量
    for i in range(1,len(ilist)):
        #取出待加入的元素
        paixvyuansu=ilist[i]
        #在已经排序好的列表里插入这个待排序的元素
            #如果他是最小的元素，则加入jieguo最后
        if paixvyuansu.fGdp <= jieguo[-1].fGdp:
            jieguo.append(paixvyuansu)
        else:
            # 找到第一个比他小的元素，把这个元素插入到他前面
            for j in range(len(jieguo)):
                if jieguo[j].fGdp < paixvyuansu.fGdp:
                    jieguo.insert(j,paixvyuansu)
                    break
    #返回这个已经排序好的列表
    return jieguo

#归并排序
def GuiBingPaiXv(ilist):
    #递归分割
    def cutlist(jlist):
        #如果这个列表长度为1，返回这个列表
        if len(jlist)==1:
            return jlist
        #递归分割列表
        left=cutlist(jlist[:(len(jlist)//2)])
        right=cutlist(jlist[(len(jlist)//2):])
        #返回排序好的子列表
        return guibing(left,right)

    #对两个排序好的列表合成一个排序好的列表
    def guibing(left,right):
        #用于储存排序好的列表
        jieguo = []
        #不断取出每个列表第一个元素并比较，取出大的元素加入jieguo列表，然后在原列表删除这个元素，再次进行比较
        #直到至少其中一个列表没有元素
        while len(left)>0 and len(right)>0:
            if left[0].fGdp>right[0].fGdp:
                jieguo.append(left[0])
                del left[0]
            else:
                jieguo.append(right[0])
                del right[0]
        #当一个列表长度为0时，剩下的列表里的元素一定比jieguo这个列表的最后一个元素小，
        # 所以把这个长度不为0的列表扩展到jieguo列表的最后
        if len(left)==0:
            jieguo.extend(right)
        else:
            jieguo.extend(left)
        #返回合并并且排序好的列表
        return jieguo

    #返回排序好的列表
    return cutlist(ilist)

#读取文件并转为列表
countries=ReadIniFile('C:\\Users\\lenovo\\Desktop\\文件\\countries.ini')

random.shuffle(countries)  # 打乱顺序
start=time.clock()
print('冒泡排序')
countries=MaoPaoPaiXv(countries)
used=time.clock()-start
print('冒泡排序用时：',used)
for x in countries:
    print(x.sName,"'s GDP: $",x.fGdp," in billions.")


random.shuffle(countries)   #打乱顺序
start=time.clock()
print('插入排序')
countries=ChaRuPaiXv(countries)
used=time.clock()-start
print('插入排序用时：',used)
for x in countries:
    print(x.sName,"'s GDP: $",x.fGdp," in billions.")


random.shuffle(countries)  # 打乱顺序
start=time.clock()
print('归并排序排序')
countries=GuiBingPaiXv(countries)
used=time.clock()-start
print('归并排序用时：',used)
for x in countries:
    print(x.sName,"'s GDP: $",x.fGdp," in billions.")