import pandas as pd
"""合并附件1和附件2"""
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df2 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件2.xlsx')
result = pd.merge(df1, df2, on='单品编码', how='inner')
result.to_csv('合并.csv')

"""统计三年品类的总销量"""
df3 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result =df3.groupby('分类名称')['销量(千克)'].sum().reset_index()
result.to_csv('三年品类总销量.csv')

"""统计品类为食用菌的销量"""
df4 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df4[df4['分类名称'] == '食用菌']
result.to_csv('食用菌.csv')

"""计算统计每个单品一天的总销量"""
df5 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
result = df5.groupby(['销售日期','单品编码'])['销量(千克)'].sum().reset_index()
result1 = pd.merge(result, df6, on='单品编码', how='inner')
result1.to_excel('每日销售量.xlsx')

"""统计每个单品每月的总销量"""
df7 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\result.xlsx')
# 将日期列转换为日期时间类型
df7['销售日期'] = pd.to_datetime(df7['销售日期'])
# 提取月份信息并添加到DataFrame中
df7['Month'] = df7['销售日期'].dt.strftime('%Y-%m')
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
# 使用groupby()和sum()计算每个月的销售量
monthly_sales = df7.groupby(['Month','单品编码'])['销量(千克)'].sum().reset_index()
df8 = pd.merge(monthly_sales, df6, on='单品编码', how='inner')
df8.to_excel('每月销售.xlsx')

"""检查附件1和附件2中出现不同的单品号"""
df8 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\每月销售.xlsx')
df8['Month'] = pd.to_datetime(df8['Month'])
df8['Year'] = df8['Month'].dt.to_period('Y')
Year_sales = df8.groupby(['Year','单品编码'])['销量(千克)'].sum().reset_index()
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df8 = pd.merge(Year_sales, df6, on='单品编码', how='inner')
print(df8)

df9 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
print(df9.nunique())

"""统计每个单品3年的总销量"""
df9 = df9.groupby('单品编码')['销量(千克)'].sum().reset_index()
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df9 = pd.merge(df9, df6, on='单品编码', how='inner')
df9.to_excel('单品总销量.xlsx')

df10 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df11 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
a = df10['单品编码'].unique()
b = df11['单品编码'].unique()
different_values = set(a).symmetric_difference(b)
print(different_values)

df12 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\每月销售.xlsx')
result = df12.groupby(['Month','分类名称'])['销量(千克)'].sum().reset_index()
result.to_excel('品类时间序列分析.xlsx')

"""筛选花叶类"""
df13 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df13 = df13[df13['分类名称'] == '花叶类']
df13.to_excel('花叶类.xlsx')

"""统计花叶类月销量"""
df14 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\花叶类.xlsx')
df14['销售日期'] = pd.to_datetime(df14['销售日期'])
df14['Month'] = df14['销售日期'].dt.strftime('%Y-%m')
monthly_sales = df14.groupby(['Month'])['销量(千克)'].sum().reset_index()

print(monthly_sales)

'''df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df15 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df15['销售日期'] = pd.to_datetime(df15['销售日期'])
df15['Month'] = df15['销售日期'].dt.strftime('%Y-%m')
monthly_sales = df15.groupby(['Month','分类名称'])['销售单价(元/千克)'].mean().reset_index()

monthly_sales.to_excel('每月销售单价.xlsx')'''

'''df16 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df17 =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df16['销售日期'] = pd.to_datetime(df16['销售日期'])
result = pd.merge(df16, df17, on=['销售日期','单品编码'])
result.to_excel('每日批发价格汇总.xlsx')'''
'''df17 = df16['销量(千克)']*df16['销售单价(元/千克)']
print(df17)'''

'''df18 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\每日批发价格汇总.xlsx')
df18['利润'] = df18['销量(千克)']*df18['销售单价(元/千克)']-df18['销量(千克)']*df18['批发价格(元/千克)']
result =df18.groupby('分类名称')['利润'].sum().reset_index()
print(result)'''

'''df19 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
df20 = df19.groupby(['分类名称','销售日期'])['销量(千克)'].sum().reset_index()
df21 = df19.groupby(['分类名称','销售日期'])['销售单价(元/千克)'].mean().reset_index()
result = pd.merge(df20, df21, on=['销售日期','分类名称'])
result1 = result[result['分类名称'] == '食用菌']
result1.to_excel('食用菌1.xlsx')'''










