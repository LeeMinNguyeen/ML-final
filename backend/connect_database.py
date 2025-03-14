from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nguyenlm22416c:YcxgUk4K2Il3lNdB@cluster0.6immj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
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
            result = collection.find_one({"username": username, "password": password}, {"_id": 0, "username": 1, "email": 1, "password": 1})
            return result
        except Exception as e:
            print(e)
            return None
    
    def NewUser(self, username, email, password):
        collection = self.db["Users"]
        try:
            result = collection.insert_one({"username": username, "email": email, "password": password})
            return result
        except Exception as e:
            print(e)
            return None
        
    def createCollection(self, collection_name):
        try:
            self.db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created successfully.")
        except Exception as e:
            print(e)
        
    def ImportData(self, data = list, import_collection = str):
        collection = self.db[import_collection]
        try:
            result = collection.insert_many(data)
            return result
        except Exception as e:
            print(e)
            return None
        
if __name__ == "__main__":
    connector = connector()
    connector.connects()