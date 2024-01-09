import pandas as pd
"""计算利润率"""
'''df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\每日批发价格汇总.xlsx')
df['利润'] = df['销量(千克)']*df['销售单价(元/千克)']-df['销量(千克)']*df['批发价格(元/千克)']
df['利润率'] = df['利润']/df['销量(千克)']/df['批发价格(元/千克)']
df1 = df.groupby(['销售日期','单品编码'])['销量(千克)'].sum().reset_index()
df2 = df.groupby(['销售日期','单品编码'])['利润率'].mean().reset_index()
result1 = pd.merge(df1, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel(r'利润率.xlsx')'''



'''条件茄类的销售情况'''
'''df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '茄类']
result.to_excel("茄类.xlsx")'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\茄类.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('茄类1.xlsx')'''

'''df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\茄类1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('茄类2.xlsx')'''

'''条件花叶类的销售情况'''
'''df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '花叶类']
result.to_excel("花叶类.xlsx")'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\花叶类.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('花叶类1.xlsx')'''

'''df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\花叶类1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('花叶类2.xlsx')'''

'''条件花菜类的销售情况'''
'''df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '花菜类']
result.to_excel("花菜类.xlsx")'''


'''df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\花菜类.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('花菜类1.xlsx')'''

'''
df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\花菜类1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('花菜类2.xlsx')
'''

'''水生根茎条件类的销售情况'''
'''
df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '水生根茎类']
result.to_excel("水生根茎类.xlsx")
'''
'''
df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\水生根茎类.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('水生根茎类1.xlsx')
'''

'''

df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\水生根茎类1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('水生根茎类2.xlsx')

'''
'''辣椒类的销售情况'''
'''df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '辣椒类']
result.to_excel("辣椒类.xlsx")'''

'''
df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\辣椒类.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('辣椒类1.xlsx')
'''

'''df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\辣椒类1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('辣椒类2.xlsx')'''

'''食用菌类的销售情况'''
'''df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result = df[df['分类名称'] == '食用菌']
result.to_excel("食用菌.xlsx")'''

'''
df = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\食用菌.xlsx')
df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df2['销售日期'] = pd.to_datetime(df2['销售日期'])
result = pd.merge(df, df1, on=['单品编码'], how='inner')
result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')
result1.to_excel('食用菌1.xlsx')'''

'''df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\食用菌1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['成本'] = df['销量(千克)']/df['损耗率(%)']*df['批发价格(元/千克)']
df['销售额'] = df['销量(千克)']*df['销售单价(元/千克)']
result = df.groupby(['销售日期'])['销量(千克)'].sum().reset_index()
result1 = df.groupby(['销售日期'])['销售额'].sum().reset_index()
result2 = df.groupby(['销售日期'])['成本'].sum().reset_index()
result3 = pd.merge(result1, result2, on=['销售日期'], how='inner')
result4 = pd.merge(result3, result, on=['销售日期'], how='inner')
result4['平均定价'] = result4['销售额']/result4['销量(千克)']
result4['利润'] = result4['销售额']-result4['成本']
result4.to_excel('食用菌2.xlsx')'''
