#集合是无序和无索引的。在Python中用“{}”编写
thisset = {'apple', 'banana', 'cherry'}
print(thisset)

#因为集合无序且无索引，所以无法通过引用索引来访问set中的项目。但可以使用for循环来遍历set项目，或使用in关键字查询集合中是否存在指定值
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)
print('banana' in thisset)

#集合无法更改项目，但可以添加一个或多个项目
thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)
thisset = {'apple', 'banana', 'cherry'}
thisset.update(['orange','mango','grapes'])
print(thisset)

#删除可用remove()、discard()和pop()方法。区别在于若删除的项目元组中不存在，那么remove会报错，discard不会报错。
# 而pop删除的是集合最后一项。但是set是无序的，因此我们不会知道被删除的是什么项目。clear()清空集合，del删除整个集合

#合并集合
set1 = {'a','b','c','d','e','f','g','h','i'}
set2 = {'1','2','3','4','5','6','7','8','9'}
set3 = set1.union(set2)
print(set3)
set1 = {'a','b','c','d','e','f','g','h','i'}
set2 = {'1','2','3','4','5','6','7','8','9'}
set1.update(set2)
print(set1)

#集合构造函数
thisset = set(('apple', 'banana', 'cherry'))
print(thisset)