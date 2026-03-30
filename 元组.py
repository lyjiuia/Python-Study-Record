##元组是有序且不可更改的集合。用”（）“表示
a = ('apple', 'banana', 'cherry','orange','kiwi','melon','mango')
print((a))

##访问元组
print(a[0])

##创建元组后，将无法更改其值。但是有一种解决方法，可以将元组转换为列表，更改里面的值，然后将列表转换回元组。
# 但不可添加元素和删除元组里的元素，只可以用del删除整个元组
x = ('apple', 'banana', 'cherry','orange','kiwi','melon','mango')
y = list(x)
y[1] = 'origin'
x = tuple(y)
print(x)

##创建只有一个项目的元组时，必须在该项目后添加一个括号
thistuple = ('apple',)
print(type(thistuple))
##不是元组
thistuple = ('apple')
print(type(thistuple))

#tuple()构造函数
thistuple = tuple(('apple', 'banana', 'cherry', 'orange'))
print(thistuple)