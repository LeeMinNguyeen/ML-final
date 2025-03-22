import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import ffn

from DataObject import ForexData

import pandas as pd
import datetime as datetime

class TrendFollow:
    def __init__(self, data, start, end):

        self.data = data

        self.data['Time'] = pd.to_datetime(self.data['Time'])
        self.data.set_index('Time', inplace=True)
        self.data = self.data.loc[start:end]
        
        self.stock = self.data.copy()
        self.stock['Close'] = self.stock['Close'].shift(1)
        
    # Trade using a simple trend following strategy
    def trade(self, length = 10, money = 10000, slippage = 1, max_position = 1):
        
        self.length = length
        
        temp_dict = {}
        temp_dict2 = {}
        # If window length is 0, algorithm doesn't make sense, so exit
        if length == 0:
            return 0

        # Compute rolling mean and rolling standard deviation
        rolling_window = self.stock['Close'].rolling(window=length)
        mu = rolling_window.mean()
        print(mu)
        std = rolling_window.std()

        # Compute the z-scores for each day using the historical data up to that day
        zscores = (self.stock['Close'] - mu) / std

        position_count = 0
        action = ""

        for i, row in enumerate(self.stock.itertuples(), 0):

            # Sell short if the z-score is > 1
            print(f"position_count: {position_count}")
            if zscores.iloc[i] > 1 and position_count < max_position:
                money -= self.stock['Open'][i] * (1 / slippage)
                print(f"sell : {self.stock['Open'][i]}, money: {money}")
                position_count += 1
                action = "sell"
            # Buy long if the z-score is < 1
            elif zscores.iloc[i] < -1 and position_count > max_position * -1:
                money += self.stock['Open'][i] * slippage
                print(f"buy  : {self.stock['Open'][i]}, money: {money}")
                position_count -= 1
                action = "buy"
            # Clear positions if the z-score between -.5 and .5
            elif abs(zscores.iloc[i]) < 0.5:
                if position_count > 0:
                    money += position_count * self.stock['Open'][i] * slippage
                elif position_count < 0:
                    money += position_count * self.stock['Open'][i] * (1 / slippage)
                print(f"clear: {self.stock['Open'][i]}, money: {money}")
                position_count = 0
                action = "clear"
            else:
                action = "hold"
            
            # Fill dictionary with the trading results.
            temp_dict[self.stock.index[i]] = [
                self.stock['Open'][i], self.stock['Close'][i], mu.iloc[i], std.iloc[i], zscores.iloc[i],
                money, position_count, self.stock['Open'][i] * (1 / slippage), self.stock['Open'][i] * slippage, action
                ]
            
            temp_dict2[self.stock.index[i]] = [
                self.stock['Open'][i], self.stock['Close'][i], mu.iloc[i], std.iloc[i], zscores.iloc[i],
                money, position_count, self.stock['Open'][i] * (1 / slippage), self.stock['Open'][i] * slippage
                ]
        
        # Create a dataframe to return for use in calculating and charting the trading results
        self.pr = pd.DataFrame(data=temp_dict).T
        self.pr.index.name = 'Date'
        self.pr.index = pd.to_datetime(self.pr.index)
        self.pr.columns = ['Open', 'Close', 'mu', 'std', 'zscores', 'money', 'position_count', 'buy_slippage', 'sell_slippage', 'Action']
        self.pr['equity'] = self.pr.money + (self.pr.Open * self.pr.position_count)

        self.pr2 = pd.DataFrame(data=temp_dict2).T
        self.pr2.index.name = 'Date'
        self.pr2.index = pd.to_datetime(self.pr2.index)
        self.pr2.columns = ['Open', 'Close', 'mu', 'std', 'zscores', 'money', 'position_count', 'buy_slippage', 'sell_slippage']
        self.pr2['equity'] = self.pr2.money + (self.pr2.Open * self.pr2.position_count)
        
        return self.pr
        
    def CalculateStats(self):
        series = self.pr2[['equity']].copy()
        series = series[self.length:-1]
        stats = series.calc_stats()
        stats = stats.to_csv(sep = ",")
        return stats
        
if __name__ == "__main__":
    data = ForexData(currency_pair = "USD/JPY", grainularity = "H4").GetData()
    backtest = TrendFollow(data, "2024-01-01", "2025-03-17")
    profit = backtest.trade(length=60, money=10000, slippage=1, max_position=10)
    result = backtest.CalculateStats()
    print(result)