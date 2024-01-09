import pandas as pd
"""统计每个单品每月的总销量"""
df7 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\数据\合并.csv')
# 将日期列转换为日期时间类型
df7['销售日期'] = pd.to_datetime(df7['销售日期'])
# 提取月份信息并添加到DataFrame中
df7['Month'] = df7['销售日期'].dt.strftime('%Y-%m')
df6 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
# 使用groupby()和sum()计算每个月的销售量
monthly_sales = df7.groupby(['Month','单品编码'])['销量(千克)'].sum().reset_index()
df8 = pd.merge(monthly_sales, df6, on='单品编码', how='inner')
df8.to_excel('每月销售.xlsx')