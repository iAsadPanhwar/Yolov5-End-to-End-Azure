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
    
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    
    data_download_url: str = DATA_DOWNLOAD_URL
    