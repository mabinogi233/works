class SunXvStack():
    def __init__(self,max=8): #创建栈
        self.max=max
        self.data=[None]*self.max
        self.top=-1

    def DesTroyStack(self): #摧毁栈
        self.data = [None] * self.max
        self.data = -1

    def push(self,value):   #元素value进展
        if self.top<self.max-1:
            self.data[self.top+1]=value
            self.top+=1
            print('进栈成功')
        else:
            print('栈满')

    def pop(self):      #元素出栈
        if self.top!=-1:
            self.data[self.top]=None
            self.top+=-1
            print('出栈成功')
        else:
            print('栈空')

    def GetTop(self):   #获取栈头元素，为空返回None
        if self.top!=-1:
            return self.data[self.top]
        else:
            return None

    def StackEmpty(self):   #判断栈是否为空，为空返回True，不为空返回False
        if self.top!=-1:
            return False
        else:
            return True

zhan=SunXvStack()
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

