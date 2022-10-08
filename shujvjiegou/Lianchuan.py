class Node():   #链串的结点
    def __init__(self,data):
        self.data=data
        self.next=None

class LianString():
    def __init__(self):
        self.head=None
        self.lenght=0

    def Assign(self, list):  # 串赋值
        for i in range(len(list)):
            node=Node(list[i])
            a = self.head
            if a != None:
                if a.next != None:
                    while a.next != None:
                        a = a.next
                    a.next = node
                    self.lenght = self.lenght + 1
                else:
                    a.next = node
                    self.lenght = self.lenght + 1
            else:
                self.head = node
                self.lenght = self.lenght + 1

    def DestroyList(self):  # 销毁这个链串
        self.head = None
        self.lenght=0

    def StringCopy(self): #串复制
        b=LianString()
        b.head=self.head
        b.lenght=self.lenght
        return b

    def DispList(self):  # 遍历单链表
        if self.head != None:
            a = self.head
            print(a.data)
            while a.next != None:
                a = a.next
                print(a.data)
        else:
            print('串为空')

    def GetLenght(self):        #获取链串的长度
        return self.lenght

def StringEqual(String, anotherString): #比较两个串是否相等
    if String.GetLenght() != anotherString.GetLenght():
        return False
    else:
        i = 1
        a=String.head
        b=anotherString.head
        for j in range(String.lenght):
            if a.data!=b.data:
                i = 0
            a=a.next
            b=b.next
        if i==0:
            return False
        else:
            return True

def Concat(String, String_2):  # 链接两个串
    String_1=String.StringCopy
    a=String_1.head
    for j in range(String_1.lenght - 1):  # 查找第SunString_1.lenght个结点
        a = a.next
    a.next=String_2.head
    String_1.lenght+=String_2.lenght
    return String_1

def SubString(LianString_1, i, j):  # 返回串从i位置开始的j个字符组成的子串
    if i + j - 1 <= LianString_1.lenght:
        a=LianString_1.head
        for m in range(i - 1):  # 查找第i个结点
            a = a.next
        b=LianString()
        b.head=a
        c=b.head
        for m in range(j-1):
            c= c.next
        c.next=None
        b.lenght=j
        return b
    else:
        return None

def DelString(LianString, i, j):  # 删除串中从第i个位置开始的j个字符
    LianString_1=LianString.StringCopy()
    if i + j - 1 <= LianString_1.lenght:
        a = LianString_1.head
        for m in range(i - 2):  # 查找第i-1个结点
            a = a.next
        b= LianString_1.head
        for m in range(i+j - 1):  # 查找第i+j个结点
            b = b.next
        a.next=b
        LianString_1.lenght=LianString.lenght-j
        return LianString_1
    else:
        return None

def InsString(LianString,LianString_2,i):  # 将顺序串2插入顺序串1的第i个位置
    LianString_1=LianString.StringCopy()
    a = LianString_1.head
    for m in range(i - 1):  # 查找第i个结点
        a = a.next
    b = LianString_2.head
    for m in range(LianString_2.lenght - 1):  # 查找第LianString_2.lenght个结点
        b = b.next
    b.next=a
    c=LianString_1.head
    for m in range(i - 2):  # 查找第i-1个结点
        c = c.next
    c.next=LianString_2.head
    LianString_1.lenght=LianString.lenght+LianString_2.lenght
    return LianString_1

def Index(LianString_1, zichuan): # 返回子串在顺序串的位置组成的列表
    index=[]
    end=[]
    a = LianString_1.head
    m=0
    while m < LianString_1.lenght -1:  # 查找第i个结点
        if a.data==zichuan.head.data and m+zichuan.lenght<=LianString_1.lenght:
            index.append(m+1)
            m = m + zichuan.lenght - 1
        a = a.next
        m+=1
    if index!=[]:
        for i in range(len(index)):
            jieguo = SubString(LianString_1, index[i], zichuan.lenght)
            if jieguo.head.data != None:
                boor = StringEqual(jieguo, zichuan)
                if boor == True:
                    end.append(index[i])
        if end == []:
            return None
        else:
            return end
    else:
        return None

lianchuan_1=LianString()
lianchuan_1.Assign([1,2,3,4,5])
lianchuan_2=LianString()
lianchuan_2.Assign([1,2,3])
lianchuan_3=LianString()
lianchuan_3.Assign([5,6,7])

