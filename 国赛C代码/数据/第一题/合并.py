import pandas as pd
"""合并附件1和附件2"""
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df2 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件2.xlsx')
result = pd.merge(df1, df2, on='单品编码', how='inner')
result.to_csv('合并.csv')