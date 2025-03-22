from DataObject import ForexData

import pandas as pd
import datetime as datetime
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error, r2_score, mean_squared_error
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
    def create_sequences(self, data, seq_length = 100):
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

        self.model = Sequential([
            LSTM(100, return_sequences=True, input_shape=(seq_length, 1)),
            LSTM(100, return_sequences=False),
            Dense(50),
            Dense(1)
        ])
        
        # Biên dịch mô hình
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        
        # Huấn luyện mô hình
        self.model.fit(X_train, y_train, epochs=100, batch_size=10, validation_data=(X_test, y_test), verbose=2)
        
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
        
        # Predict existing and future values
        last_sequence = self.close_price[-50:]  # Use the last 50 closing prices as the initial sequence
        all_predictions = []
        for i in range(len(self.close_price) + x_time):
            last_sequence_scaled = self.scaler.transform(last_sequence.reshape(-1, 1))
            prediction = self.model.predict(last_sequence_scaled.reshape(1, 50, 1))
            prediction = self.scaler.inverse_transform(prediction)
            all_predictions.append(prediction[0, 0])
            last_sequence = np.append(last_sequence[1:], prediction)
            if i < len(self.close_price) - 1:
                last_sequence[-1] = self.close_price[i + 1]
        
        future_dates = pd.date_range(start=self.data.index[-1], periods=x_time + 1)
        
        self.future_df = pd.DataFrame({
            'date': self.data.index.to_list() + future_dates[1:].to_list(),
            'actual_data': np.append(self.real_price.flatten(), [np.nan] * x_time),
            'lstm_predicted_data': all_predictions
        })
        
    def ExportResult(self):
        self.future_df.to_csv(f"{self.folder}result/predicted_results.csv", index=False)
        
    def ModelEvaluate(self):
        # Evaluate the model on the test set
        seq_length = 50
        X, y = self.create_sequences(self.close_price, seq_length)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Inverse transform the predictions and actual values
        y_test_inv = self.scaler.inverse_transform(y_test)
        y_pred_inv = self.scaler.inverse_transform(y_pred)

        # Calculate evaluation metrics
        mape = mean_absolute_percentage_error(y_test_inv, y_pred_inv) * 100
        mae = mean_absolute_error(y_test_inv, y_pred_inv)
        r2 = r2_score(y_test_inv, y_pred_inv)
        rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))

        print(f"MAPE: {mape:2f}%")
        print(f"MAE: {mae:4f}")
        print(f"R2: {r2:4f}")
        print(f"RMSE: {rmse:4f}")

if __name__ == "__main__":
    data = ForexData(currency_pair = "EUR/USD", grainularity = "D1")
    
    df = data.GetData()
    lstm = LSTM_model(data = df, start = "2004-05-05", end = "2025-03-19")
    lstm.Train()
    
    print("Model Evaluation:\n")
    lstm.ModelEvaluate()
    
    '''
    df = data.GetData()
    lstm2 = LSTM_model(data = df, start = "2024-01-01", end = "2025-1-31")
    lstm2.GetModel("LSTM")
    fig = lstm2.Predict()
    fig = lstm2.DrawResultGraph()
    lstm2.ExportResult()
    plt.show()
    '''