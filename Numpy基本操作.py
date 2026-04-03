#Numpy是Python计算中的基础软件包。提供了多维数组对象、派生对象（如掩码数组和矩阵）以及用于数组快速操作的例程集合，包括数学运算、
# 逻辑运算、形状操作、排序、选择、I\O、离散傅里叶变换、基本线性代数、基本统计操作、随机模拟等

#创建数组
import numpy as np
a = np.array([1,2,3,4,5])
print(a)
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)

list1 = [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]],
         [[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]]
arr2 = np.array(list1)
print(arr2.shape) #形状
print(arr2.ndim) #维度
print(arr2.size) #个数
print(arr2.dtype) #类型

#基本数组创建
list2 = np.zeros((3,3))
print(list2)
list3 = np.ones((3,3))
print(list3)
list4 = np.empty(3) #内容随机，取决于内存
print(list4)
list5 = np.arange(3,0,-1)
print(list5)
for i in range(5):
    print(i)
list6 = np.linspace(0,1,5)
print(list6)