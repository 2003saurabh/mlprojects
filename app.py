from src.mlprojects.logger import logging
from src.mlprojects.exception import CustomException
from src.mlprojects.components.data_ingestion import DataIngestion
from src.mlprojects.components.data_ingestion import DataIngestionConfig
from src.mlprojects.components.data_transformation import DataTransformationConfig,DataTransformation 
from src.mlprojects.components.model_trainer import ModelTrainerConfig,ModelTrainer

import sys

if __name__ == '__main__':
    logging.info("Starting data ingestion process")
    try:
       # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()


        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        #model_trainer_config=ModelTrainerConfig()
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)
      
