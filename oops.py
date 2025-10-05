#this program is about oops

#making class using inheretence concept

#single level inheretence
class car:
    color = "black"

    @staticmethod
    def start():
        print("car is started")
    
    @staticmethod
    def stop():
        print("car is stop..")


class toyota(car):
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def show_info(self):
        print("name:",self.name)
        print("model:",self.model)
        print(self.color)
        self.start()
        self.stop()    

c1 = toyota("honda civic",2016)
c1.show_info()

#single multi-level inheretence
class car1:
    @staticmethod
    def start():
        print("car is started")
    
    @staticmethod
    def stop():
        print("car is stop..")

class toyota1(car1):
    def __init__(self,brand):
        self.brand = brand

class fortuner1(toyota1):
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def show_info(self):
        print("name:",self.name)
        print("model:",self.model)
        self.start()
        self.stop()    

c1 = fortuner1("honda civic",2016)
c1.show_info()

#multiple inheretence
class A:
    a1 = "class A"

class B:
    a2 = "class B"

class C(A,B):
    a3 = "class C"

c1 = C()
print(c1.a1)
print(c1.a2)
print(c1.a3)


#use super() function in inheretence
class person:

    def __init__(self,name,fname,age):
        self.name = name
        self.fname = fname
        self.age = age

    def show(self):
        print("name: ",self.name)
        print("father name: ",self.fname)
        print("age: ",self.age)
        

class student(person): 
    
    def __init__(self,name,fname,age,roll_no,field_study):
        super().__init__(name,fname,age)
        self.field_study = field_study
        self.roll_no = roll_no
    
    def show(self):
        print("information of student")
        super().show()
        print("roll no:",self.roll_no)
        print("field of study:",self.field_study)

class teacher(person): 
    
    def __init__(self,name,fname,age,field_teaching):
        super().__init__(name,fname,age)
        self.field_teaching = field_teaching
    
    def show(self):
        print("information of teaching")
        super().show()
        print("field of teaching:",self.field_teaching)

s1 = student("saifullah","khalid",20,101,"BS CS")
s1.show()
t1 = teacher("salman","akbar",30,"english")
t1.show()


#class which uses static and class decorator
class A:
    name = "saifullah"

    @staticmethod
    def eat():
        print("eating..")
   
    @classmethod
    def changename(classattribute):
        classattribute.name = "salim"
        print("name changed to ",classattribute.name)
a1 = A()

a1.eat()
print(a1.name)
a1.changename()


#class is about to use property decorator
class student1:
    def __init__(self,phton,cpp,java):
        self.phyton = phton
        self.cpp = cpp
        self.java = java

    @property
    def percentage(self):
        return  ((self.phyton + self.cpp + self.java) / 3)

stu1 = student1(89,98,78)
print(stu1.percentage())

# s1.phyton = 99        
# s1.percentage()        
        

#making private class attribute

class bank_account1:

    def __init__(self,account_no,account_pass):
        #to express attribute as private we use '__' before attribute
        self.__account_no = account_no
        self.__account_pass = account_pass

    def __reset_pass_account(self):
        print("account no:",self.__account_no)
        print("account password:",self.__account_pass)
    
    def bank_user(self):
        self.answer = input("Are you a user of this bank: y/n :")
        if(self.answer == "y" or self.answer == "Y"):
            self.__reset_pass_account()
        elif(self.answer == "n" or self.answer == "N"):
            print("you are not eleigible to reset your account:")
        else:
            print("you enter wrong character:")
        
account1 = bank_account1(1230,"saif123")
account1.bank_user()









#class of student that take name and marks of student and print its average
class student:
    def __init__(self,name,python,java,cpp):
        self.name = name
        self.python = python
        self.java = java
        self.cpp = cpp

    @staticmethod
    def hello():
        print("hello! saifullah")

    def average(self):
        return (self.python + self.java + self.cpp)/3
    
#class object declaration and calling
s1 = student("saifullah",100,100,100)
print(s1.average())
s1.hello()

#this is a class which is used to createa account and its detail of balance
class bank_account:
    balance = 0
    def __init__(self,account_no):
        self.__account_no = account_no

    def debit(self):
        print("please debit/remove your money")
        self.amount_debit = float(input("enter amount you want to debit:"))
        self.balance -=self.amount_debit

    def credit(self):
        print("please credit/save your money")
        self.amount_credit = int(input("enter amount you want to credit:"))
        self.balance  +=self.amount_credit


    def balance_show(self):
        print("your total balance: ",self.balance  )
    
    def show_account(self):
        print(self.__account_no)


user1 = bank_account(12345)
print(user1.show_account())

user1.credit()
user1.debit()
user1.balance_show()
        

#class is about police academy
class police:
    
    police_land_name = "kabal police land"
    list_roll_no = []
    def __init__(self,roll_no,name,fname,age):
        
        self.roll_no = roll_no
        self.name = name
        self.fname = fname
        self.age = age

    
    def show_info(self):
        self.list_roll_no.append(self.roll_no)
        print("information of condidate ",self.roll_no)
        print("name: ",self.name)
        print("father name: ",self.fname)
        print("age: ",self.age)
        print("police lane name: ",self.police_land_name)
        


condidate_1 = police(1,"salman","waleed",24)
condidate_2 = police(2,"akbar","aimal",21)
condidate_3 = police(3,"waqas","junaid",29)
condidate_1.show_info()
condidate_2.show_info()
condidate_3.show_info()
print("all roll no:",police.list_roll_no)
print("found" if police.list_roll_no.index(1,0,len(police.list_roll_no))==True else "not found")