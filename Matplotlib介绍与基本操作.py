#Matplotlib是Python中最流行的数据可视化库，可以将数据转为折线图、散点图、饼图、柱状图等等。核心模块为matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
#图表初步绘制
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]
plt.plot(x,y)
plt.show()

#添加图例、X轴、Y轴、标题、网格
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]
plt.plot(x,y,label = '线性增长')
plt.title('我的第一张图表')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.legend()
plt.grid(True)
plt.show()