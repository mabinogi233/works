class Node():   #单链表的结点
    def __init__(self,data):
        self.data=data
        self.next=None

    def getdata(self):  #返回结点储存数据
        return self.data


class InitLsit():
    def __init__(self):         #创建一个单链表
        self.head=None
        self.lenght=0

    def DestroyList(self):      #销毁这个链表
        self.head=None
        self.lenght=0

    def GetLength(self):        #获取链表的长度
        return self.lenght

    def GetElem(self,i):        #获取链表第i个元素，若i超出索引，返回none
        if i <= self.lenght:
            a=self.head
            if i==1:
                return a.getdata()
            else:
                for j in range(i-1):
                    a=a.next
                return a.getdata()
        else:
            return None

    def GetValue(self,value):   #获取值为Value的元素的索引组成的列表，不存在返回-1
        a=self.head
        j=1
        index=[]
        while j<= self.lenght:
            if value==a.getdata():
                index.append(j)
            a=a.next
            j=j+1
        if index!=[]:
            return index
        else:
            return -1

    def InsElem(self,i,node):       #将结点node插入为第i个元素
        a = self.head
        if i> 2:
            if i <= self.lenght:
                for j in range(i-2):        #查找第i-1个结点
                    a=a.next
                node.next=a.next
                a.next=node
                self.lenght=self.lenght + 1
                print('插入成功')
            else:
                print('插入失败')
        elif i==2:
            node.next=a.next
            a.next=node
            self.lenght = self.lenght + 1
            print('插入成功')
        else:
            node.next=self.head
            self.head=node
            self.lenght = self.lenght + 1
            print('插入成功')

    def DelElem(self,i):        #删除第i个元素
        a = self.head
        if i>2:
            if i <= self.lenght:
                for j in range(i-2):    #查找第i-1个结点
                    a=a.next
                a.next = a.next.next
                self.lenght=self.lenght - 1
                print('删除成功')
            else:
                print('删除失败')
        elif i==2:
            a.next=a.next.next
            self.lenght = self.lenght - 1
            print('删除成功')
        else:
            self.head = a.next
            self.lenght = self.lenght - 1
            print('删除成功')

    def DispList(self):     #遍历单链表
        if self.head != None:
            a=self.head
            print(a.getdata())
            while a.next != None:
                a=a.next
                print(a.getdata())
        else:
            print('表为空')

    def append(self,node):     #在表的最后加入结点node
        a=self.head
        if a != None:
            if a.next !=None:
                while a.next !=None:
                    a=a.next
                a.next=node
                self.lenght=self.lenght+1
            else:
                a.next=node
                self.lenght = self.lenght + 1
        else:
            self.head=node
            self.lenght = self.lenght + 1


node_1=Node(1)
node_2=Node(2)
node_3=Node(3)
list=InitLsit()
list.append(node_1)
list.append(node_2)
list.append(node_3)
list.DispList()
print('链表长度为 ',list.GetLength())
print(list.GetElem(2))
print(list.GetValue(3))
node_4=Node(4)
list.InsElem(1,node_4)
list.DispList()
list.DelElem(1)
list.DispList()
list.DestroyList()
