#按孩子兄弟链储存
class TreeNode():
    def __init__(self,data):#构造树的结点
        self.data=data
        self.child=None
        self.brother=[]

    def setchild(self,Treenode):    #将孩子节点设置为Treenode
        self.child= Treenode

    def addbrother(self,Treenode):  #将兄弟节点Treenode加入结点
        self.brother.append(Treenode)

class BTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BTree():
    def __init__(self):
        self.root=None

class Tree():
    def __init__(self):
        self.root=None

    def setroot(self,root):#将值root节点设置为树的根节点
        self.root=root

    def ReturnToBTtee(self):    #将树变为二叉树
        btree=BTree()
        btree.root=BTreeNode(self.root.data)#将二叉树根节点得值设置为树的根节点对应的值
        def zhuanhua(root,node):    #将node和其对应的兄弟节点转化为root的二叉树(root是二叉树节点,node是普通树节点)
            root.left=BTreeNode(node.data)      #将BT(node)设置为root的左儿子
            if node.brother!=[] :    #node有兄弟
                linshi=root.left
                for i in range(len(node.brother)):    #不断将node的兄弟作为前一个兄弟的右儿子加入二叉树
                    linshi.right=BTreeNode(node.brother[i].data)
                    linshi=linshi.right
                #准备递归
                linshi = root.left
                if node.child!=None:
                    zhuanhua(linshi,node.child)
                for i in range(len(node.brother)):
                    linshi=linshi.right
                    if node.brother[i].child!=None:
                        zhuanhua(linshi,node.brother[i].child)
        zhuanhua(btree.root,self.root.child)
        return btree

node_1=TreeNode('A')
node_2=TreeNode('B')
node_3=TreeNode('C')
node_4=TreeNode('D')
node_5=TreeNode('E')
node_6=TreeNode('F')
node_7=TreeNode('G')
node_1.setchild(node_2)
node_2.addbrother(node_3)
node_2.addbrother(node_4)
node_3.setchild(node_5)
node_5.addbrother(node_6)
node_4.setchild(node_7)
tree=Tree()
tree.setroot(node_1)
btree=tree.ReturnToBTtee()


