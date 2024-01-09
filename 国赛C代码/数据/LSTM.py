import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df =pd.read_excel(r'D:\PycharmProjects\工具包\国赛C\茄类2.xlsx')



# 准备训练数据和目标
X = df['销量(千克)'].values.tolist()

y = list(range(1, 1051))
X= np.array(X).reshape(len(X), 1, 1)
y = np.array(y)




# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建LSTM模型
model = Sequential()
model.add(LSTM(100, input_shape=(1, 1)))  # 50个LSTM单元
model.add(Dense(1))  # 输出层，输出一个值

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(X_train, y_train, epochs=100, batch_size=1)

# 使用模型进行预测
predicted_values = model.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, predicted_values)

# 打印均方误差作为评价指标
print("均方误差 (MSE):", mse)
