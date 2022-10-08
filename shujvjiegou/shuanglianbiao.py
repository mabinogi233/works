class node():
    def __init__(self,data):    #生成一个节点
        self.prev=None
        self.data=data
        self.next=None
    def getdata(self):
        return self.data

class DoubleList():
    def __init__(self): #生成一个双链表
        self.head=None
        self.lenght=0
        self.tail=None

    def DestroyList(self):  #摧毁双链表
        self.head=None
        self.lenght=0
        self.tail=None

    def GetLenght(self):#   获取链表长度
        return self.lenght

    def GetElem(self,i):    #获取第i个结点中的元素的值
        if i <= self.lenght:
            a = self.head
            if i == 1:
                return a.getdata()
            else:
                for j in range(i - 1):
                    a = a.next
                return a.getdata()
        else:
            return None

    def GetValue(self,value):   #获取值为value的元素对应的索引
        a = self.head
        j = 1
        index = []
        while j <= self.lenght:
            if value == a.getdata():
                index.append(j)
            a = a.next
            j = j + 1
        if index != []:
            return index
        else:
            return -1    #不存在返回None

    def IntElem(self,i,value):  #将值value插入为第i个元素
        a=self.head
        if i<=self.lenght:
            if i==1:        #i为1
                value.next=a
                a.prev=value
                self.head=value
                self.lenght+=1
                print('添加成功')
            else:
                j=1
                while j<i-1:
                    a=a.next
                    j=j+1
                value.next=a.next
                value.prev=a
                a.next.prev=value
                a.next=value
                self.lenght+=1
                print('添加成功')
        else:
            print('添加失败')

    def DelElem(self,i):#删除第i个元素
        a=self.head
        if i<=self.lenght:
            if i==1:
                a.next.prev=None
                self.head=a.next
                self.lenght=self.lenght-1
                print('删除成功')
            elif i==self.lenght:
                j=1
                while j<i-1:
                    a=a.next
                    j+=1
                a.next.prev=None
                a.next=None
                self.tail=a
                self.lenght+=-1
                print('删除成功')
            else:
                j = 1
                while j < i - 1:
                    a = a.next
                    j += 1
                a.next.next.prev=a
                a.next.prev=None
                a.next=a.next.next
                self.lenght+=-1
                print('删除成功')
        else:
            print('删除失败，超出索引范围')

    def append(self,node):#将node插入链表最后
        a = self.head
        if a != None:
            if a.next != None:
                while a.next != None:
                    a = a.next
                a.next = node
                node.prev=a
                self.tail=node
                self.lenght = self.lenght + 1
            else:
                a.next = node
                node.prev=a
                self.tail=node
                self.lenght = self.lenght + 1
        else:
            self.head = node
            self.lenght = self.lenght + 1

    def DispList(self):     #遍历链表
        if self.head != None:
            a=self.head
            print(a.getdata())
            while a.next != None:
                a=a.next
                print(a.getdata())
        else:
            print('表为空')


    def reserve(self):      #倒置链表
        a=self.head
        while a.next!=None:
            a.next,a.prev=a.prev,a.next
            a=a.prev
        a.next,a.prev=a.prev,a.next
        self.head,self.tail=self.tail,self.head

    def updata(self,i,data):    #修改第i个元素的值
        a=self.head
        j = 1
        while j < i :
            a = a.next
            j += 1
        a.data=data
        print('修改成功')

lianbiao=DoubleList()
node_1=node(1)
node_2=node(2)
node_3=node(3)
lianbiao.append(node_1)
lianbiao.append(node_2)
lianbiao.append(node_3)
node_4=node(4)
lianbiao.updata(2,4)

print('正序输出')
lianbiao.DispList()  #成功
print('倒序输出')
lianbiao.reserve()
lianbiao.DispList()



