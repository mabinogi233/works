class ShunQueue():
    def __init__(self,max = 8): #生成一个顺序队列（逻辑环）
        self.max = max
        self.data = [None] * self.max
        self.head = -1
        self.tail = -1

    def DestroyQueue(self): #销毁这个队列
        self.data = [None] * self.max
        self.head = -1
        self.tail = -1

    def EnQueue(self, value):   #元素进队
        if self.tail == -1:
            self.tail += 1
            self.data[self.tail] = value
            self.head = 0
            print('进队成功')
        elif (self.head == 0 and self.tail == self.max - 1) or (self.tail + 1 == self.head):
            print('进队失败，队列已满')
        else:
            if self.tail != self.max - 1:
                self.tail += 1
                self.data[self.tail] = value
                print('进队成功')
            else:
                self.tail = 0
                self.data[self.tail] = value
                print('进队成功')

    def DelQueue(self): #元素出队
        if self.head == -1:
            print('出队失败，队列为空')
        elif self.head == self.tail:
            self.data[self.head] = None
            self.head = -1
            self.tail = -1
            print('出队成功')
        else:
            if self.head == self.max - 1:
                self.data[self.head] = None
                self.head = 0
                print('出队成功')
            else:
                self.data[self.head] = None
                self.head += 1
                print('出队成功')

    def GetHead(self):  #获取队头元素
        return self.data[self.head]

    def QueueEmpty(self):   #判断队列是否为空，为空返回Treu，不为空返回False
        if self.head == -1:
            return True
        else:
            return False

liandui=ShunQueue()
liandui.EnQueue(12)
liandui.EnQueue('字符串')
liandui.EnQueue(234)
print(liandui.GetHead())
liandui.DelQueue()
print(liandui.GetHead())
liandui.DelQueue()
print(liandui.GetHead())
liandui.DelQueue()


liandui.DestroyQueue()