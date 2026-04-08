import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
sns.set(style='white',palette='muted',color_codes=True)

np.random.seed(sum(map(ord,'categorical')))
titanic = pd.read_csv(r'F:\Seaborn\titanic.csv')
tips = pd.read_csv(r'F:\Seaborn\tips.csv')
iris = pd.read_csv(r'F:\Seaborn\iris.csv')
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)
plt.show()
sns.swarmplot(x='day',y='total_bill',hue='sex',data=tips)
plt.show()
sns.boxplot(x='day',y='total_bill',hue='time',data=tips)
plt.show()
sns.violinplot(x='total_bill',y='day',hue='sex',data=tips,split=True)
plt.show()

#组合
sns.violinplot(x='day',y='total_bill',data=tips,inner=None)
sns.swarmplot(x='day',y='total_bill',data=tips,color='white',alpha=.5)
plt.show()

sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()

sns.pointplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()

sns.pointplot(x='class',y='survived',hue='sex',data=titanic,
              palette={'male':'g','female':'r'},
              markers=['^','o'],linestyles=['-','--'])
plt.show()
#宽型数据
sns.boxplot(data=iris,orient='h')
plt.show()
#多层面板分类图
sns.catplot(x='day',y='total_bill',hue='smoker',data=tips,kind='bar')
plt.show()
sns.catplot(x='day',y='total_bill',hue='smoker',col='time',data=tips,kind='swarm')
plt.show()
sns.catplot(x='time',y='total_bill',hue='smoker',col='day',data=tips,kind='box',height=4,aspect=.5)
plt.show()