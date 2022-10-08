class SunString():
    def __init__(self): #生成串
        self.data = None
        self.lenght = 0

    def Assign(self, list): #串赋值
        self.data = [None] * len(list)
        for i in range(len(list)):
            self.data[i] = list[i]
        self.lenght = len(list)
        print('赋值成功')

    def DestroyString(self):    #摧毁串
        self.data = None
        self.lenght=0

    def StringCopy(self):   #获取串的拷贝
        fuben = SunString()
        fuben.Assign(self.data)
        return fuben

    def StringLenght(self): #获取串的长度
        return self.lenght

    def DispString(self):  # 输出串中所有字符
        for i in range(self.lenght):
            print(self.data[i])


def StringEqual(String, anotherString): #比较两个串是否相等
    if String.StringLenght() != anotherString.StringLenght():
        return False
    else:
        i = 1
        for j in range(String.StringLenght()):
            if String.data[j] != anotherString.data[j]:
                i = 0
        if i==0:
            return False
        else:
            return True


def Concat(SunString_1, SunString_2):  # 链接两个串
    r = SunString()
    r.data = [None] * (SunString_1.lenght + SunString_2.lenght)
    for i in range(SunString_1.lenght):
        r.data[i] = SunString_1.data[i]
    for i in range(SunString_2.lenght):
        r.data[SunString_1.lenght + i] = SunString_2.data[i]
    r.lenght = SunString_1.lenght + SunString_2.lenght
    return r


def SubString(SunString_1, i, j):  # 返回串从i位置开始的j个字符组成的子串
    if i + j - 1 <= SunString_1.lenght:
        jieguo = SunString()
        jieguo.data = [None] * j
        jieguo.lenght=j
        for m in range(i, i + j,1):
            jieguo.data[m - i] = SunString_1.data[m-1]
        return jieguo
    else:
        return None


def Index(SunString_1, zichuan): # 返回子串在顺序串的位置组成的列表
    index=[]
    head=zichuan.data[0]
    end=[]
    i=0
    while i < SunString_1.lenght:
        if SunString_1.data[i]==head and i+zichuan.lenght<=SunString_1.lenght:
            index.append(i+1)
            i=i+zichuan.lenght-1
        i+=1
    if index!=[]:
        for i in range(len(index)):
            jieguo=SubString(SunString_1,index[i],zichuan.lenght)
            if jieguo!=None:
                boor=StringEqual(jieguo,zichuan)
                if boor ==True:
                    end.append(index[i])
        if end==[]:
            return None
        else:
            return end
    else:
        return None


def InsString(SunString_1,SunString_2,i):  # 将顺序串2插入顺序串1的第i个位置
    if i<SunString_1.lenght:
        r = SunString()
        r.data = [None] * (SunString_1.lenght + SunString_2.lenght)
        for j in range(i - 1):
            r.data[j] = SunString_1.data[j]
        for j in range(SunString_2.lenght):
            r.data[i - 1 + j] = SunString_2.data[j]
        for j in range(SunString_1.lenght - i + 1):
            r.data[i - 1 + SunString_2.lenght + j] = SunString_1.data[i - 1 + j]
        r.lenght = SunString_1.lenght + SunString_2.lenght
        return r
    else:
        return None

def DelString(SunString_1, i, j):  # 删除串中从第i个位置开始的j个字符
    if i+j<=SunString_1.lenght:
        r = SunString()
        r.lenght = SunString_1.lenght - j
        r.data = [None] * (SunString_1.lenght - j)
        for m in range(i - 1):
            r.data[m] = SunString_1.data[m]
        for m in range(r.lenght - i + 1):
            r.data[i - 1 + m] = SunString_1.data[i - 1 + j + m]
        return r
    else:
        return None

def RepSteing(SunString_1,s1,s2): # 将串中所有出现的子串s1换为s2
    list=Index(SunString_1,s1)
    if list!=None and s1.lenght==s2.lenght:
        for i in range(len(list)):
            for j in range(s1.lenght):
                SunString_1.data[list[i]+j-1]=s2.data[j]
        return SunString_1
    else:
        return None

chuan_1=SunString()
chuan_1.Assign([1,1,1,1])
chuan_2=SunString()
chuan_2.Assign([1,1])
chuan_3=SunString()
chuan_3.Assign([3,4])
r=RepSteing(chuan_1,chuan_2,chuan_3)
r.DispString()





