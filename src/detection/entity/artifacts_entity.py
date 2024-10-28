from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    data_download_dir: str
    feature_store_file_path: str
    unzip_dir: str

@dataclass
class DataValidationArtifact:
    valid_status: bool
    