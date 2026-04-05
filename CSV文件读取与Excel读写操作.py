#CSV（Comma-Seperated Values，逗号分隔值），有时也称字符分隔值。是一种以纯文本形式存储表格的通用的简单文件形式，被用户、商业和
# 科学领域广泛使用。核心方法有pd.read_csv(‘文件路径’，sep='',headers（列标签）=,names=[],dtype={} )
# 和DataFrame.to_csv(‘文件路径’，‘index = True/False,header = True,columns = [])
import pandas as pd
#读取csv文件，并自定义列名和分隔符
df = pd.read_csv(r'F:\机器学习\第二章 第二模块：Python数据科学必备工具包实战\pandas\1_Pandas(1)(1)\Pandas\Pandas代码\tips.csv')
print(df.to_string()) #to_string()是返回完整的DataFrame数据，否则只显示前5行和后5行
#将DataFrame写入csv
#三个字段
name = ['Google','Kaggle','Github','Taobao']
site = ['www.google.com','www.kaggle.com','www.github.com','www.taobao.com']
age = [40,50,60,70]
#传入字典
dict = {'name':name,'site':site,'age':age}
df = pd.DataFrame(dict)
#保存csv
df.to_csv(r'F:\Pandas学习\site.csv')
print(df.head())
print(df.tail())
print(df.info())

#to_excel()用来写入文件。写入单个对象要指定目标文件名，写入多个对象要创建一个带有目标文件名的ExcelWriter对象，并用sheet_name参数
# 依次指定工作表名称。里面常用参数有excel_writer,sheet_name,na_rep=,float_format,columns
info_website = pd.DataFrame({'name':['编程帮','C语言中文网','微学苑','92python'],
                             'Language':['PHP','C','PHP','Python'],
                             'url':['www.biancheng.com','c.biancheng.net','www.weixueyuan.com','www.92python.com']})
info_user = pd.DataFrame({'username':['user1','user2','user3','user4'],
                          'visit_count':[100,150,180,200]})
#创建ExcelWriter对象
writer = pd.ExcelWriter(r'F:\Pandas学习\website.xlsx')
info_website.to_excel(writer,sheet_name='website',index = False)
info_user.to_excel(writer,sheet_name='用户访问',index = False)
writer.close()
print('多工作表写入成功')

#pd.read_excel用于读取Excel文件
# (io,sheet_name=,header=,names=,index_col=,usecols=,squeeze=,skiprows=,converters=,nrows=,skipfooter=)
df = pd.read_excel(r'F:\Pandas学习\website.xlsx',index_col = 'name',skiprows = [1])
#处理未命名列
df.columns = df.columns.str.replace('Unnamed: 0','col_label')
print(df)