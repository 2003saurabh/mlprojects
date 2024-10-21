import os
import sys
from src.mlprojects.exception import CustomException
from src.mlprojects.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
port=os.getenv("port")
db=os.getenv('db')



def read_sql_data():
    logging.info("Reading SQL database started from utils")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            port=3307,
            password=password,
            database=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)
    
