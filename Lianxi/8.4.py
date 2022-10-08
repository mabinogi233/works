moshushi=['Amin','sodg','tom','anna']
def show(list):
    for i in list:
        print(i)
show(moshushi)

def make_great(list):
    for i in range(len(list)):
        list[i]='The great '+list[i]
    return list
#show(make_great(moshushi))

a=make_great(moshushi[:])#传入moshushi列表的副本，函数不会修改moshushi列表
show(a)
show(moshushi)