# 元组中储存的值不可修改，但可以修改储存元组的变量的值,操作大致同列表
#例如 lie=(200,200)
#可以lie=(400,200)这样‘修改’
food=('apple','banana','bear','pinapple','peach')
for i in food:
    print(i)


def xiugaiyuanzu(i,j,yuanzu): #将元组yuanzu中索引为i的元素修改为j
    list=[]                     #创建一个列表，储存元组中的数据,也可用list()把元组转化为列表
    for a in range(len(yuanzu)):
        list.append(yuanzu[a])
    del list[i]
    list.insert(i,j)
    new_yuanzu=tuple(list)      #将列表转化为元组
    return new_yuanzu

jieguo=xiugaiyuanzu(1,'melon',food)
print(jieguo)

