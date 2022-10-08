import pulp
import time
import re
import xlrd

#使用字典存储节点
def input_poits():
    maxEnd = -1
    maxChildConut = 0
    #存储循环间依赖
    ref_list = []
    dict_poit = {}
    '''
    test = ["1,2,0,9,0,0,0,0,0,0,0,0,0","2,3,0,1,1,0,0,0,0,1,1,0,1","3,4,0,11,0,5,1,0,0,2,2,0,1","4,5,0,0,0,0,0,0,0,3,3,0,1",
            "5,6,0,0,0,0,0,0,0,4,4,0,1","6,7,0,0,0,0,0,0,0,5,5,0,1","7,8,0,0,0,0,0,0,0,6,6,0,1","8,0,0,0,0,0,0,0,0,7,7,0,1",
            "9,10,0,0,0,0,0,0,0,1,5,1,1","10,8,0,0,0,0,0,0,0,2,6,1,1","11,6,0,0,0,0,0,0,0,3,4,1,1"]
    n = 11
    '''

    n = int(input("输入节点个数"))
    print("请按照 节点编号,子节点i，边类型i,(……)，开始时间步，最晚开始时间步，节点类型，有无父节点 格式输出")
    for i in range(n):
        line = input()
        line_list = line.strip("\n").strip(" ").split(",")
        #是否拥有父节点
        fujiedian  = int(line_list[-1])
        #节点类型
        poitType = int(line_list[-2])
        #开始步
        start = int(line_list[-4])
        #结束步
        end = int(line_list[-3])
        #节点
        poit = int(line_list[0]) - 1
        dict_poit[poit] = {}
        dict_poit[poit]['child'] = []
        dict_poit[poit]['start'] = start
        dict_poit[poit]['end'] = end
        if(maxEnd<end):
            maxEnd = end
        dict_poit[poit]['type'] = poitType
        dict_poit[poit]['hasFather'] = fujiedian
        #子节点
        childconut = 0
        for i in range(1,len(line_list)-4,2):
            if(int(line_list[i])!=0):
                ref_type = int(line_list[i + 1])
                if(ref_type==0):
                    childconut += 1
                    dict_poit[poit]['child'].append(int(line_list[i])-1)
                if(ref_type==1):
                    ref_list.append({'start':int(line_list[0]),'end':int(line_list[i])})
        if(childconut>maxChildConut):
            maxChildConut = childconut

    #返回节点集合，最大的时间，节点个数
    return dict_poit,maxEnd,len(dict_poit.keys()),ref_list,maxChildConut


def read_xls(path):
    maxEnd = -1
    maxChildConut = 0
    #存储循环间依赖
    ref_list = []
    dict_poit = {}

    xlsf = xlrd.open_workbook(path)
    shxls = xlsf.sheet_by_name("Sheet1")
    for i in range(shxls.nrows):
        line_list = []
        if(i>=6):
            for j in range(shxls.ncols):
                line_list.append(int(shxls.cell(i,j).value))
            # 是否拥有父节点
            fujiedian = int(line_list[-1])
            # 节点类型
            poitType = int(line_list[-2])
            # 开始步
            start = int(line_list[-4])
            # 结束步
            end = int(line_list[-3])
            # 节点
            poit = int(line_list[0]) - 1
            dict_poit[poit] = {}
            dict_poit[poit]['child'] = []
            dict_poit[poit]['start'] = start
            dict_poit[poit]['end'] = end
            if (maxEnd < end):
                maxEnd = end
            dict_poit[poit]['type'] = poitType
            dict_poit[poit]['hasFather'] = fujiedian
            # 子节点
            childconut = 0
            for i in range(1, len(line_list) - 4, 2):
                if (int(line_list[i]) != 0):
                    ref_type = int(line_list[i + 1])
                    if (ref_type == 0):
                        childconut += 1
                        dict_poit[poit]['child'].append(int(line_list[i]) - 1)
                    if (ref_type == 1):
                        ref_list.append({'start': int(line_list[0]), 'end': int(line_list[i])})
            if (childconut > maxChildConut):
                maxChildConut = childconut



    return dict_poit, maxEnd, len(dict_poit.keys()), ref_list, maxChildConut



#创建ILP优化方程组
def create_ILP(dict_poit,maxEnd,poitConut,ref_list,maxChildConut,maxPE = 16,jiange=3):
    start_time = time.time()
    # x[i][j]==1 表示节点i可以在时间j开始执行
    x = pulp.LpVariable.dicts("x", ([i for i in range(poitConut)], [j for j in range(maxEnd+1)]), lowBound=0, upBound=1, cat='Integer')
    #加入优化目标，每个时间步使用的资源最小（min（max（Σ(j）x（i，j））= PEconut）
    tcs = pulp.LpProblem("TCS solve by ILP",pulp.LpMinimize)
    PEconut = pulp.LpVariable("PEconut", 0 ,maxPE, cat='Integer')
    tcs += PEconut
    #加入约束条件
    #加入资源约束 每个时间步的PE使用数量,
    # 每个时间步模Ⅱ相同的算子都会竞争资源
    list_pe_ref = {}
    for i in range(jiange):
        list_pe_ref[i] = pulp.lpSum([0])
    for j in range(0,maxEnd+1,1):
        list_pe_ref[j%jiange] += pulp.lpSum([x[i][j] for i in range(poitConut)])
    for i in range(jiange):
        tcs += list_pe_ref[i] <= PEconut

    #加入时间约束（起始时间的唯一性）Σ(j) x[i][j] == 1
    for i in range(poitConut):
        tcs += pulp.lpSum([x[i][j]for j in range(maxEnd+1)]) == 1

    #加入依赖约束
    for father_poit in dict_poit.keys():
        #每个节点要在约定的时间步内调度
        father_start = pulp.lpSum([k * x[father_poit][k] for k in range(maxEnd + 1)])
        tcs += father_start >= dict_poit[father_poit]['start']
        tcs += father_start <= dict_poit[father_poit]['end']
        for child_poit in dict_poit[father_poit]['child']:
            # child_poit的开始时间步在father_poit完成之后  默认每个算子执行周期为一（+1）
            father_start = pulp.lpSum([ int(k) * x[father_poit][k] for k in range(maxEnd+1) ])
            father_end = father_start + 1
            child_start = pulp.lpSum([ int(k) * x[child_poit][k] for k in range(maxEnd + 1 )])
            #依赖约束
            tcs += child_start - father_end >= 0

    #长依赖约束，循环间依赖长度不能为Ⅱ的整数倍
    n = pulp.LpVariable.dicts("n", ([i for i in range(len(ref_list))]), cat='Integer')
    b = pulp.LpVariable.dicts("b", ([i for i in range(len(ref_list))]),lowBound=1,upBound=jiange-1,cat='Integer')
    i = 0
    for ref in ref_list:
        father_poit = ref['start']
        child_poit = ref['end']
        #获取开始时间
        father_start = pulp.lpSum([int(k) * x[father_poit][k] for k in range(maxEnd + 1)])
        child_start = pulp.lpSum([int(k) * x[child_poit][k] for k in range(maxEnd + 1)])
        #时间间隔不能是Ⅱ的整数倍，|t| ！= n * Ⅱ，n>0 等价于 t ！= n * Ⅱ，n属于整数
        t = child_start - father_start
        #等于0表示t可以写成 n*jiange + b  b∈[1,jiange-1]的形式，表示t不能被Ⅱ整除
        tcs += t - jiange * n[i] - b[i] == 0
        i += 1
    #求解
    tcs.solve()
    end_time = time.time()
    #输出
    output(dict_poit,tcs,poitConut,maxEnd,maxChildConut,end_time-start_time)
    return tcs


def output(dict_poit,tcs_pulp,poit_conut,maxEnd,maxChildConut,time_used):
    if(pulp.LpStatus[tcs_pulp.status]=='Optimal'):
        listx = [[0 for i in range(maxEnd + 1)] for j in range(poit_conut)]
        for v in tcs_pulp.variables():
            if(v.name=='PEconut'):
                print("使用了PE：",v.varValue,"个")
            # 找到x
            if (re.match(r"x[^x]*", v.name)):
                i = int(v.name.split("_")[1])
                j = int(v.name.split("_")[2])
                listx[i][j] = int(v.varValue)

        # 输出调度结果
        print("节点编号", end='\t')
        print("时间步", end='\t')
        for i in range(maxChildConut):
            print("子节点" + str(i + 1), end='\t')
        print("节点类型", end='\t')
        print("原节点编号")
        for i in range(poit_conut):
            print(i + 1, end='\t\t\t')
            for j in range(maxEnd + 1):
                if (listx[i][j] == 1):
                    print(j, end='\t\t\t')
            childconut = 0
            for j in dict_poit[i]['child']:
                childconut += 1
                print(j + 1, end='\t\t')
            for j in range(maxChildConut - childconut):
                print(0, end='\t\t')
            print(dict_poit[i]['type'], end='\t\t\t')
            print(i + 1)
        print("调度时间：",time_used)
    else:
        print(pulp.LpStatus[tcs_pulp.status])
        print("调度失败")


if __name__ == "__main__":

    #dict_poit,maxEnd,poitConut,ref_list,maxChildConut = input_poits()

    #create_ILP(dict_poit,maxEnd,poitConut,ref_list,maxChildConut)

    dict_poit,maxEnd,poitConut,ref_list,maxChildConut = read_xls(r"D:\试验田\DFG-CQU\DFG_格式文件\g31.xlsx")
    create_ILP(dict_poit,maxEnd,poitConut,ref_list,maxChildConut,jiange=100)