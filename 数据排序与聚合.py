import pandas as pd
data = {'Name':['Alice','Bob','Charlie','David'],
        'Age':[20,30,40,50],
        'Gender':['Female','Male','Female','Male'],
        'Salary':[5000,10000,12000,15000]}
df = pd.DataFrame(data)
#按值排序
df_sorted = df.sort_values(by=['Age'],ascending=False)
print(df_sorted)
#按索引排序
df_sorted_by_index = df.sort_index(axis = 1)
print(df_sorted_by_index)

data = {'Department':['HR','Finance','IT','IT'],
        'Employee':['Alice','Bob','Charlie','David'],
        'Salary':[5000,10000,12000,15000]}
df = pd.DataFrame(data)
#按部门分组，并计算平均薪资
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)
grouped = df.groupby('Department').agg({'Salary':'mean'})
print(grouped)
grouped_multiple = df.groupby('Department').agg({'Salary':['mean','sum']})
print(grouped_multiple)

#创建透视表
pivot_table = df.pivot_table(values = 'Salary',index = 'Department',aggfunc = 'mean')
print(pivot_table)