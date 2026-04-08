import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from Seaborn介绍与基本操作 import sinplot

sns.set()
data = np.random.normal(size=(20,6)) + np.arange(6) / 2
sns.violinplot(data=data)
sns.despine(offset=10, trim=True)
plt.show()

sns.set_style("whitegrid")
data = np.random.normal(size=(20,6)) + np.arange(6) / 2
sns.boxplot(data=data)
sns.despine(left=True) #各个方向的轴线可以自行设置是否隐藏
plt.show()

with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()
plt.subplot(212)
sinplot(-1)
plt.show()

sns.set_context("paper")
plt.figure(figsize=(8,6))
sinplot()
plt.show()

sns.set_context("talk")
plt.figure(figsize=(8,6))
sinplot()
plt.show()

sns.set_context("notebook",font_scale=2,rc={"lines.linewidth": 2.5})
plt.figure(figsize=(8,6))
sinplot()
plt.show()