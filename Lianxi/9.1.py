class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.tpye=type
    def describe_restaurant(self):
        print(self.name,' ',self.tpye)
    def open(self):
        print('这个餐馆正在营业')

a=Restaurant('China','zhongshi')
b=Restaurant('Pinao','us')
c=Restaurant('King','uk')
a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()

class User():
    def __init__(self,first_name,last_name,*middle_name):
        self.fist_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name        #middle_name 保存在元组中
    def describe_user(self):
        print('you name is ',self.fist_name,' ',self.middle_name,' ',self.last_name)
    def greet_user(self):
        print('hello ',self.fist_name,' ',self.middle_name,' ',self.last_name)
d=User('li','Fe','hei','HIW')
e=User('LW','WF','AWF')
d.describe_user()
e.describe_user()