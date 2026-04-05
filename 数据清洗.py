#数据清洗是对一些没有用的数据进行处理的过程。很多数据集存在缺失、数据格式错误、错误数据或重复数据的情况，为了使数据集
# 更加准确，所以要进行清洗
import pandas as pd
df = pd.read_csv(r'F:\机器学习\第二章 第二模块：Python数据科学必备工具包实战\pandas\1_Pandas(1)(1)\Pandas\Pandas代码\macrodata.csv')
print(df.head())
#清洗空值 DataFrame.dropna(axis=,how=,thresh=None,subset=None,inplace=False)
print(df['pop'])
print(df['realinv'].isnull())
new_df = df.dropna()
print(new_df.to_string())
#指定空数据类型
missing_values = ['n/a','na','--']
df = pd.read_csv(r'F:\机器学习\第二章 第二模块：Python数据科学必备工具包实战\pandas\1_Pandas(1)(1)\Pandas\Pandas代码\macrodata.csv',na_values=missing_values)
print(df['pop'])
print(df['realinv'].isnull())
#删除包含空数据的行
new_df = df.dropna()
print(new_df.to_string())
#修改源数据
df.dropna(inplace=True)
print(df.to_string())
#移除指定列有空值的行
df.dropna(subset=['realinv'],inplace = True)
print(df.to_string())
#替换空字段
df.fillna(12345,inplace=True)
print(df.to_string())
#使用统计值替换空字段(平均值、中位数、众数）
x = df['pop'].mean()
print(x)
df['pop'].fillna(x,inplace=True)
print(df.to_string())

#清洗格式错误数据
data = {'Date':['2020/12/01','2020/12/02','2020/12/03','2020-12-04'],'duration':[50,40,45,60]}
df = pd.DataFrame(data,index = ['day1','day2','day3','day4'])
#强制转换日期格式
df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
print(df.to_string())
#直接替换
person = {'name':['Google','Runoob','Taobao'],'age':[50,40,12345]}
df = pd.DataFrame(person)
df.loc[2,'age'] = 30
print(df.to_string())
#设置条件语句
for x in df.index:
    if df.loc[x,'age'] > 120:
        df.loc[x,'age'] = 120
print(df.to_string())
#删除错误行
for x in df.index:
    if df.loc[x,'age'] > 120:
        df.loc(x,inplace=True)
print(df.to_string())
#清洗重复数据
person = {'name':['Google','Runoob','Taobao','Kaggle'],'age':[50,40,40,70]}
df = pd.DataFrame(person)
df.drop_duplicates(inplace=True)
print(df.to_string())