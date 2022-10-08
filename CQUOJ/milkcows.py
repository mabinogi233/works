N=int(input())
listy=[]
maxa=0
maxende=0
minstarted=1000000000
for i in range(N):
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    if b-a>maxa:
        maxa=b-a
    if minstarted>a:
        minstarted=a
    if b>maxende:
        maxende=b
    listy.append([a,b])
mina=0
listy=sorted(listy,key=(lambda x:x[0]))
start=listy[0][0]
end=listy[0][1]
for hang in listy:
    if hang[0]>end:
        maxa = max(end - start, maxa)
        mina=max(mina,hang[0]-end)
        start=hang[0]
    end=max(end,hang[1])
print(maxa,mina)
