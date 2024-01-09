import pandas as pd
df9 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
print(df9.nunique())

"""统计每个单品3年的总销量"""
df9 = df9.groupby('单品编码')['销量(千克)'].sum().reset_index()
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df9 = pd.merge(df9, df6, on='单品编码', how='inner')
df9.to_excel('单品总销量.xlsx')