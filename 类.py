#类(class)类似于对象构造函数，或者用于创建对象的“蓝图”。Python是一种面向对象的编程语言，几乎所有东西都是对象，拥有属性和方法。
#创建类使用class关键字，语法格式：
# class 类名：
      #类的内容（属性、方法）
      #类属性 = 初始值

#创建类与对象
class MyClass:
    x = 1
    y = 2
    z = 3
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)

#所有类都有一个名为init()的函数，它始终在启动类的时候执行。使用该函数将值赋给对象属性，或在创建对象时需要执行的其他操作：
#创建名为Person的类，使用_init_()函数为name和age赋值
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
p1 = Person('李四',63)
print(p1.name)
print(p1.age)

#对象也可以包含方法，其属于该对象的函数
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('你好！我叫' + self.name)
p1 = Person('Model',23)
p1.myfunc()

#self参数是对类当前实例的引用，用于访问属于该类的变量。它不必命名为self，可以随意调用它，但必须是函数中的首个参数
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print('Hello!my name is' + abc.name)
p1 = Person('Bob',23)
p1.myfunc()

#Python中的类分为子类与父类，两者属于继承与被继承关系
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.graduationyear = 2024
    def welcome(self):
        print('Welcome',self.firstname,self.lastname,'to the class of',self.graduationyear)
x = Person(firstname = 'Bob',lastname = 'Tim')
x.printname()
s2 = Student(firstname = 'Tina',lastname = 'Pat')
s2.printname()
s2.welcome()