from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    # data_zip_file_path: str
    data_download_dir: str
    # feature_store_file_path: str
    # unzip_dir: str
    # downloaded_data: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
