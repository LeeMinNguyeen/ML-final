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

class LSTM_model:
    def __init__(self, data, start, end):
        self.StartDate = start
        self.EndDate = end
        self.data = data
        
        self.folder = "backend/model/"

        self.data['Time'] = pd.to_datetime(self.data['Time'])
        self.data.set_index('Time', inplace=True)
        self.data = self.data.loc[start:end]
                
        self.close_price = self.data['Close'].values.reshape(-1, 1)
        
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.scaler.fit_transform(self.close_price)
        
    def GetModel(self, model_name):
        self.model = tf.keras.models.load_model(f"{self.folder}{model_name}.h5")
    
    def SaveModel(self, model, model_name):
        model.save(f"{self.folder}{model_name}.h5")
    
    # Hàm tạo chuỗi thời gian cho LSTM
    def create_sequences(self, data, seq_length = 50):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)
    
    def Train(self):
        seq_length = 50  # Số điểm dữ liệu đầu vào
        X, y = self.create_sequences(self.close_price, seq_length)
        
        # Chia tập dữ liệu thành train và test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Xây dựng mô hình LSTM **KHÔNG CÓ DROPOUT**
        self.model = Sequential([
            LSTM(100, return_sequences=True, input_shape=(seq_length, 1)),
            LSTM(100, return_sequences=False),
            Dense(50),
            Dense(1)
        ])
        
        # Biên dịch mô hình
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        
        # Huấn luyện mô hình
        history = self.model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
        
        self.SaveModel(self.model, "LSTM")
        
    def DrawResultGraph(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.future_df['date'], self.future_df['actual_data'], label='Actual Data', color='b')
        plt.plot(self.future_df['date'], self.future_df['lstm_predicted_data'], label='LSTM Predicted Data', color='r')
        plt.title('EUR/USD Price Prediction')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        fig = plt.gcf()
        return fig
    
    def Predict(self):
        
        # Calculate the number of time steps to predict
        future_dates = pd.date_range(start=self.data.index[-1], end=self.EndDate, freq='D') 
        x_time = len(future_dates)
        
        self.real_price = self.scaler.inverse_transform(self.close_price)
        
        # Predict future values
        last_sequence = self.close_price[-50:]
        future_predictions = []
        for _ in range(x_time):
            last_sequence_scaled = self.scaler.transform(last_sequence.reshape(-1, 1))
            prediction = self.model.predict(last_sequence_scaled.reshape(1, 50, 1))
            prediction = self.scaler.inverse_transform(prediction)
            future_predictions.append(prediction[0, 0])
            last_sequence = np.append(last_sequence[1:], prediction)

        future_dates = pd.date_range(start=self.data.index[-1], periods=x_time + 1)

        # print(f"Predicted Prices Shape: {future_predictions.shape}, Real Prices Shape: {self.real_price.shape}")

        self.future_df = pd.DataFrame({
            'date': self.data.index.to_list() + future_dates[1:].to_list(),
            'actual_data': np.append(self.real_price.flatten(), [np.nan] * x_time),
            'lstm_predicted_data': np.append(self.real_price.flatten(), future_predictions)
        })
    
    def ExportResult(self):
        self.future_df.to_csv(f"{self.folder}result/predicted_results.csv", index=False)

if __name__ == "__main__":
    data = ForexData(currency_pair = "EUR/USD", grainularity = "H4")
    df = data.GetData()
    lstm = LSTM_model(data = df, start = "2025-03-01", end = "2025-04-01")
    # lstm.Train()
    lstm.GetModel("LSTM")
    lstm.Predict()