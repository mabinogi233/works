import sys
sys.setrecursionlimit(1000000)  #设置递归深度
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

    def pop(self):      #元素出栈
        if self.top!=-1:
            self.data[self.top]=None
            self.top+=-1

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
        else:                       #链队为空
            self.head=node
            self.tail=node
            node.next=node

    def DeQueue(self):      #元素出队
        if self.head != None:
            if self.head!=self.tail:
                a=self.head
                self.tail.next=a.next
                self.head=a.next
            else:        #元素只有一个
                self.head=None
                self.tail=None

    def GetHead(self):  #获取头元素
        if self.head!=None:
            return self.head.data
        else:
            return None

    def QueueEmpty(self):#判断队列是否为空，为空返回0，不为空返回1
        if self.head!=None:
            return 1
        else:
            return 0

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.ltag=None
        self.rtag=None

class BTree():
    def __init__(self):
        self.root=None

    def CreateBTree(self,list_2):   #根据二叉树的括号表示法建立二叉树
        if len(list_2)>0:
            Stack=SunXvStack()       #建立一个栈      #树的根节点为string中的第一个元素
            k=0
            list_1=[]
            for j in range(len(list_2)):
                list_1.append(Node(list_2[j]))
            for i in range(1,len(list_1)):    #遍历整个list
                if list_1[i].data=='(':                #如果为（，则他前一个元素进栈，并且使k=1，
                    b=list_1[i-1]
                    Stack.push(b)     #表示后面第一个元素是前一个的左儿子
                    k=1
                    if self.root==None: #树的根节点为string中的第一个元素
                        self.root=b
                elif list_1[i].data==')':          #如果为），表示栈头元素左右儿子处理完毕，出栈
                    Stack.pop()
                elif list_1[i].data==',':      #如果为，则他下一个元素为右儿子，k=2
                    k=2
                else:   #其他情况
                    if k==1:    #如果k=1，则其为左文字
                        a=Stack.GetTop()
                        a.left=list_1[i]
                    else:       #如果k=2，则其为右儿子
                        a=Stack.GetTop()
                        a.right=list_1[i]
        else:
            print('string为空')

    def DestroyBTree(self):#摧毁二叉树
        self.root=None

    def BTHeight(self): #返回二叉树的高度
        a = self.root
        def getheight(node): #递归计算高度
            if node==None :    #为空返回None
                return 0
            else:           #不为空返回左子树和右子树的高度+1
                le=node.left
                ri=node.right
                return max(getheight(le),getheight(ri))+1
        height=getheight(a)
        return height

    def LeafCount(self):    #返回二叉树叶子结点的个数
        a = self.root
        def getcount(node):     #递归计算个数
            if node==None:         #为空返回0
                return 0
            elif node.right==None and node.right==None: #为叶子节点返回1
                return 1
            else:       #返回左子树和右子树叶子节点的个数
                le=node.left
                ri=node.right
                return getcount(le)+getcount(ri)
        sum=getcount(a)
        return sum

    def NodeCount(self):    #返回二叉树节点的个数
        a = self.root

        def getcount(node):  # 递归计算个数
            if node == None:  # 为空返回0
                return 0
            else:  # 返回左子树和右子树节点和自身节点的个数
                le = node.left
                ri = node.right
                return getcount(le) + getcount(ri) + 1
        sum = getcount(a)
        return sum

    def DispBTree(self):    #括号法输出二叉树
        a=self.root
        def bianli(node):
            if node!=None:
                print(node.data)
                if node.left!=None or node.right!=None: #有子树时输出
                    print('(',end='')
                    bianli(node.left)           #递归处理左子树
                    if node.right!=None:        #右子树输出，
                        print(',',end='')
                    bianli(node.right)          #递归处理右子树
                    print(' )')           #右子树输出后输出 ）
        bianli(a)

    def PreOrder(self): #先序遍历
        a=self.root
        def bianli(node):
            if node!=None:
                print(node.data)
                bianli(node.left)
                bianli(node.right)
        bianli(a)

    def InOrder(self):  #中序遍历
        a = self.root
        def bianli(node):
            if node != None:
                bianli(node.left)
                print(node.data)
                bianli(node.right)
        bianli(a)

    def PostOrder(self):    #后序遍历
        a = self.root
        def bianli(node):
            if node != None:
                bianli(node.left)
                bianli(node.right)
                print(node.data)
        bianli(a)

    def LevelOrder(self):#层次遍历
        queue =lianQueue()
        l = []
        queue.EnQueue(self.root)
        while queue.GetHead()!=None:
            current = queue.GetHead()
            queue.DeQueue()
            l.append(current.data)
            if current.left!=None:
                queue.EnQueue(current.left)
            if current.right!=None:
                queue.EnQueue(current.right)
        for i in l:
            print(i)

    def CreatThread(self,model):  #按model线索化，1为先序，2为中序，3为后序     本质上是把二叉树变为一个双链表
        class HeadNode():
            def __init__(self):
                self.left = None
                self.right = None
                self.ltag = None
                self.rtag = None
        head=HeadNode() #创建头结点
        head.ltag=0
        head.rtag=1
        head.right=self.root

        def InThread(p,pre):    #中序建立线索
            if p!=None:
                pre=InThread(p.left,pre)
                if p.left==None:
                    p.left=pre
                    p.ltag=1
                else:
                    p.ltag=0
                if pre.right==None:
                    pre.right=p
                    pre.rtag=1
                else:
                    pre.rtag=0
                pre=p
                pre=InThread(p.right,pre)
            return pre
        def PreThread(p,pre):    #先序建立线索
            if p!=None:
                if p.left==None:
                    p.left=pre
                    p.ltag=1
                else:
                    p.ltag=0
                if  pre.right==None:
                    pre.right=p
                    pre.rtag=1
                else:
                    pre.rtag=0
                pre=p
                if p.ltag!=1:
                    pre=PreThread(p.left,pre)
                if p.rtag!=1:
                    pre=PreThread(p.right,pre)
            return pre

        def PostThread(p,pre):  #后序遍历
             if p != None:
                 if p.ltag != 1:
                     pre = PostThread(p.left, pre)
                 if p.rtag != 1:
                     pre = PostThread(p.right, pre)
                 if p.left == None:
                     p.left = pre
                     p.ltag = 1
                 else:
                     p.ltag = 0
                 if pre.right == None :
                     pre.right = p
                     pre.rtag = 1
                 else:
                     pre.rtag = 0
                 pre = p
             return pre

        if self.root==None: #树为空
            head.ltag=0
            head.left=head
            head.rtag=1
            head.right=None
        else:    #树不为空
            if model==1:
                head.left = self.root
                pre = head
                pre=PreThread(self.root,pre)    #先序遍历线索化二叉树
            elif model==2:
                head.left = self.root
                pre = head
                pre=InThread(self.root,pre)   #中序遍历线索化二叉树
            else:
                head.left = self.root
                pre = head
                pre=PostThread(self.root,pre)   #后序遍历线索化二叉树
            pre.right=head
            pre.rtag=1
            head.right=pre
            self.head=head

    '''def FindNode(self,value):#查找对应值得结点
        a = self.root
        def bianli(node):
            if node != None:
                bianli(node.left)

                if node.data==value:
                     return node

                bianli(node.right)
        bianli(a)'''


    '''def FindParent(self,p):#获取结点p的父节点
        a = self.root
        jieguo=None
        def bianli(node):
            if node != None:
                bianli(node.left)
                if node.left or node.right==p:
                    jieguo= node
                bianli(node.right)
        bianli(a)
        return jieguo'''

    def FirstNode(self,model):  #查找当前遍历的第一个节点，model为模式
        if model == 1:  # 先序
            return self.root
        if model == 2:  # 中序
            p=self.root
            while p.ltag==0:
                p=p.left
            return p
        ''' if model == 3:  # 后序
            p = self.root
            while p.ltag == 0:
                p = p.left
            return p'''

    def LastNode(self,model):   #查找当前遍历的最后一个节点，model为模式
        if model == 1:  # 先序
            return self.head.right
        if model == 2:  # 中序
            return self.head.right
        #if model == 3:  # 后序
          #  return self.head.right

    def PreNode(self,p,model):#查找在当前遍历情况下p节点的前驱节点,model为模式
        #if model == 1:  # 先序   先序遍历查找前驱结点比较困难

        if model == 2:  # 中序
            if p.ltag==1:
                return p.left
            else:
                q=p.left
                while q.rtag==0:
                    q=q.right
                return q
        '''if model == 3:  # 后序
            if p.ltag==1:
                return  p.left
            elif p.right!=None:
                return p.right
            else:
                return p.left'''



    def PostNode(self,p,model):#查找在当前遍历情况下p节点的后继节点，model为模式
        if model == 1:  # 先序
            if p==None:
                return None
            elif p.rtag==1:
                return p.right
            elif p.left!=None:
                return p.left
            else:
                return p.right
        if model == 2:  # 中序
            post=p.right
            if p.rtag!=1:
                while post.ltag==0:
                    post=post.left
            return post
        #if model == 3:  # 后序  后序查找后继节点比较困难


    def DispTree(self,model):  # 遍历二叉树  1为先序，2为中序，3为后序 。必须与CreateThread要对应
        if model==1:    #先序
            p=self.FirstNode(1)
            while p!=self.head:
                print(p.data)
                p=self.PostNode(p,1)
        if model==2:      #中序
            p = self.FirstNode(2)
            while p != self.head:
                print(p.data)
                p = self.PostNode(p, 2)
        #if model==3:    #后序


    def ThDispTree(self,model): #逆序遍历二叉树 model为模式
       # if model == 1:   #先序

        if model == 2:   #中序
            p=self.LastNode(2)
            while p !=self.head:
                print(p.data)
                p=self.PreNode(p,2)
       # if model == 3:   #后序

tree=BTree()
tree.CreateBTree(['A','(','B',',','C','(','D',',','E',')',')'])
#后序线索化未完成

