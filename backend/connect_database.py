from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nguyenlm22416c:KoXrZzWniEiTc0Iy@cluster0.6immj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
class connector():
    def __init__(self):
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["ForexTrading"]
        
    def connects(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
            
    def login(self, username, password):
        collection = self.db["Users"]
        try:
            result = collection.find_one({"user":username, "password":password})
            return result
        except Exception as e:
            print(e)
            return None
        
if __name__ == "__main__":
    connector = connector()
    connector.connects()