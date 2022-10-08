#删除二维列表的一列
list=[[0 for i in range(4)]for j in range(5)]#生成一个 4行 5列的空二维列表(列表解析)
for i in range(len(list)):
    for j in range(len(list[i])):
        list[i][j]=i+j
print(list)
def shanchuyilie(a,list): #删除list 第a列的数据
    for i in range(len(list)):
        del list[i][a-1]
    return list

shanchu=shanchuyilie(2,list)
print(shanchu)

