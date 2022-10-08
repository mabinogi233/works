car='subaru'
if car=='subaru':
    print('True')
    print('car= subaru')
elif car =='audi':
    print('True')
    print('car=audi')

str_1='listen'
str_2='Listen'
if str_1==str_2:
    print('True')
else:
    print('False')
if str_2.lower()==str_1:
    print('True')
else:
    print('False')

#比较数字的大小
def compare(a,b):
    if a==b:
        print(a,'=',b)
    elif a>b:
        print(a,'>',b)
    elif a<b:
        print(a,'<',b)


i=1
j=2
print(j==2 and i==2)
print(i==2 or j ==2)

list=[A for A in range(0,10)]
print(2 in list)
print(10 in list)


