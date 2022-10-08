
url_true=r"D:\codes\vivado_works\true_cache\cache_lab_v0.05\traces\cache_lab_trace.txt"
url_me=r"D:\codes\vivado_works\cache_lab_v0.05\cache_lab_v0.05\traces\cache_lab_trace.txt"
listy= []
listx=[]
with open(url_true,'r',encoding='utf-8')as f:
    for line in f.readlines():
        listy.append(line.strip("\n").split(" "))
with open(url_me,'r',encoding='utf-8')as f:
    for line in f.readlines():
        listy.append(line.strip("\n").split(" "))
conut = 0

for i in range(len(listx)):
    for j in range(listx[i]):
        if(listx[i][j]!=listy[i][j]):
            conut+=1
print(conut)