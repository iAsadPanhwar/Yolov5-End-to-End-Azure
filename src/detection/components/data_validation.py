import os
import sys
import shutil
from src.detection.exception import AppException
from src.detection.logger import logging
from src.detection.entity.config_entity import DataValidationConfig
from src.detection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class DataValidation:
    def __init__(
        self,
        data_validation_config: DataValidationConfig,
        data_ingestion_artifact: DataIngestionArtifact,
    ):
        try:
            logging.info(f"{'>>' * 20}Data Validation log started.{'<<' * 20}")
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.validation_error_message = ""
        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            all_files = os.listdir(self.data_ingestion_artifact.data_download_dir)

            logging.info(f"{all_files} found in {self.data_ingestion_artifact.data_download_dir} directory")
            
            for required_file in self.data_validation_config.required_file_list:
                if required_file not in all_files:
                    validation_status = False
                    self.validation_error_message += f"{required_file} is not found in downloaded data directory.\n"
                    logging.error(f"{required_file} is not found in downloaded data directory.")

            os.makedirs(self.data_validation_config.valid_status_file_dir, exist_ok=True)
            status_file_path = os.path.join(self.data_validation_config.valid_status_file_dir, "status.txt")

            with open(status_file_path, "w") as f:
                f.write(f"Validation status: {validation_status}")
                if not validation_status:
                    f.write(f"\n{self.validation_error_message}")

            return validation_status
        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class")

        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            # if status:
            #     shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)
