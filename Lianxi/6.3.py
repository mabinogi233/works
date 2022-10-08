Python = {
    'print': '传入相应参数，打印相应的数据',
    'if': '如果条件为真则执行下面的代码块',
    'string': '字符串数组，一种数据类型',
    'break': '跳出循环',
    'for': '根据参数执行循环'
}
for k,v in Python.items():
    print(k+';\n'+'\t'+v)

Python['int']='整形数据'
Python['float']='浮点型数据'
Python['and']='做"和"运算，并返回布尔类型的数据'
Python['or']='做"或"运算，并返回布尔类型的数据'
Python['！=']='不等于'
for k,v in Python.items():
    print(k+';\n'+'\t'+v)

river={
    'Chuangjiang':'zhongguo',
    'niluohe':'yindu',
    'mixixibihe':'meiguo'
}
for k in river.keys():
    print(k)
for v in river.values():
    print(v)

favourite_lauguages={
    'jen':'Python',
    'sarah':'C',
    'edward':'Python',
    'phil':'Ruby'
}
purper={
    'phil':'Ruby',
    'tim':'Python',
    'anna':'Java'
}
for k in purper.keys():
    if k in favourite_lauguages.keys():
        print('Thanks for your help,'+k)
    else:
        print('plsase join it,'+k)