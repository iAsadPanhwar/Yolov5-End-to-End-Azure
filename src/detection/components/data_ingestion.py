import os
import sys
import zipfile
from roboflow import Roboflow
from src.detection.logger import logging
from src.detection.exception import AppException
from src.detection.entity.config_entity import DataIngestionConfig
from src.detection.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.rf = Roboflow(api_key=self.data_ingestion_config.roboflow_api_key)
            self.project = self.rf.workspace(self.data_ingestion_config.workspace_name).project(self.data_ingestion_config.project_name)
            self.version = self.project.version(self.data_ingestion_config.version_number)
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self):
        """
        Fetch data from Roboflow
        """
        try:
            dataset = self.version.download(
                self.data_ingestion_config.model_format, 
                location=self.data_ingestion_config.data_download_dir
            )
            logging.info(f"Dataset downloaded successfully to: {self.data_ingestion_config.data_download_dir}")
            return self.data_ingestion_config.data_download_dir
        except Exception as e:
            error_message = f"Error occurred while downloading data from Roboflow: {str(e)}"
            logging.error(error_message)
            raise AppException(error_message, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiate the data ingestion process
        """
        try:
            download_dir = self.download_data()

            

            data_ingestion_artifact = DataIngestionArtifact(
                data_download_dir=download_dir
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys)


