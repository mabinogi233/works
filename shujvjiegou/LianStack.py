class LianStack():
    def __init__(self):     #生成一个链栈
        self.top = None
        self.head = None
        self.lenght=0

    class Nodezhan():
        def __init__(self, value):
            self.data = value
            self.next = None

    def DestroyStack(self): #摧毁栈
        self.head = None
        self.top = None
        self.lenght=0

    def push(self, value):  #元素进栈
        class Nodezhan():
            def __init__(self, value):
                self.data = value
                self.next = None
        node = Nodezhan(value)
        a = self.head
        if a != None:
            if a.next != None:
                while a.next != None:
                    a = a.next
                a.next = node
                self.lenght = self.lenght + 1
                self.top=node
            else:
                a.next = node
                self.top = node
                self.lenght = self.lenght + 1
        else:
            self.head = node
            self.top = node
            self.lenght = self.lenght + 1
        print('进栈成功')

    def pop(self):      #弹出栈头元素
        if self.top != None:
            if self.lenght>1:
                a = self.head
                for u in range(self.lenght - 2):  # 查找第lenght-1个结点
                    a = a.next
                a.next=None
                self.top=a
                self.lenght+=-1
            else:
                self.DestroyStack()
        else:
            print('栈为空')

    def GetTop(self):
        return self.top.data

    def StackEmpty(self):   #栈为空返回True，不为空返回False
        if self.top != None:
            return False
        else:
            return True

zhan=LianStack()
print(zhan.StackEmpty())
zhan.push(1)
zhan.push(2)
zhan.push(3)
print(zhan.StackEmpty())
print(zhan.GetTop())
zhan.pop()
print(zhan.GetTop())
zhan.pop()
print(zhan.GetTop())
zhan.pop()
print(zhan.StackEmpty())