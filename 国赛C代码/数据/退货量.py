import pandas as pd
'''df = pd.read_csv('D:\PycharmProjects\工具包\国赛C\合并.csv')
df1 = df[df['销售类型'] == '退货']
df1.to_excel(r'退货.xlsx')'''

df = pd.read_excel('D:\PycharmProjects\工具包\国赛C\数据\退货.xlsx')
df['销售日期'] = pd.to_datetime(df['销售日期'])
df['Year'] = df['销售日期'].dt.to_period('Y')
df1 = df.groupby(['Year','单品名称'])['销量(千克)'].sum().reset_index()
df1.to_excel(r'每年退货量.xlsx')



