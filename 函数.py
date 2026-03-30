#在Python中定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号，然后在缩进中编写函数体，最终返回值用return表示
def my_abs(x):
    if x >= 0:
        print(x)
    else:
        print(-x)
my_abs(7)

#Python函数中除了正常定义的必选参数外，还有默认参数、可变参数与关键字参数，使函数定义出来的接口不仅可以处理复杂的参数，还可以简化代码
def power(x):     #x为位置参数
    return x ** 2
print(power(5))

def power(x, n):  #x、n均为位置参数
    s= 1
    while n > 0:
        n = n-1
        s = s*x
    print(s)
power(2,5)

def power(x, n = 2):  #x为位置参数，n为默认参数。必选参数务必要在默认参数前
    s= 1
    while n > 0:
        n = n-1
        s = s*x
    print(s)
power(5)

def calc(numbers):  #numbers为可变参数，即个数可变
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc([1,2,3,4,5]))
print(calc([1,2,3,4]))

def person(name,age,**kw):  #最后一个为命名关键字参数
    print('name:',name,'age:',age,'other:',kw)
person('Jack',24,city = 'Beijing',adres = 'Franklin',zipcode = 123456)

def person(name,age,*,city,job):  #若想限制只能传入city和job两个参数，可以用*隔开。“*”后面就是命名关键字参数，调用时
                                  #必须以“参数名=值“的形式传入，且只能传入指定参数
    print(name,age,city,job)
person('Jack',24,city = 'Beijing',job = 'Engineer')


def person(name, age, *args, city, job):  # 若函数已有可变参数，那么后面的命名关键字参数就不需要再写*
    print(name, age,args, city, job)
person('Jack', 24,1,2, city='Beijing', job='Engineer')

#在函数内部可以调用其他函数。如果一个函数在内部调用自身本身，这个函数即为递归函数。如阶乘的计算
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(5))
print(fact(100))

#Lambda函数是一个小的匿名函数，可接受任意数量的参数，但只能有一个表达式。语法Lambda arguments:expression执行表达式并返回结果
# 常作为一个大函数框架下的内部匿名函数
x = lambda a: a * 2
print(x(5))
x = lambda a,b: a * b
print(x(5,6))

def myfunc(n):
    return lambda a: a*n
mydouble = myfunc(2)
mytriple = myfunc(3)
print(mydouble(5))
print(mytriple(5))