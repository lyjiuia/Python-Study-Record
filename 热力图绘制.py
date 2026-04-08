import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import uniform
from seaborn import heatmap

np.random.seed(0)
sns.set()

uniform_data = np.random.rand(3,3)
print(uniform_data)
heatmap = sns.heatmap(uniform_data)
plt.show()
ax = sns.heatmap(uniform_data,vmin=0.2,vmax=0.5)
plt.show()

normal_data = np.random.randn(3,3)
print(normal_data)
ax1 = sns.heatmap(normal_data,center=0)
plt.show()

flights = pd.read_csv(r'F:\Seaborn\flights.csv')
print(flights.head())
flights = flights.pivot(index='month',columns='year',values='passengers')
print(flights)
ax = sns.heatmap(flights)
plt.show()
ax = sns.heatmap(flights,annot=True,fmt='g')
plt.show()
ax = sns.heatmap(flights,linewidths=.5,annot=True,fmt='g')
plt.show()
ax = sns.heatmap(flights,cmap='YlGnBu')
plt.show()
ax = sns.heatmap(flights,cbar=False,cmap='YlGnBu') #cbar可以设置是否隐藏
plt.show()