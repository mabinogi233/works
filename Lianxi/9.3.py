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

class IceRestaurant(restaurant):
    def __init__(self,name,type,number=0):
        super(IceRestaurant, self).__init__(name,type,number=0)  #super（）方法继承父类
    flavors=['apple','banana','peach']
    def dayin(self):
        for i in self.flavors:  #调用类中的变量 要用self.变量名
            print(i)

a=IceRestaurant('Labi','China')
a.dayin()


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

class Privileges():
    privileges=['can add post','can delete','can ban user']
    def show(self):
         print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,*middle_name):           #构造方法
        super(Admin, self).__init__(first_name,last_name,*middle_name)
    pri=Privileges()        #将privilege的实例作为Admin的属性

b=Admin('LI','mi','swifhiw')
b.pri.show()        #调用Admin实例b 中的属性pri 中的方法 show( )





