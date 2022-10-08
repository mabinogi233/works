a=input('请输入第一个边')
b=input('请输入第二个边')
c=input('请输入第三个边')
def sanjiaoxing(a,b,c):
    if a+b<c or a+c<b or b+c<a:
        print('不能组成三角形')
    else:
        if a==b or a==c or b==c:
            if a==b and b==c:
                print('等边三角形')
            else:
                print('等腰三角形')
        else:
            print('一般三角形')
sanjiaoxing(int(a),int(b),int(c))

def f():
    list=[]
    dayushiyi=[]
    sum=0
    for i in range(20):
        list.append(int(input('请输入数')))
    for i in range(20): #查找大于11的数
        if list[i]>11:
            dayushiyi.append(list[i])
    for i in range(len(dayushiyi)):
        sum+=dayushiyi[i]
    pingjun=sum/len(dayushiyi)
    print('平均数为',pingjun)
    print('和为',sum)

def g():
    list = []
    ten=0   #表示90-100
    seven=0 #表示70-89
    six=0       #表示60-69
    bujige=0    #表示60以下
    for i in range(20):
        list.append(int(input('请输入数')))
    for i in list:
        if    90<=i<=100:
            ten+=1
        elif  70<=i<90:
            seven+=1
        elif 60<=i<70:
            six+=1
        else:
            bujige+=1

def yunsuan():
    list=[]
    for i in range(20):
        list.append(int(input('请输入数')))

    def insertSort(a, len):  # 直接插入排序
        for i in range(1, len):
            if a[i - 1] > a[i]:
                t = a[i]
                j = i - 1
                while a[j] > t and j >= 0:
                    a[j + 1] = a[j]
                    j = j - 1
                a[j + 1] = t
        return a

    insertSort(list,20)
    print('最大值为',list[-1])
    print('最小值为',list[0])

