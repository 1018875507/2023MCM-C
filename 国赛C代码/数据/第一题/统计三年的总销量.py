"""统计三年品类的总销量"""
df3 = pd.read_csv(r'D:\PycharmProjects\工具包\国赛C\合并.csv')
result =df3.groupby('分类名称')['销量(千克)'].sum().reset_index()
result.to_csv('三年品类总销量.csv')