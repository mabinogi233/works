sandwich_orders=['苹果','芒果','香蕉']
finish=[]
for san in sandwich_orders:
    print(san)

while sandwich_orders:  #列表为空则为False，列表不为空为True
    sand=sandwich_orders.pop()
    print('I made ',sand,' sandwich')
    finish.append(sand)

sandwich_orders=['苹果','pastrami','芒果','pastrami','香蕉','pastrami','pastrami']
print('pastrami 买完了')
while 'pastrami' in sandwich_orders:   #pastrami在列表中，返回True
    sandwich_orders.remove('pastrami')
for san in sandwich_orders:
    print(san)

place={}
while True :
    name=input('请输入姓名')
    list = []
    while True:
        pla=input('请输入你想去的地方,退出请输入quit')
        if pla == 'quit':
            break
        list.append(pla)
    place[name]=list
    buer=input('是否新建调查人？')
    if buer=='否':
        break
print(place)