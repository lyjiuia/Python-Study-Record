import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(rc={'figure.figsize':(6,6)})
#分类色板
current_palette = sns.color_palette('Set1', n_colors=6) #color_palette不写参数则为默认颜色，set_palette设置所有图颜色
sns.palplot(current_palette)
plt.show()
#圆形画板
sns.palplot(sns.color_palette('hls', n_colors=8))
plt.show()

data = np.random.normal(size=(20,8)) + np.arange(8) / 2
sns.boxplot(data=data,palette=sns.color_palette('hls', n_colors=8))
plt.show()
#hls_palette()函数用来控制颜色的亮度和饱和度
sns.palplot(sns.hls_palette(8,l=7,s=9))
plt.show()
sns.palplot(sns.color_palette('Paired',10))
plt.show()

#xkcd包含了一套众包努力的针对随机RGB色的命名，产生了954个可以随机通过skcd_rgb字典中调用的命名颜色
plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw = 3)
plt.plot([0,1],[0,2],sns.xkcd_rgb['medium green'],lw = 3)
plt.plot([0,1],[0,3],sns.xkcd_rgb['denim blue'],lw = 3)
plt.show()

colors = ['windows blue','amber','greyish','faded green','dusty purple']
print(type(colors))
sns.palplot(sns.xkcd_palette(colors))
plt.show()
#连续画板
sns.palplot(sns.color_palette('Blues'))
sns.palplot(sns.color_palette('BuGn_r'))
plt.show()
#色调线性变换
sns.palplot(sns.color_palette('cubehelix',8))
plt.show()
sns.palplot(sns.cubehelix_palette(8,start=5,rot=-75))
plt.show()
sns.palplot(sns.cubehelix_palette(8,start=75,rot=-150))
plt.show()
#light_palette()和dark_palette()调用定制连续调色板
sns.palplot(sns.light_palette('green',10))
sns.palplot(sns.dark_palette('purple',10))
sns.palplot(sns.light_palette('navy',reverse=True))
plt.show()

data = np.random.multivariate_normal([0,0],[[1,-5],[-5,1]],size=300)
x,y = data[:,0],data[:,1]
pal = sns.dark_palette('green',as_cmap=True)
sns.kdeplot(x=x,y=y,cmap=pal)
plt.show()