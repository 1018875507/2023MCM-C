import pandas as pd
df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df5 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df5.groupby(['销售日期','单品编码'])['销量(千克)'].sum().reset_index()
df5['本次销售额'] =df5['销量(千克)']*df5['销售单价(元/千克)']

df6 = df5.groupby(['销售日期','单品编码'])['本次销售额'].sum().reset_index()
result1 = pd.merge(result, df6, on=['单品编码','销售日期'], how='inner')
result2 = pd.merge(df, result1, on='单品编码', how='inner')
result3 = result2.groupby(['分类名称','销售日期'])['销量(千克)'].sum().reset_index()
result4 = result2.groupby(['分类名称','销售日期'])['本次销售额'].sum().reset_index()
result = pd.merge(result3, result4, on=['分类名称','销售日期'], how='inner')
result.to_excel("第二题第一问.xlsx")
