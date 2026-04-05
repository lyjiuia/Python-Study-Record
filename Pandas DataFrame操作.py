#DataFrame是Pandas中的数据结构，它是一种类似于SQL或电子表格的二维数据结构。由一组有序的列组成，每一列都可以是不同的数据类型。
#这好比一个Series容器，又好像是共享同一个索引的Series集合
import pandas as pd
#创建DataFrame
data = [['Alex',10],['Bob',12],['Clarke',10]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
#通过字典创建
data = {'Name':['Tom','Jerry','Tim','Steve'],'Age':[10,20,25,28]}
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
#通过Series创建
s1 = pd.Series([1,2,3],name = 'A')
s2 = pd.Series([4,5,6],name = 'B')
df = pd.DataFrame({'A':s1,'B':s2})
print(df)

#访问DataFrame数据
data1 = {'Name':['Tom','Jack','Peter','Tim'],'Age':[10,20,30,40]}
df = pd.DataFrame(data1,index = ['rank1','rank2','rank3','rank4'])
print(df['Name']) #列
print(df.loc['rank2']) #行
print(df.iloc[1]) #行
df['Score'] = [90,85,88,92] #添加新列
print(df)
age_colunms = df.pop('Age')#删除
del df['Score'] #删除
print(df)

#DataFrame常见属性和方法
data1 = {'Name':['Tom','Jack','Peter','Tim'],'Age':[10,20,30,40]}
df = pd.DataFrame(data1)
print(df.T) #转置
print(df.axes)
print(df.index)
print(df.columns)
print(df.head(2))
print(df.tail(1))