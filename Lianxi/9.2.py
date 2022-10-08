class restaurant():
    def __init__(self,name,type,number=0):
        self.name=name
        self.tpye=type
        self.number=number
    def describe_restaurant(self):
        print(self.name,' ',self.tpye)
    def open(self):
        print('这个餐馆正在营业')
    def jisuanrenshu(self):
        print('有',self.number,'人在这里就餐过')
    def set_number(self,number_1):
        self.number=number_1
    def increment_number_served(self,max):      #使就餐的人数增加
        self.number += max

a=restaurant('麦嘉基','china')
''' a.jisuanrenshu()
    a.number=10
    a.jisuanrenshu()'''         #直接修改属性
a.set_number(10)
print(a.number)
a.increment_number_served(1)
print(a.number)

class User():
    def __init__(self,first_name,last_name,*middle_name,login_attempts=0):
        self.fist_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name        #middle_name 保存在元组中
        self.longin=login_attempts
    def describe_user(self):
        print('you name is ',self.fist_name,' ',self.middle_name,' ',self.last_name)
    def greet_user(self):
        print('hello ',self.fist_name,' ',self.middle_name,' ',self.last_name)
    def increment_login_attempts(self):
        self.longin += 1
    def reset_login(self):
        self.longin=0

e=User('LW','WF','AWF')
e.increment_login_attempts()
e.increment_login_attempts()
e.increment_login_attempts()
print(e.longin)
e.reset_login()
print(e.longin)



