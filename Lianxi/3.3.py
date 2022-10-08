
list=['shijiazhuang','xizhang','anhui','xinjiang','chongqing']
print(list)
new_list=sorted(list)   #创建list的一个副本，对副本new_list正向排序，不会改变list的排序，并返回这个副本
print(new_list)
print(list)
new_list2=sorted(list,reverse=True) ##创建list的一个副本，对副本new_list逆向排序，不会改变list的排序，并返回这个副本
print(new_list2)
print(list)
list.reverse() #反转列表排列顺序，无返回值
print(list)
list.reverse()
print(list)
list.sort() #正向排序list，无返回值
print(list)
list.sort(reverse=True)#逆向排序list，无返回值
print(list)
print(len(list))

