import numpy as np
import pandas as pd
from scipy import stats,integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
x = np.random.normal(size=100)
sns.histplot(x,kde=False)
plt.show()
sns.histplot(x,bins=20,kde=False)
plt.show()
x = np.random.gamma(6,size=200)
sns.distplot(x,kde=False,fit=stats.gamma)
plt.show()

#根据均值和协方差生成数据,最好使用散点图
mean,cov = [0,1],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
df = pd.DataFrame(data,columns=['x','y'])
print(df)
sns.jointplot(x=df['x'],y=df['y'],data=df)
plt.show()

data1 = np.random.multivariate_normal(mean,cov,1000)
x,y = data1[:,0],data1[:,1]
with sns.axes_style("white"):
    sns.jointplot(x=x,y=y,kind='hex',color='lightgreen')
plt.show()

#多变量分析：以鸢尾花数据集为例
iris = pd.read_csv(r'F:\机器学习\第二章 第二模块：Python数据科学必备工具包实战\Seaborn\iris.data')
sns.pairplot(iris)
plt.show()

#regplot()和Implot()均可用来绘制回归关系，推荐regplot()
sns.set(color_codes=True)
np.random.seed(sum(map(ord,'regression')))
tips = pd.read_csv(r'F:\Seaborn\tips.csv')
print(tips.head())
sns.regplot(x=tips['total_bill'],y=tips['tip'],data=tips)
plt.show()
sns.regplot(data=tips,x='size',y='tip',x_jitter=.05)
plt.show()