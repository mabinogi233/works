class shuxvbiao():
    def __init__(self,max=8):   #创建一个有max个单元的顺序表
        self.max=max
        self.min=0
        self.list=[None] * self.max
        self.len=0

    def detate(self):       #删除顺序表
        del self.list

    def Getlength(self):        #获取顺序表的长度
        return self.len

    def GetElem(self,i):      #获取顺序表第i个元素
        if i <= self.len:
            return self.list[i-1]
        else:
            return None             #不存在返回None

    def GetValue(self,value):     #获取顺序表中值为值为value的元素的(逻辑序号)索引组成的列表
        j=0
        index=[]
        for i in range(self.len):
            if self.list[i]==value:
                j=1
                index.append(i+1)
        if j ==0:
            return -1           #不存在则返回-1
        else:
            return index

    def InsElem(self,item,i):   #将m插入第i位置，并使长度加一(m是第i个元素)
        if i <= self.len :
            for j in range(self.len,i-1,-1):
                self.list[j]=self.list[j-1]
            self.list[i-1]=item
            self.len=self.len+1
            print(item,' 添加成功')
        else:
            print(item,' 添加失败')

    def DelElem(self,i):    #删除第i个元素
        if i <= self.len:
            for j in range(i,self.len):
                self.list[j-1]=self.list[j]
            self.len=self.len-1
            print('删除成功')
        else:
            print('删除失败')

    def DispList(self):     #顺序遍历顺序表
        for i in range(self.len):
            print(self.list[i])

    def append(self,item):   #在顺序表末尾加入元素
        self.list[self.len]=item
        self.len=self.len+1

list=shuxvbiao(16)  #创建最大长为16的顺序表
list.append(21)
list.append(22)
list.append(70)
list.InsElem(50,4)
list.InsElem(25,2)
list.DispList()
print('线性表的长度为 ',list.Getlength())
a=list.GetValue(22)     #获取值为25的元素的逻辑索引组成的列表
print(a)
b=list.GetElem(2)       #获取第二个元素
print(b)
list.DelElem(2)
list.DispList()
list.detate()

