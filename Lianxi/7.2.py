pizza = []
while True:
    piz=input('Please order a pizza,or if you want to quit ,please writr quit')
    if piz =='quit':
        break
    else:
        pizza.append(piz)
        print('We add it in list')

while True:
    age=int(input('Please write your age'))
    if age<=3:
        print('free')
    elif age>3 and age<=12:
        print('10$')
    else :
        print('15$')


