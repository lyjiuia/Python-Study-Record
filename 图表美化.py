#matplotlib里面内置了多种主题风格，使用仅需一行代码。保存图表的语法格式plt.savefig(fname,dpi,bbox_inches,transparent)
import matplotlib.pyplot as plt
import numpy as np
from unicodedata import category

print(plt.style.available)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.style.use('bmh')
months = ['1月','2月','3月','4月','5月','6月']
sales = [1200,1500,1300,1800,2100,1900]
plt.plot(months,sales,color='steelblue',marker='o',label='月销售额')
plt.title('月度销售额')
plt.xlabel('月份')
plt.ylabel('销售额（万元）')
plt.legend()
plt.savefig('test.png',dpi=300,bbox_inches='tight')
plt.show()
plt.style.use('default')

#综合数据分析报告
months = ['1月','2月','3月','4月','5月','6月']
revenue = [12000,15000,13000,18000,21000,19000]
orders = [320,410,370,500,500,530]
categorys = ['电子','服装','食品','家居','其他']
categorys_pct = [35,25,20,12,8]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

np.random.seed(1)
price = np.random.randint(50,500,100)
clicks = price * 2 + np.random.randn(100) * 80
fig,axes = plt.subplots(2,2,figsize=(10,8))
plt.suptitle('某电商平台上半年运营数据概览',fontsize=20,fontweight='bold')
#左上：营收趋势折线图
axes[0][0].plot(months,revenue,color = 'red',linestyle = '--',linewidth = 2,marker = 'o',label = '月营收')
axes[0][0].set_title('月营收趋势')
axes[0][0].set_xlabel('月份')
axes[0][0].set_ylabel('营收（元）')
axes[0][0].legend()
axes[0][0].grid(True)
#右上：月订单量柱状图
axes[0][1].bar(months,orders,width = 0.3,color = 'blue',label = '月订单量')
axes[0][1].set_title('月订单量')
axes[0][1].set_xlabel('月份')
axes[0][1].set_ylabel('订单数')
axes[0][1].legend()
#左下：商品价格与点击量散点图
axes[1][0].scatter(price,clicks,s = 60,c = 'seagreen',alpha = 1,label = '商品价格与点击量关系')
axes[1][0].set_title('商品价格 vs 点击量')
axes[1][0].set_xlabel('点击量')
axes[1][0].set_ylabel('商品价格（元）')
axes[1][0].legend()
axes[1][0].grid(True)
#右下：商品销售占比饼图
axes[1][1].pie(categorys_pct,labels = categorys,autopct = '%1.1f%%',shadow = False,startangle = 90)
axes[1][1].set_title('商品销售占比')

plt.tight_layout()
plt.savefig('电商平台上半年月度运营报告.png',dpi=300,bbox_inches='tight')
plt.show()
plt.style.use('default')