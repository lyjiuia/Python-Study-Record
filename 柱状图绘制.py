#柱状图适合对比不同类别之间的数量差异。比如城市的销售额、各科目的考试成绩等。语法格式plt.bar(x,height,width,color,label)
#垂直：plt.barh(y,width,color,label)
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
cities = ['北京','上海','广州','深圳','杭州']
sales = [3200,2900,2600,2800,2300]
plt.bar(cities,sales,width=0.5,color='blue',label = '季度销售额')
plt.title('各城市季度销售额')
plt.xlabel('城市')
plt.ylabel('销售额（万元）')
plt.legend()
plt.show()

#分组柱状图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
cities = ['北京','上海','广州','深圳']
q1_sales = [3200,2900,2600,2800]
q2_sales = [3500,3100,2400,3000]
x = np.arange(1,len(cities)+1)
width = 0.3
print(x)
plt.bar(x,q1_sales,width = 0.3,label = 'Q1')
plt.bar(x+width,q2_sales,width = 0.3,label = 'Q2')
plt.xticks(x+width/2,cities)
plt.title('各城市Q1 vs Q2销售额')
plt.xlabel('城市')
plt.ylabel('销售额（万元）')
plt.legend()
plt.show()