list=['shijiazhuang','xizhang','anhui','xinjiang','chongqing']
print('The first three item in the list are:')
for i in list[:3]:
    print(i)
print('\nThree item from the middle of the list are:')
for i in list[1:4]:
    print(i)
print('\nThe last three item in the list are:')
for i in list[-3:]:  #输出最后三个元素
    print(i)

food=['zhishi','huangyou','oingguo']
friend_food=food[:] #创建food的副本
food.append('caomei')
friend_food.append('boluo')
print('\nMy favourite pizzas are ')
for i in food:
    print(i)
print("\nMy friend's favourite pizzas are ")
for i in friend_food:
    print(i)

