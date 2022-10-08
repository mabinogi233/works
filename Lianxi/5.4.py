people=['admin','tom','anna','frog','kim']
for people_1 in people:
    if people_1=='admin':
        print('Welcome admin')
    else:
        print('Hello '+people_1)

if people==[]:
    print('you need to find a people')
for i in range(len(people)):
    del people[0]
if people==[]:
    print('you need to find a people')

current_users=['admin','tom','anna','frog','kim']
new_users=['tamme','tom','aim','frog','labber']
for user in new_users:
    if user in current_users:
        print('The name '+user+' is used,please change the name')
    else:
        print('You can ues the name:'+user)

for i in range(len(current_users)):
    current_users[i].title()
for i in range(len(new_users)):
    new_users[i].title()

list=[i for i in range(1,10)]
for num in list:
    print(num)
for num in list:
    if num == 1:
        print(str(num)+'\nst\n')
    elif num ==2 :
        print(str(num) + '\nnd\n')
    elif num == 3:
        print(str(num) + '\nrd\n')
    else:
        print(str(num) + '\nth\n')



