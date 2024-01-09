import pandas as pd
"""检查附件1和附件2中出现不同的单品号"""
df8 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\每月销售.xlsx')
df8['Month'] = pd.to_datetime(df8['Month'])
df8['Year'] = df8['Month'].dt.to_period('Y')
Year_sales = df8.groupby(['Year','单品编码'])['销量(千克)'].sum().reset_index()
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df8 = pd.merge(Year_sales, df6, on='单品编码', how='inner')
print(df8)