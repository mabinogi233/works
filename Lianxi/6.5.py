people_1={
    'name':'Wei',
    'xing':'Liu',
    'age':18,
    'local':'shijiazhuang'
}
people_2={
    'name':'chaoran',
    'xing':'Wang',
    'age':21,
    'local':'shijiazhuang'
}
people_3={
    'name':'Cao',
    'xing':'Cao',
    'age':35,
    'local':'chengde'
}
people=[people_1,people_2,people_3]
for peo in people:
    print(peo)

pet_1={
    'name':'timmi',
    'age':5,
    'master':'Wangchaoran'
}
pet_2={
    'name':'tom',
    'age':3,
    'master':'Wanggou'
}
pet_3={
    'name':'White',
    'age':6,
    'master':'Lisi'
}
pet=[pet_1,pet_2,pet_3]
for i in pet:
    print(i)

favourite_palces={}
favourite_palces['Liming']=['hebei','chengdu']
favourite_palces['Xiaoli']=['henan','hainan','chongqing']
favourite_palces['Ming']=['bulage']
for k,v in favourite_palces.items():
    print(k+' ',v)

people21={
    'admin':[2,75,68],
    'tom':[5,54],
    'anna':[8],
    'frog':[6,4],
    'kim':[74,65,48,20]
}
for k,v in people21.items():
    print(k)
    for i in range(len(v)):
        print(v[i])

cities={}
cities['hebei']={
    'belong':'China',
    'renhou':'4000万',
    'miaoshu':'雾霾严重'
}
cities['chongqing']={
    'belong':'China',
    'renhou':'800万',
    'miaoshu':'山城'
}
cities['London']={
    'belong':'UK',
    'renhou':'1000万',
    'miaoshu':'曾经的雾都'
}
for k,v in cities.items():
    print(k,' : ')
    for i,j in v.items():
        print('\t',i,':',j)