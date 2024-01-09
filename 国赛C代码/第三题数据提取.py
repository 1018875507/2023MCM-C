import pandas as pd
"""df =pd.read_csv('D:\PycharmProjects\工具包\国赛C\合并.csv')
# 将 '日期' 列转换为日期时间对象
df['销售日期'] = pd.to_datetime(df['销售日期'])

# 提取日期为2023年6月24日至30日的数据
start_date = pd.to_datetime('2023-06-24')
end_date = pd.to_datetime('2023-06-30')
filtered_data = df[(df['销售日期'] >= start_date) & (df['销售日期'] <= end_date)]
print(filtered_data['单品名称'].value_counts())
filtered_data.to_excel('日后的销售情况.xlsx')"""

'''df = pd.read_excel('D:\PycharmProjects\工具包\国赛C\日后的销售情况.xlsx')
df1 =df[df['分类名称'] == '食用菌']
df1.to_excel('食用菌24日.xlsx')'''
'''df= pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df1 =pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
# 提取日期为2023年6月24日至30日的数据
start_date = pd.to_datetime('2023-06-24')
end_date = pd.to_datetime('2023-06-30')
filtered_data = df[(df['销售日期'] >= start_date) & (df['销售日期'] <= end_date)]
result = pd.merge(filtered_data,df1,on='单品编码',how='inner')
print(result)'''

'''统计销售量大于2.5的单品'''
'''df = pd.read_excel('D:\PycharmProjects\工具包\国赛C\日后的销售情况.xlsx')
result = df.groupby(['单品名称','销售日期'])['销量(千克)'].sum().reset_index()
result[result['销量(千克)'] >=2.5]['单品名称'].value_counts().to_excel('大于2.5的天数.xlsx')'''

'''df = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件1.xlsx')
df1 =pd.read_excel('D:\PycharmProjects\工具包\国赛C\大于2.5的天数.xlsx')
result = pd.merge(df1,df,on='单品名称',how='inner')
result.to_excel('大于2.5的天数1.xlsx')'''

'''计算获取评价指标数据'''
'''df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\日后的销售情况.xlsx')
df4 =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df1 = df.groupby(['单品名称'])['销量(千克)'].sum().reset_index()
df2 = df.groupby(['单品名称'])['是否打折销售'].sum().reset_index()
df3 = df.groupby(['单品名称'])['销售单价(元/千克)'].mean().reset_index()
result = pd.merge(df1,df4,on='单品名称',how='inner')
result1 = pd.merge(result,df2,on='单品名称',how='inner')
result1 = pd.merge(result1,df3,on='单品名称',how='inner')
result1.to_excel('评价数据.xlsx')'''

'''计算统计27个单品的销售情况'''
'''df5 = pd.read_csv(r'D:\浏览器下载\优劣解距离法计算结果.csv')
list1 = df5['索引'].to_list()
for i in range(0,27):

    f=list1[i]
    print(f)
    df = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')

    df1 = pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
    df2 = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\附件3.xlsx')
    df['销售日期'] = pd.to_datetime(df['销售日期'])
    df2['销售日期'] = pd.to_datetime(df2['销售日期'])
    result = pd.merge(df, df1, on=['单品编码'], how='inner')
    result1 = pd.merge(result, df2, on=['单品编码','销售日期'], how='inner')

    result1['损耗率(%)']= 1 - result1['损耗率(%)']/100
    result1['成本'] = result1['销量(千克)']/result1['损耗率(%)']*result1['批发价格(元/千克)']
    result1['销售额'] = result1['销量(千克)']*result1['销售单价(元/千克)']


    a = result1.groupby(['销售日期','单品名称_x'])['销量(千克)'].sum().reset_index()
    print(a)
    b = result1.groupby(['销售日期','单品名称_x'])['销售额'].sum().reset_index()
    print(b)
    c = result1.groupby(['销售日期','单品名称_x'])['成本'].sum().reset_index()
    print(c)

    result3 = pd.merge(a, b, on=['销售日期','单品名称_x'], how='inner')
    result4 = pd.merge(result3, c, on=['销售日期','单品名称_x'], how='inner')
    result4['平均定价'] = result4['销售额']/result4['销量(千克)']
    result4['利润'] = result4['销售额']-result4['成本']
    result4[result4['单品名称_x']=='{}'.format(f)].to_excel('D:\PycharmProjects\工具包\国赛C\数据\拟合\{}.xlsx'.format(f))
    print(i)
    '''

'''df = pd.read_csv(r'D:\浏览器下载\优劣解距离法计算结果.csv')
df1 =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\损耗.xlsx')
df2 =pd.merge(df,df1,on='单品名称')
df2.to_excel('损耗率的.xlsx')'''






