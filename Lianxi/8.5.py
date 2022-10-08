def sandwich(*shicai): #     * shicai 表示可以传递任意数量的shicai (接受任意数量的实参)
    print('The sandwich have',shicai)
sandwich('apple')
sandwich('banana','apple')
sandwich('apple','greap','babab')

def yonghu(ming,xing,**jieshao): #  **jieshao 表示创建一个名为jieshao的字典，可以传入任意数量的内容进入jieshao这个字典
    list={}                      #  以变量名为key ，变量值为value储存 (任意数量的关键字实参)
    list['名']=ming
    list['姓']=xing
    for k,v in jieshao.items():
        list[k]=v
    return list
a=yonghu('wenze','liu',local='shijiazhuang',xingbie='男',age=18) #红色字表示关键字
print(a)

def car(zhizaoshang,xinghao,**canshu):
    zidian={}
    zidian['制造商']=zhizaoshang
    zidian['型号']=xinghao
    for k,v in canshu.items():
        zidian[k]=v
    return zidian
b=car(xinghao='KCW201',zhizaoshang='baoma',chedeng=True,color='green')#红色是使用关键字实参,可以改变关键字的位置
c=car('fengtian','WFAWFG54',color='blue')   #使用位置实参,不能改变关键字位置
print(b)
print(c)
