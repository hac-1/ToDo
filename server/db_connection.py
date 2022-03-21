from pymongo import MongoClient
class dbConnect:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.database = self.client.to_do
        self.collection = self.database.todo
    
    def insert(self,data):
        print(data)
        self.collection.insert_one(data)
    
    def delete(self,data):
        print(data["task"])
        print(self.collection.delete_one(data["task"]))
    
    def read(self):
        values=self.collection.find({},{"_id":0})
        l=[]
        for i in values:
            l.append(i)
        return (l)