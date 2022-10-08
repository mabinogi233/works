list=['Father','Mother','Grandma','Grandpa']
for i in range(len(list)):
    print('I invite '+list[i]+' to a party')

print("Grandpa can't go to party")
list.remove('Grandpa')
list.append('Brother')
for i in range(len(list)):
    print(list[i]+'is coming to party')

print('l find a big table')
#向指定位置添加指定元素
list.insert(0,'sister')
list.insert(2,'son')
list.append('daughter')
for i in range(len(list)):
    print('I invite '+list[i]+" to party")

print('sorry,I can only invite two people')
while True:
    a=list.pop()
    print('Sorry '+a)
    if len(list)==2:
        break
for i in range(2):
    print('You are also in the list '+list[i])
del list[0]
del list[0]
print(list)
