from connect_database import connector
import pandas as pd
import mplfinance as mpf
        
class ForexData:
    def __init__(self, currency_pair, grainularity):
        self.db = connector()
        self.db.connects()
        
        self.currency_pair = currency_pair
        self.grainularity = grainularity
        
        self.collection_name = self.currency_pair.replace("/", "") + "_" + self.grainularity
    
    def __storecache(self, df):
        file = "backend/data/cache/" + self.collection_name + ".csv"
        df.to_csv(file)
        
    def __loaddata(self):
        collection = self.db.db[self.collection_name]
        self.data = collection.find()
        
        self.df = pd.DataFrame(list(self.data))
        self.__storecache(self.df)
        return self.df
    
    def GetData(self):
        try:
            self.df = pd.read_csv(f"backend/data/cache/{self.collection_name}.csv")
            print(f"load: {self.collection_name}")
        except:
            self.__loaddata()
        finally:
            return self.df

    def CandlePlot(self, startdate, enddate):
        self.df['Time'] = pd.to_datetime(self.df['Time'])
        self.df.set_index('Time', inplace=True)
        
        self.df = self.df.loc[startdate:enddate]
        
        fig, ax = mpf.plot(self.df, type='candle', style='charles', title=self.currency_pair + " " + self.grainularity, returnfig=True, volume = True)
        return fig
        
if __name__ == "__main__":
    data = ForexData(currency_pair = "EUR/USD", grainularity = "H4")
    df = data.GetData()
    data.CandlePlot(startdate = "2024-04-01", enddate = "2024-04-02")