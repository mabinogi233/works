def insertSort(a,len):  #直接插入排序,插入排序
    for i in range(1, len):
        if a[i-1] > a[i]:
            t = a[i]
            j = i-1
            while a[j] > t and j >= 0:
                a[j+1] = a[j]
                j = j-1
            a[j+1] = t
    return a

#折半插入排序
def BinInsertSort(a,len):   #折半排序,插入排序
    for i in range(1, len):
        left = 0
        right = i - 1
        tmp = a[i]
        while left <= right:
            middle = (right + left) // 2
            if tmp < a[middle]: #插入点在左半区
                right = middle - 1
            else:
                left = middle + 1
        j = i - 1
        while j >= right+1:
            a[j + 1] = a[j]
            j += -1
        a[right+1] = tmp
    return a

def shell_sort(a):#希尔排序,插入排序
    n = len(a)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            while i >= gap and a[i] < a[i - gap]:
                a[i], a[i - gap] = a[i - gap], a[i]
                i -= gap
                #print(a)
        gap //= 2
    return a

def bubbleSort(nums):   #冒泡排序,交换排序
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def QuickSort(myList,start,end):    #快速排序,交换排序。end为数组索引
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

def select_sort(list):  #简单选择排序，选择排序
    k=0
    for i in range(len(list)-1):
        k=i
        for j in range(i+1,len(list)):
            if list[j]<list[k]:
                k=j
        if k!=i:
            list[i],list[k]=list[k],list[i]
    return list

def heap_sort(list):    #堆排序，选择排序
    # 最大堆调整
    def sift_down(lst, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break
    # 创建最大堆
    for start in range((len(list) - 2) // 2, -1, -1):
        sift_down(list, start, len(list) - 1)

    # 堆排序
    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        sift_down(list, 0, end - 1)
    return list

def cocktailSort(num_array):    #鸡尾酒排序，简单选择排序的变种
    flag=True
    for i in range(len(num_array)//2):
        if flag:
            flag=False
            #将最大值排到队尾
            for j in range(i,len(num_array)-i-1):
                if num_array[j]>num_array[j+1]:
                    num_array[j],num_array[j+1]=num_array[j+1],num_array[j]
                    flag=True
            #将最小值排到队首
            for j in range(len(num_array)-1-i,i,-1):
                if num_array[j]<num_array[j-1]:
                    num_array[j],num_array[j-1]=num_array[j-1],num_array[j]
                    flag=True
        else:
            break
    return num_array

def Merge(list):        #归并排序
    def merge_sort(li):
        # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
        if len(li) == 1:
            return li
        # 取拆分的中间位置
        mid = len(li) // 2
        # 拆分过后左右两侧子串
        left = li[:mid]
        right = li[mid:]
        # 对拆分过后的左右再拆分 一直到只有一个元素为止
        # 最后一次递归时候ll和lr都会接到一个元素的列表
        # 最后一次递归之前的ll和rl会接收到排好序的子序列
        ll = merge_sort(left)
        rl = merge_sort(right)
        # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
        # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
        return merge(ll, rl)
    # 这里接收两个列表
    def merge(left, right):
        # 从两个有顺序的列表里边依次取数据比较后放入result
        # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
        result = []
        while len(left) > 0 and len(right) > 0:
        # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
        result += left
        result += right
        return result
    return merge_sort(list)





