##获取数据类型
x = 10
print(type(x))

##列表是有序且可更改的集合。在Python中，列表用“【】“表示
list1 = ['apple', 'banana', 'cherry','orange','kiwi','melon','mango']
print((list1))
##访问列表
print(list1[0])
print(list1[-1])
print(list1[1:3])
print(list1[:2])
print(list1[2:])
print(list1[:])
print(list1[-4:-1])

##列表添加
list1.append("pear")
list1.insert(1,'strawberry')
print(list1)

##列表删除
#list1.remove('banana')
#print(list1)
#list1.pop()
#print(list1)

##del除了可以删除指定索引外，还可以删除整个列表
#del list1[0]
#print(list1)

##清空列表
#list1.clear()
#print(list1)

##复制列表
mylist = list1.copy()
print(mylist)
list2 = list(list1)
print(list2)

##合并列表
list3 = ['1','2','3']
list4 = list1 + list3
print(list4)
for x in list3:
    list1.append(x)
    print(list4)

