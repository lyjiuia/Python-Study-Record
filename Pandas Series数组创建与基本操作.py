#Pandas Series类似于一维数组，由一组数据与索引构成,结构类似于字典。一般使用函数Series(data,index,dtype,copy)来构造，
# 其类型与是否复制要指定参数

#创建Series
import numpy as np
import pandas as pd
#ndarray创建，使用默认索引
arr = np.array([1,2,3,4,5])
s = pd.Series(arr)
print(s)
#ndarray创建，并指定索引
arr1 = np.array(['a','b','c','d','e'])
s1 = pd.Series(arr1,index=[100,101,102,103,104])
print(s1)
#字典创建
data = {'a':0,'b':1,'c':2,'d':3,'e':4}
s2 = pd.Series(data)
print(s2)
#标量创建
s3 = pd.Series(5,index=[1,2,3,4,5])
print(s3)

#Series数据访问
x = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(1,x.iloc[0]) #位置
print(1,x['a']) #标签
print(x[0:3])
print(x[['a','b','c','d']])
print(x.axes)  #索引列表
print(x.index) #索引值
print(x.dtype) #数据类型
print(x.size) #大小
print(x.ndim) #维度
print(x.values) #返回值
print(x.empty) #判断是否为空

#查看前几行/后几行的数据
y = pd.Series(np.random.randn(5))
print("The original series is:")
print(y)
print(y.head())
print(y.tail())

#查看缺失值
z = pd.Series([1,2,3,4,None])
print(pd.isnull(z))
print(pd.notnull(z))