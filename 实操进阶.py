import numpy as np
#排序、连接和重塑
arr = np.array([10,6,8,5,3])
arr1 = np.sort(arr) #升序
arr2 = np.sort(arr)[::-1] #降序
print(arr1)
print(arr2)
#连接
c = np.array([1,2,3,4,5])
d = np.array([6,7,8,9,10])
e = np.concatenate((c,d))
print(e)
#重塑
f = np.array([1,2,3,4,5,6,7,8,9,10])
g = f.reshape((5,2))
print(g)
#添加数组维度
h = np.array([1,2,3,4,5,6,7,8,9,10])
h1 = h[np.newaxis,:]
print(h1)
print(h1.shape)

col_vector = h[:,np.newaxis]
print(col_vector)
print(col_vector.shape)

J = np.expand_dims(col_vector,axis=0)
print(J)

#索引和切片
data = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
#[1,2,3,4,5]
print(data[0])
#3
print(data[0,2])
#[[2,3]，[7,8]]
print(data[0:2,1:3])

#数组堆叠拆分与数学运算
a1 = np.array([[1,2],
               [3,4]])
a2 = np.array([[5,6],
               [7,8]])
b1 = np.vstack([a1,a2])  #垂直堆叠
b2 = np.hstack([a1,a2])  #水平堆叠
print(b1)
print(b2)

x = np.arange(1,25).reshape((2,12))
x1 = np.hsplit(x,3)
x2 = np.hsplit(x,(3,5))
print(x1)
print(x2)

#运算
data1 = np.array([[1,2,3],[4,5,6]])
data2 = np.array([[7,8,9],[10,11,12]])
data3 = data1 + data2
data4 = data2 - data1
data5 = data1 * data2
data6 = data1 / data2
print(data3)
print(data4)
print(data5)
print(data6)

#数组聚合与矩阵变形
y = np.array([1,2])
print(y.max())
print(y.min())
print(y.sum())
print(y.mean())
print(y.var())
print(y.std())
print(y.prod())

y1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y1.max(axis=0))
print(y1.min(axis=0))
print(y1.sum(axis=0))

z = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
z1 = z.reshape((5,3))
z2 = z.transpose()
print(z1)
print(z2)

#均方差计算
y_pred = np.array([1,2,3])
n = len(y_pred)
y2 = np.array([1,1,1])
error = 1/n * np.sum(np.square(y_pred - y2))
print(error)