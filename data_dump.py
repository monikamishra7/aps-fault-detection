import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
# Database Name
dataBase = "aps"

# Collection  Name
collection = "sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")


#convert record to json so we can dump this record to mongo db
df.reset_index(drop = True ,inplace = True)
json_record=list(json.loads(df.T.to_json()).values())
print(json_record[0])
 
 #insert convert json into mongodb
client[dataBase][collection].insert_many(json_record)

