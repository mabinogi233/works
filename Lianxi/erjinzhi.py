num=input('请输入一个二进制数')  #将二进制数转化为十进制
num=list(num)
sum=0
for i in range(len(num)):
    if num[i]=='1':
        sum=sum + 2**(len(num)-1-i)
print(sum)

