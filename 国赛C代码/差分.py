import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt

# 创建一个示例时间序列数据
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# 将数据加载到Pandas DataFrame中
df = pd.DataFrame(data, columns=['Value'])

# 进行一阶差分（即当前值减去前一个值）
df['Differenced'] = df['Value'].diff()

# 删除第一个NaN值
df = df.dropna()

# 拟合ARIMA模型
model = ARIMA(df['Differenced'], order=(1, 0, 0))
model_fit = model.fit(disp=0)

# 预测未来值
n_forecast = 5
forecast, stderr, conf_int = model_fit.forecast(steps=n_forecast)

# 创建一个包含未来预测值的日期索引
future_dates = pd.date_range(start=df.index[-1], periods=n_forecast+1, closed='right')

# 创建一个包含差分值和预测值的新DataFrame
forecast_df = pd.DataFrame({'Differenced': forecast}, index=future_dates)

# 反差分以获得原始预测值
forecast_df['Value'] = df['Value'].iloc[-1] + forecast_df['Differenced'].cumsum()

# 打印预测值
print(forecast_df['Value'])

# 可视化原始数据和预测值
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='原始数据', marker='o')
plt.plot(forecast_df.index, forecast_df['Value'], label='预测值', linestyle='--', marker='o')
plt.xlabel('时间')
plt.ylabel('数值')
plt.legend()
plt.show()
