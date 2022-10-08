def erxiangshixishu(n):
    if n==0:
        list=[1]
        return list
    else:
        list=[]
        list.append(1)
        comb_old=1
        for k in range(1,n):
            comb=jisuanjiecheng(n)//(jisuanjiecheng(k)*jisuanjiecheng(n-k))
            if comb_old>=comb:
                break
            comb_old=comb
            list.append(comb)
        if n % 2!=0:
            for i in range(len(list)-1,-1,-1):
                list.append(list[i])
        else:
            for i in range(len(list)-2,-1,-1):
                list.append(list[i])
        return list

def jisuanjiecheng(n):
    jiecheng=1
    for i in range(1,n+1):
        jiecheng=jiecheng*i
    return jiecheng

#N=int(input())
for i in range(N):
    list=erxiangshixishu(i)
    for j in range(len(list)):
        if j!=len(list)-1:
            print(list[j],end=' ')
        else:
            print(list[j],end='\n')