#seaborn是在matplotlib的基础上进行了封装，也就是对统计数据可视化
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(0, 7):
        plt.plot(x, np.sin(x + i * 5) * (7 - i) * flip)
sns.set()
sinplot()
plt.show()

sns.set_style("whitegrid")
data = np.random.normal(size=(20,6)) + np.arange(6) / 2
sns.boxplot(data=data)
plt.show()

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(0, 7):
        plt.plot(x, np.sin(x + i * 5) * (7 - i) * flip)
sns.set_style("white")
sinplot()
plt.show()

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(0, 7):
        plt.plot(x, np.sin(x + i * 5) * (7 - i) * flip)
sns.set_style("ticks")
sinplot()
plt.show()

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(0, 7):
        plt.plot(x, np.sin(x + i * 5) * (7 - i) * flip)
sinplot()
sns.despine()
plt.show()