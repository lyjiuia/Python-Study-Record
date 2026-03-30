#Python当中的条件判断语句通常使用if和else，常见符号有>、<、==、!=、>=、<=
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('You can vote! Congratulations!')
elif age < 0:
    print('Plesee input correct age!')
else:
    print('Sorry, you are not allowed to vote!')

#Python中的循环语句通常是while循环和for循环
fruits = ['apple', 'banana', 'cherry','orange','kiwi','melon','mango']
for x in fruits:
    print(x)

for y in range(len(fruits)):
    print(y)

for z in range(0,10,2):
    print(z)

i = 1
while i <= 7:
    print(i)
    i += 1     #while循环中若条件为真，程序将会一直执行下去

code = int(input('请输入密码：'))
while  code != 123456:
    print('密码错误！请重新输入密码')
    code = int(input())
print('密码正确！')

#break语句在while条件为真时可以强行中断，避免陷入死循环
a = 1
while a <= 10:
    print(a)
    if a % 2 == 0:
        break
    a += 1
#若使用continue语句，我们可以停止当前的迭代，继续下一个
i = 1
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)

#嵌套循环
adj = ['red','yellow','green','blue']
fruits = ['apple','banana','cherry','orange']
for x in fruits:
    for y in adj:
        print(x,y)

#if语句不能为空。但是实际情况因某些原因写的if语句不完整，可以用pass语句避免报错
for x in [1,2,3,4,5,6,7,8,9,10]:
    pass