import pandas as pd
df = pd.read_excel('D:\PycharmProjects\工具包\国赛C\食用菌1.xlsx')
df['损耗率(%)']= 1 - df['损耗率(%)']/100
df['损耗前的质量'] =df['销量(千克)']/df['损耗率(%)']
a = df['损耗前的质量'].sum()
b =df['销量(千克)'].sum()
print(1-b/a)
