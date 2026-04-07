#箱线图用于展示数据的分布特征和异常情况。它能直观地反应出数据的中心位置（中位数）、离散程度（四分位距）以及识别异常值。
# 语法格式：plt.boxplot(x,vert,patch_artist,showmeans)
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
np.random.seed(42)
class_a = np.random.normal(loc=80,scale=10,size=50)
class_b = np.random.normal(loc=70,scale=15,size=50)
class_c = np.random.normal(loc=85,scale=5,size=50)
data = [class_a,class_b,class_c]
plt.boxplot(data,vert=True,patch_artist=True,notch=True,showfliers=True,labels=['A','B','C'])
plt.title('三个班级数学成绩对比')
plt.xlabel('分数')
plt.grid(axis='x',color='k',linestyle='-',linewidth=0.5,alpha=0.3)
plt.show()

#有时我们希望在同一张画布上展示多张图表，这就用到了子图。语法格式：fig,axis = plt.subplots(nrows,ncols,figsize)
months = ['1月','2月','3月','4月','5月','6月']
sales = [1200,1500,1300,1800,2100,1900]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig,axis = plt.subplots(1,2,figsize=(10,5))
axis[0].plot(months,sales)
axis[0].set_title('折线图：销售趋势')
axis[0].set_xlabel('月份')
axis[0].set_ylabel('销售额度')
axis[1].bar(months,sales)
axis[1].set_title('柱状图：销售额数量差异')
axis[1].set_xlabel('月份')
axis[1].set_ylabel('销售额度')
plt.tight_layout()
plt.show()

#三角函数子图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x = np.linspace(0,2*np.pi,100)
fig,axes = plt.subplots(2,2,figsize=(10,8))
#左上sinx函数图像
axes[0][0].plot(x,np.sin(x),color='steelblue')
axes[0][0].set_title('sin(x)')
#右上cosx函数图像
axes[0][1].plot(x,np.cos(x),color='orange')
axes[0][1].set_title('cos(x)')
#左下tanx函数图像
axes[1][0].plot(x,np.tan(x),color='red')
axes[1][0].set_title('tan(x)')
axes[1][0].set_ylim(-5,5)
#右下sinx+cosx
axes[1][1].plot(x,np.sin(x)+np.cos(x),color='blue')
axes[1][1].set_title('sin(x)+cos(x)')
plt.suptitle('三角函数图像',fontsize=20)
plt.tight_layout()
plt.show()