import time

def feidigui():#用二维列表储存三角数塔
    sanjiao=[
        [9],
        [12,15],
        [10,6,8],
        [2,18,9,5],
        [19,7,10,4,16]]

    #创建动态规划表
    dongtaiguihuabiao=[[-1*float('INF') for i in range(len(sanjiao))] for j in range(len(sanjiao))]
    for i in range(len(sanjiao)):
        dongtaiguihuabiao[-1][i]=sanjiao[-1][i]


    #动态规划
    for i in range(len(sanjiao)-2,-1,-1):
        for j in range(i+1):
            dongtaiguihuabiao[i][j]=max(dongtaiguihuabiao[i+1][j],dongtaiguihuabiao[i+1][j+1])+sanjiao[i][j]

    #回溯
    path=[]
    a=dongtaiguihuabiao[0][0]
    x = a - sanjiao[0][0]
    path.append([0,0,sanjiao[0][0]])
    for i in range(1,len(sanjiao)):
        lie=0
        for j in range(i+1):
            if x==dongtaiguihuabiao[i][j]:
                path.append([i,j,sanjiao[i][j]])
                lie=j
                break
        x=x-sanjiao[i][lie]

    print("最大路径长度为：",dongtaiguihuabiao[0][0])

    for dian in path:
        print('经过点：',dian[0]+1,dian[1]+1,'该点的值为：',dian[2])

def diguichuangjian():
    sanjiao = [
        [9],
        [12, 15],
        [10, 6, 8],
        [2, 18, 9, 5],
        [19, 7, 10, 4, 16]]

    # 创建动态规划表
    dongtaiguihuabiao = [[-1 * float('INF') for i in range(len(sanjiao))] for j in range(len(sanjiao))]
    for i in range(len(sanjiao)):
        dongtaiguihuabiao[-1][i] = sanjiao[-1][i]

    def digui(i,j):
        if dongtaiguihuabiao[i][j]!=-1*float('INf'):
            return dongtaiguihuabiao[i][j]
        else:
            if i==len(sanjiao):
                dongtaiguihuabiao[i][j]=j
                return j
            else:
                dongtaiguihuabiao[i][j]=max(digui(i+1,j),digui(i+1,j+1))+sanjiao[i][j]
                return dongtaiguihuabiao[i][j]

    digui(0,0)
    #回溯
    path=[]
    a=dongtaiguihuabiao[0][0]
    x = a - sanjiao[0][0]
    path.append([0,0,sanjiao[0][0]])
    for i in range(1,len(sanjiao)):
        lie=0
        for j in range(i+1):
            if x==dongtaiguihuabiao[i][j]:
                path.append([i,j,sanjiao[i][j]])
                lie=j
                break
        x=x-sanjiao[i][lie]

    print("最大路径长度为：",dongtaiguihuabiao[0][0])

    for dian in path:
        print('经过点：',dian[0]+1,dian[1]+1,'该点的值为：',dian[2])

start=time.clock()
feidigui()
print('非递归创建动态规划表，用时',time.clock()-start)

start=time.clock()
diguichuangjian()
print('递归创建动态规划表，用时',time.clock()-start)