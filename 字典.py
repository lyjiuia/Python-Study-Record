#字典是一个无序、可变和有索引的集合。在Python中用“{}”表示，拥有键和值
thisdict = {'fruit':'apple','vegetables':'tomato','drink':'rio'}
print(thisdict)

#查找
print(thisdict['fruit'])
x = thisdict.get('vegetables')
print(x)

#更改
thisdict['fruit'] = 'banana'
print(thisdict)

#遍历字典，返回键和值
for y in thisdict:
    print(y)
for z in thisdict:
    print(thisdict[z])
for a,b in thisdict.items():
    print(a,b)

#增加与删除。除以下方法外，还可以用popitem与del，clear用来清空字典
thisdict['color'] = 'red'
print(thisdict)
thisdict.pop('fruit')
print(thisdict)

#复制字典
mydict = thisdict.copy()
print(mydict)

#嵌套字典
family = {'child1': {'name':'a','year':1999},
          'child2': {'name':'b','year':1994},
          'child3': {'name':'c','year':2007}}
print(family)
child1 = {'name':'Robot','year':1999}
child2 = {'name':'Tim','year':2000}
child3 = {'name':'Tom','year':2007}
family = {'child1':child1,'child2':child2,'child3':child3}
print(family)

#字典构造函数
thisdict = dict(brand = 'Porsche',model = 911,year = 2020)
print(thisdict)