#均分纸牌（最后一堆纸牌只能往第一堆移动）
import tensorflow
import scipy
#计算有几个零子串
def jisuanlingshuangeshu(liebiao):
    linggeshu=0
    j=0
    geshu=len(liebiao)
    while j<geshu:
        if liebiao[j]==0:
            end=j
            for i in range(j+1,len(liebiao)):
                if liebiao[i]==0:
                    end+=1
                    continue
                break
            linggeshu+=1
            j=end
        j+=1
    print(linggeshu)
    return linggeshu

#去掉全部零元
def qudaolingchuan(liebiao):
    i=0
    while i<len(liebiao):
        if liebiao[i]==0:
            del liebiao[i]
            i-=1
        i+=1

#贪心算法计算移动次数
def jisuan(liebiao):
    w = 0
    if liebiao[-1] == 0:
        for i in range(len(liebiao) - 2):
            liebiao[i + 1] += liebiao[i]
            if liebiao[i] == 0:
                w += 1
            liebiao[i] = 0
        return len(liebiao) - 2 - w
    else:
        if liebiao[-1] < 0:
            for i in range(len(liebiao) - 1):
                liebiao[i + 1] += liebiao[i]
                if liebiao[i] == 0:
                    w += 1
                liebiao[i] = 0
            return len(liebiao) - w - 1
        else:
            liebiao[0] += liebiao[-1]
            liebiao[-1] = 0
            for i in range(len(liebiao) - 2):
                liebiao[i + 1] += liebiao[i]
                if liebiao[i] == 0:
                    w += 1
                liebiao[i] = 0
            return len(liebiao) - w - 1

#判断能不能把两个零子串中间的元素全部移动为0，返回移动次数
def panduan(liebiao,linggeshu):
    i=0
    yidongcishu=0
    linggeshux= 0
    while i<len(liebiao)and linggeshux<=linggeshu:
        if liebiao[i]==0:
            start=-1
            end=len(liebiao)
            linggeshux+=1
            for j in range(i,len(liebiao)):
                if liebiao[j]!=0:
                    start=j
                    break
            for j in range(start,len(liebiao)):
                i=len(liebiao)
                if liebiao[j]==0:
                    end=j
                    i=j-1
                    break
            if start!=-1 and end!=len(liebiao):
                x=0
                listx=liebiao[start:end]
                for j in range(len(listx)-1):
                    listx[j+1]+=listx[j]
                    if listx[j]==0:
                        x+=1
                    listx[j]=0
                if listx[-1]==0:
                    for m in range(start,end):
                        liebiao[m]=0
                    yidongcishu+=len(listx)-1-x
        i+=1
    return yidongcishu

#主函数
def main(liebiao):
    jieguo=-1
    X=jisuanlingshuangeshu(liebiao)
    if X==0:
        jieguo=jisuan(liebiao)
    elif X==1:
        boor,P=qubuqu(liebiao)
        if boor==True:
            qudaolingchuan(liebiao)
            jieguo = max(jisuan(liebiao),P)
        else:
            jieguo=jisuan(liebiao)
    else:
        linshiyidongcishu=panduan(liebiao,X)
        if linshiyidongcishu==0:
            jieguo=jisuan(liebiao)
        else:
            Y=jisuanlingshuangeshu(liebiao)
            if Y==1:
                boor_1,P=qubuqu(liebiao)
                if boor_1==True:
                    qudaolingchuan(liebiao)
                    jieguo = max(jisuan(liebiao),P) + linshiyidongcishu
                else:
                    jieguo=jisuan(liebiao)+linshiyidongcishu
            else:
                yido=1
                while yido!=0:
                    a=jisuanlingshuangeshu(liebiao)
                    yido=panduan(liebiao,a)
                    linshiyidongcishu+=yido
                    print(linshiyidongcishu)
                Y = jisuanlingshuangeshu(liebiao)
                if Y == 1:
                    boor_2,P=qubuqu(liebiao)
                    if boor_2==True :
                        qudaolingchuan(liebiao)
                        jieguo = max(jisuan(liebiao), P) + linshiyidongcishu
                    else:
                        jieguo = jisuan(liebiao) + linshiyidongcishu
                else:
                    jieguo=jisuan(liebiao)+linshiyidongcishu

    print(jieguo)

#判断去不去零
def qubuqu(liebiao):
    x=None
    print(liebiao)
    for i in range(len(liebiao)):
        if liebiao[i]==0:
            start=i
            end=len(liebiao)
            for j in range(start,len(liebiao)):
                if liebiao[j]!=0:
                    end=j
                    break
            x=(start,end)
            break
    if x[1]!=len(liebiao):
        A=sum(liebiao[:x[0]])
        B=sum(liebiao[x[1]:])
        print(liebiao[x[1]:])
        print(liebiao[:x[0]])
        if B<0:
            return False
        elif B>0:
            Y = min(x[1] - x[0]+1,len(liebiao[:x[0]])+len(liebiao[x[1]:])-1)
            print('Y',Y)
            return True,Y
        else:
            if liebiao[-1]>0:
                Y=len(liebiao[:x[0]])+len(liebiao[x[1]:])-1
                return True,Y
            Y = min(x[1] - x[0]+1,len(liebiao[:x[0]])+len(liebiao[x[1]:]))
            print('Y',Y)
            return True,Y



while True:

    liebiao=[]

    geshu=int(input('输入有几堆纸牌'))
    for i in range(geshu):
        liebiao.append(int(input()))

    avg=sum(liebiao)//geshu
    for i in range(geshu):
        liebiao[i]=liebiao[i]-avg

    main(liebiao)
