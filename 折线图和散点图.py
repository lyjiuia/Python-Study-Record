#折线图语法格式plt.plot(x,y,color,linestyle,linewidth,marker,label)
#单个折线图
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
months = ['1月','2月','3月','4月','5月','6月']
sales = [1200,1500,1300,1000,2100,1900]
plt.plot(months,sales,color = 'r',linestyle = '--',linewidth = 2,marker = 'o',label = '每月的销售额')
plt.title('上半年月销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额（元）')
plt.legend()
plt.grid(True)
plt.show()

#多个折线图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
months = ['1月','2月','3月','4月','5月','6月']
sales_a = [1200,1500,1300,1000,2100,1900]
sales_b = [800,1000,1200,1100,2100,2000]
plt.plot(months,sales_a,color = 'r',linestyle = '--',linewidth = 2,marker = 'o',label = 'a部门每月的销售额')
plt.plot(months,sales_b,color = 'b',linestyle = '-',linewidth = 2,marker = 'o',label = 'b部门每月的销售额')
plt.title('a、b部门上半年月销售额趋势对比')
plt.xlabel('月份')
plt.ylabel('销售额（元）')
plt.legend()
plt.grid(True)
plt.show()

#散点图适合展示两个变量之间的关系，如身高与体重、广告投入与销售额。语法格式为plt.scatter(x,y,s,c,alpha,label)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
height = np.random.randint(155,190,50)
weight = height * 0.45 + np.random.randn(50) * 5 #+/-5kg
plt.scatter(height,weight,s = 60,c = 'r',alpha = 1,label = '样本数据')
plt.title('身高与体重的关系')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.grid(True)
plt.show()