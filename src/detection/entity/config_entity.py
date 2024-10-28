import os
from dataclasses import dataclass
from datetime import datetime
from src.detection.constants.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = ARTIFACTS_DIR

training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    # feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    # data_download_url: str = DATA_DOWNLOAD_URL

    # New attributes for Roboflow
    roboflow_api_key: str = "AaIJxHFVNAo0pcWWo3yS"
    workspace_name: str = "rice-leaf-uacyp"
    project_name: str = "riceleaf-4rg3g"
    version_number: int = 4
    model_format: str = "yolov5"

    # Directory to save the downloaded dataset
    data_download_dir: str = os.path.join(data_ingestion_dir, "downloaded_data")

    # # Directory to unzip the dataset if needed
    # unzip_dir: str = os.path.join(data_ingestion_dir, "unzipped_data")
    
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    
    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES