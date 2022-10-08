people={
    'name':'Wei',
    'xing':'Liu',
    'age':18,
    'local':'shijiazhuang'
}
for k,v in people.items():  #以key，value的形式遍历字典，并打印相应的键和值
    print(k,v)
for k in people.keys():     #获取所以得键并打印
    print(k)
for v in people.values():   #获取所以得值并打印
    print(v)

people={
    'admin':2,
    'tom':5,
    'anna':8,
    'frog':6,
    'kim':74
}

Python={
    'print':'传入相应参数，打印相应的数据',
    'if':'如果条件为真则执行下面的代码块',
    'string':'字符串数组，一种数据类型',
    'break':'跳出循环',
    'for':'根据参数执行循环'
}
for k,v in Python.items():
    print(k+';\n'+'\t'+v)