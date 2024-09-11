import pandas as pd
import numpy as np
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import custom_exception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    
    
class data_ingestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    
    def intiate_data_ingestion(self):
        logging.info("Data ingestion started")
        
        try:
            data=pd.read_csv(os.path.join("notebooks/data","Gemstone.csv"))
            logging.info("Csv file read as df")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data saved")
            
            
            logging.info("spliting the data")
            Train_data,Test_data=train_test_split(data,test_size=0.25)
            logging.info("data spliting completed")
            
            Train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            Test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            
            
        except Exception as e:
            raise custom_exception(e,sys)