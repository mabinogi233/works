car = input('What car you like')
print('Let me see if I can find a '+car)

people=int(input('How many people ?'))  #input输入的数据默认为string
if people >=8:
    print('sorry,no table for ',people ,' people')
else:
    print('order success')

num=int(input('please write a number'))
if num<10:
    print('Is not a 10 的倍数')
elif num%0==0:
    print('这个数是10的倍数')
else:
    print('Is not a 10 的倍数')
