from DataObject import ForexData

import pandas as pd
import datetime as datetime
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class LSTM:
    def __init__(self, data, start, end):
        self.folder = "backend/model/"
        
        self.data = data

        self.data['Time'] = pd.to_datetime(self.data['Time'])
        self.data.set_index('Time', inplace=True)
        self.data = self.data.loc[start:end]
    
    def GetModel(self, model_name):
        self.model = tf.keras.models.load_model(f"{self.folder}{model_name}.h5")
    
    def SaveModel(self, model_name):
        self.model.save(f"{self.folder}{model_name}.h5")
    
    def Train(self):
        # Chọn giá đóng cửa làm biến dự đoán
        close_prices = self.data['Close'].values.reshape(-1, 1)
        
        # Chuẩn hóa dữ liệu về khoảng [0, 1]
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(close_prices)
        
        # Hàm tạo chuỗi thời gian cho LSTM
        def create_sequences(data, seq_length):
            X, y = [], []
            for i in range(len(data) - seq_length):
                X.append(data[i:i+seq_length])
                y.append(data[i+seq_length])
            return np.array(X), np.array(y)

        seq_length = 50  # Số điểm dữ liệu đầu vào
        X, y = create_sequences(scaled_data, seq_length)
        
        # Chia tập dữ liệu thành train và test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Xây dựng mô hình LSTM **KHÔNG CÓ DROPOUT**
        model = Sequential([
            LSTM(100, return_sequences=True, input_shape=(seq_length, 1)),
            LSTM(100, return_sequences=False),
            Dense(50),
            Dense(1)
        ])
        
        # Biên dịch mô hình
        model.compile(optimizer='adam', loss='mean_squared_error')
        
        # Huấn luyện mô hình
        history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
        
    def DrawResultGraph(self):
        pass
    
    def Predict(self):
        pass

if __name__ == "__main__":
    data = ForexData(currency_pair = "EUR/USD", grainularity = "H4")
        
    