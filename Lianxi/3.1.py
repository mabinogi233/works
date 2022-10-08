name=['Anna','Tom','Tim']
for i in range(len(name)):
    print(name[i])

Wenhou='Holle,nice to meet you,'
for i in range(len(name)):
    print(Wenhou+name[i])

tongqin=['bike','car']
for i in range(len(tongqin)):
    if tongqin[i]=='bike':
        print('l like ride '+tongqin[i])
    elif tongqin[i]=='car':
        print('l like drive '+tongqin[i])
    else:
        continue
