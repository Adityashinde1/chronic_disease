from urllib import request
from kidney_disease.entity.config_entity import DataIngestionConfig
import sys,os
from kidney_disease.exception import kidneyDiseaseException
from kidney_disease.logger import logging
from kidney_disease.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
from sklearn.model_selection import train_test_split
from six.moves import urllib
import numpy as np

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise kidneyDiseaseException(e,sys)
    

    def download_data(self,) -> str:
        try:
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            csv_download_dir = self.data_ingestion_config.csv_download_dir
            
            os.makedirs(csv_download_dir,exist_ok=True)

            kidneyDisease_file_name = os.path.basename(download_url)

            csv_file_path = os.path.join(csv_download_dir, kidneyDisease_file_name)

            logging.info(f"Downloading file from :[{download_url}] into :[{csv_file_path}]")
            
            urllib.request.urlretrieve(download_url, csv_file_path)
            logging.info(f"File :[{csv_file_path}] has been downloaded successfully.")
            return csv_file_path

        except Exception as e:
            raise kidneyDiseaseException(e,sys) from e

    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            csv_data_dir = self.data_ingestion_config.csv_download_dir

            file_name = os.listdir(csv_data_dir)[0]

            kidneyDisease_file_path = os.path.join(csv_data_dir,file_name)


            logging.info(f"Reading csv file: [{kidneyDisease_file_path}]")

            kidneyDisease_dataframe = pd.read_csv(kidneyDisease_file_path)

            # Replacing "?" to NaN value
            kidneyDisease_dataframe['pcv'] = kidneyDisease_dataframe['pcv'].replace("?", np.NaN)
            kidneyDisease_dataframe['wc'] = kidneyDisease_dataframe['wc'].replace("?", np.NaN)
            kidneyDisease_dataframe['rc'] = kidneyDisease_dataframe['rc'].replace("?", np.NaN)

            # Dropping id column
            kidneyDisease_dataframe = kidneyDisease_dataframe.drop('id',axis=1)

            # filling missing values for column - "rc", 'pcv', 'wc'
            rc_column_value = 5.1
            pcv_column_value = 27
            wc_column_value = 8500

            kidneyDisease_dataframe['rc'] = kidneyDisease_dataframe['rc'].fillna(value=rc_column_value)
            kidneyDisease_dataframe['pcv'] = kidneyDisease_dataframe['pcv'].fillna(value=pcv_column_value)
            kidneyDisease_dataframe['wc'] = kidneyDisease_dataframe['wc'].fillna(value=wc_column_value)

            # Chnaging the datatype of numerical columns
            kidneyDisease_dataframe = kidneyDisease_dataframe.astype({"rc": float, "pcv": int, "wc": int})

            logging.info(f"Splitting data into train and test")

            # Train test split
            train_set, test_set = train_test_split(kidneyDisease_dataframe, test_size=0.2)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)

            if train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                train_set.to_csv(train_file_path,index=False)

            if test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                test_set.to_csv(test_file_path,index=False)            


            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise kidneyDiseaseException(e,sys) from e


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            csv_file_path =  self.download_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise kidneyDiseaseException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")
