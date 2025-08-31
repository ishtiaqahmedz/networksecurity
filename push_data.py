import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where() #ca; certificate authority

import pandas as pd
import numpy as np 
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_converter(self,file_path):
        try:
            
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            #we will convert our data into Json format so we can push it in MongoDB
            
            records =list(json.loads(data.T.to_json()).values())    #start reading from inner most to the out bracket to understand 
            return records                                          #the conversion: converts a Pandas DataFrame → JSON string → 
                                                                    #Python dict → list of row dictionaries, making it ready for 
                                                                    # MongoDB insertion.
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database_name,collection_name):
        try:
            print("Now inserting data in MongoDB Database:",database_name)
            
            self.database=database_name #stores the database object (not a string)
            self.collection=collection_name #store network data
            self.records=records
            
            #self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
          
            #self.collection=self.database[self.collection] #will become collection=database["networkdata"]
            #self.collection.insert_many(self.records)


            #other way:
            print("Connecting to MongoDB Atlas:", MONGO_DB_URL)
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=certifi.where())
            #Creates a connection object to MongoDB using your connection string (MONGO_DB_URL).
            # Now you can use self.mongo_client["mydb"] to access a database.


            db = self.mongo_client[database_name]   # this will always ensure this is a DB object
            collection = db[collection_name]        # this will always ensure this is a Collection object
            collection.insert_many(records)
            return len(records)


        except Exception as e:
            raise NetworkSecurityException(e,sys)
        


if __name__ =="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATA_BASE_NAME="NetworkDatabase"
    COLLECTION_NAME="NetworkData"
    network_obj=NetworkDataExtract()

    records= network_obj.cv_to_json_converter(FILE_PATH)
    #print(records)
    no_of_records=network_obj.insert_data_mongodb(records,DATA_BASE_NAME,COLLECTION_NAME)
    print(no_of_records, " have been inserted in the database")

