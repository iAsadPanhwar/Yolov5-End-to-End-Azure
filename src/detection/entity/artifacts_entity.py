from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_download_dir: str
    feature_store_path: str
    unzip_dir: str
