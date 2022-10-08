def city_country(city,country):
    return city+','+country
a=city_country('shijiazhuang','zhongguo')
b=city_country('beijing','zhongguo')
c=city_country('Santiago','Chile')
print(a)
print(b)
print(c)

def make_album(name,zhuanjiming,len=0):
    zhuanji={}
    zhuanji[name]=zhuanjiming
    if len !=0:
        zhuanji['shumu']=len
    return zhuanji
d=make_album('wangchaoran','zhexue')
e=make_album('geng','Laber',10)
print(d)
print(e)

while True:
    i=input('请输入歌手名字')
    j=input('请输入专辑名字')
    m=make_album(i,j)
    print(m)
    quit=input('退出请输入quit，继续请输入con')
    if quit=='quit':
        break


