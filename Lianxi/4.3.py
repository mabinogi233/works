for i in range(1,21):
    print(i)
list=[i for i in range(1,1000001)]

for i in range(len(list)):
    print(list[i])

print(min(list))
print(max(list))
print(sum(list))

#for i in range(1,21,2):#(初始的i，终止的i+1，步长)
list1=[i for i in range(1,21,2)]
for list2 in list1:
    print(list2)

list3=[i for i in range(3,31,3)]
for list2 in list3:
    print(list2)

list4=[]
for i in range(1,11):
    list4.append(i**3)
for i in range(len(list4)):
    print(list4[i])

list5=[i**3 for i in range(1,11)]
for i in list5:
    print(i)

