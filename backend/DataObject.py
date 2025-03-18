from connect_database import connector
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

class MongoDatabase(connector):
    def __init__(self):
        super().__init__()
        self.connects()
        
    def disconnect(self):
        self.connector.client.close()
        
class ForexData:
    def __init__(self, currency_pair, grainularity):
        self.db = MongoDatabase()
        self.currency_pair = currency_pair
        self.grainularity = grainularity
        self.collection_name = self.currency_pair.replace("/", "") + "_" + self.grainularity
        
    def GetData(self):
        print(f"load: {self.collection_name}")
        collection = self.db.db[self.collection_name]
        self.data = collection.find()
        
        self.df = pd.DataFrame(list(self.data))

    def CandlePlot(self, startdate, enddate):
        self.df = self.df.set_index("Time")
        self.df.index = pd.to_datetime(self.df.index, unit='s') # update unit = to be dynamic
        self.df = self.df.loc[startdate:enddate]
        
        mpf.plot(self.df, type='candle', style='charles', volume=True, ylabel='Price', ylabel_lower='Volume', figratio=(12, 6), figscale=1.5)
        plt.show()
        
if __name__ == "__main__":
    data = ForexData(currency_pair = "EUR/USD", grainularity = "S1")
    df = data.GetData()
    data.CandlePlot(startdate = "2024-04-01", enddate = "2024-04-02")