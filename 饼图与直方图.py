#饼图适合展示各部分占整体的比例关系。比如市场份额、支出构成等，语法格式plt.pie(x,labels,autopct,explode,colors,startangle)
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
labels = ['餐饮','房租','交通','娱乐','其他']
sizes = [3500,3000,1000,1500,1000]
explode = [0.2,0.05,0.05,0.05,0.05]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=explode,shadow=True,startangle=90)
plt.title('月度支出构成')
plt.show()

#直方图用于展示数值型数据的分布情况，主要用于数据集中在哪些范围、是否呈现正态分布等。语法格式为plt.hist(x,bins,color.edgecolor,alpha)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
np.random.seed(42) #设置随机种子，保证每次运行生成的随机数值完全相同（便于复现结果）
scores = np.random.normal(loc=75,scale=5,size=200) #模拟200个学生的成绩，均值75，标准差10，
scores = np.clip(scores,0,100)
plt.hist(scores,bins=50,color='red',edgecolor='white',alpha=0.5)
plt.title('学生成绩分布')
plt.xlabel('分数')
plt.ylabel('人数')
plt.grid(axis='y')
plt.show()