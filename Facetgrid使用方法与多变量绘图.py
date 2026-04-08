import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
sns.set(style='white',palette='muted',color_codes=True)
np.random.seed(sum(map(ord,'axis_grids')))

tips = pd.read_csv(r'F:\Seaborn\tips.csv')
print(tips.head())
g = sns.FacetGrid(tips,col='time')
g.map(plt.hist,'tip')
g.add_legend()
plt.show()

g = sns.FacetGrid(tips,col='sex',hue='smoker')
g.map(plt.scatter,'total_bill','tip',alpha=0.5)
g.add_legend()
plt.show()

g = sns.FacetGrid(tips,row='smoker',col='time',margin_titles=True)
g.map(sns.regplot,'size','total_bill',color='blue',fit_reg=False,x_jitter=.1)
g.add_legend()
plt.show()

g = sns.FacetGrid(tips,col='day',height=4,aspect=5)
g.map(sns.barplot,'sex','total_bill')
g.add_legend()
plt.show()

from pandas import Categorical
ordered_days = tips.day.value_counts().index
print(ordered_days)
ordered_days = Categorical(['Thur','Fri','Sat','Sun'])
g = sns.FacetGrid(tips,row='day',row_order=ordered_days,height=1.7,aspect=4)
g.map(sns.boxplot,'total_bill')
plt.show()

pal = dict(Lunch='seagreen',Dinner='pink')
g = sns.FacetGrid(tips,hue='time',palette=pal,height=5)
g.map(plt.scatter,'total_bill','tip',s=50,alpha=0.5,linewidth=.5,edgecolor='white')
g.add_legend()
plt.show()

g = sns.FacetGrid(tips,hue='sex',palette='Set1',height=5,hue_kws={'marker':['^','v']})
g.map(plt.scatter,'total_bill','tip',s=100,alpha=0.5)
g.add_legend()
plt.show()

with sns.axes_style('white'):
    g = sns.FacetGrid(tips,row='sex',col='smoker',margin_titles=True,height=2.5,aspect=4)
g.map(plt.scatter,'total_bill','tip',color='#334488',edgecolor='white',lw=.5)
g.set_axis_labels('Total bill(US Dollar)','Tip')
g.set(xticks=[10,30,50],yticks=[2,6,10])
g.fig.subplots_adjust(wspace=.02,hspace=.02)
plt.show()

iris = pd.read_csv(r'F:\Seaborn\iris.csv')
g = sns.PairGrid(iris)
g.map(plt.scatter)
plt.show()

g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.show()

g = sns.PairGrid(iris,hue='species')
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()
plt.show()

g = sns.PairGrid(iris,vars=['sepal_length','sepal_width'],hue='species')
g.map(plt.scatter)
plt.show()

g = sns.PairGrid(tips,hue='size',palette='GnBu_d')
g.map(plt.scatter,s=50,edgecolor='white')
g.add_legend()
plt.show()