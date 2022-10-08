N=int(input())
listx=[]
for i in range(N):
    j=list(input())
    listx.append(j)
listy=[]
for i in range(N):
    j=list(input())
    listy.append(j)
def eql(listx,listy):
    for i in range(N):
        for j in range(N):
            if listx[i][j]!=listy[i][j]:
                return False
    return True

def xuanzhuan_90(listx):
    a=0
    b=0
    listz=[[0 for i in range(len(listx))]for j in range(len(listx))]
    for i in range(len(listx)-1,-1,-1):
        for j in range(len(listx)):
            listz[j][i]=listx[a][b]
            b+=1
        a+=1
        b=0
    return listz

def jingxiang(listx):
    listz=[]
    for i in listx:
        j=i[::-1]
        listz.append(j)
    return listz

jieguo=[]
listx=xuanzhuan_90(listx)
if eql(listx,listy):
    jieguo.append(1)
listx=xuanzhuan_90(listx)
if eql(listx, listy):
    jieguo.append(2)
listx=xuanzhuan_90(listx)
if eql(listx, listy):
    jieguo.append(3)
listx = xuanzhuan_90(listx)
listx=jingxiang(listx)
if eql(listx, listy):
    jieguo.append(4)
listx=xuanzhuan_90(listx)
if eql(listx, listy):
    jieguo.append(5)
listx=xuanzhuan_90(listx)
if eql(listx, listy):
    jieguo.append(5)
listx=xuanzhuan_90(listx)
if eql(listx, listy):
    jieguo.append(5)
listx=xuanzhuan_90(listx)
listx=jingxiang(listx)
if eql(listx, listy):
    jieguo.append(6)
if jieguo!=[]:
    print(min(jieguo))
else:
    print(7)

'''flag=0
for a in range(1,4):
    listx=xuanzhuan_90(listx)
    if eql(listx,listy):
        flag=a
        break
if flag!=0:
    print(flag)
else:
    listx=xuanzhuan_90(listx)
    listx=jingxiang(listx)
    if eql(listx,listy):
        flag=4
    else:
        for i in range(1,4):
            listx=xuanzhuan_90(listx)
            if eql(listx,listy):
                flag=5
                break
    if flag!=0:
        print(flag)
    else:
        listx=xuanzhuan_90(listx)
        listx=jingxiang(listx)
        if eql(listx,listy):
            print(6)
        else:
            print(7)'''

