class lianQueue():
    def __init__(self):      #创建一个链队（循环单链表）
        self.head=None
        self.tail=None

    def DestroyQueue(self):     #摧毁这个链队
        self.head=None
        self.tail=None

    def EnQueue(self,value):        #元素进队
        class Node():               #创建一个节点
            def __init__(self, data):
                self.data = data
                self.next = None
        node=Node(value)
        if self.head != None:       #链队不为空
            a=self.tail
            a.next=node
            node.next=self.head
            self.tail=node
            print('进队成功')
        else:                       #链队为空
            self.head=node
            self.tail=node
            node.next=node
            print('进队成功')

    def DeQueue(self):      #元素出队
        if self.head != None:
            if self.head!=self.tail:
                a=self.head
                self.tail.next=a.next
                self.head=a.next
                print('出队成功')
            else:        #元素只有一个
                self.head=None
                self.tail=None
                print('出队成功')

        else:            #队列为空
                print('队列为空')

    def GetHead(self):  #获取头元素
        if self.head != None:
            return self.head.data
        else:
            return None

    def QueueEmpty(self):#判断队列是否为空，为空返回0，不为空返回1
        if self.head!=None:
            return 1
        else:
            return 0

liandui=lianQueue()
liandui.EnQueue(12)
liandui.EnQueue('字符串')
liandui.EnQueue(234)
print(liandui.GetHead())
liandui.DeQueue()
liandui.EnQueue(122)
print(liandui.QueueEmpty())

print(liandui.GetHead())
liandui.DeQueue()
print(liandui.GetHead())
liandui.DeQueue()
print(liandui.GetHead())
liandui.DeQueue()


liandui.DestroyQueue()