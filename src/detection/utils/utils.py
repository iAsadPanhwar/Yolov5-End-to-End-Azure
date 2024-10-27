import os.path
import sys
import yaml
import base64

from src.detection.exception import AppException
from src.detection.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns a dictionary.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
        logging.info(f"Successfully read YAML file: {file_path}")
        return content
    except Exception as e:
        error_message = f"Error occurred while reading YAML file: {file_path}"
        logging.error(error_message)
        raise AppException(error_message, sys) from e
    
def write_yaml_file(file_path: str, data: dict, replace: bool = False) -> None:
    """
    Writes a dictionary to a YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        with open(file_path, 'w') as yaml_file:
            yaml.safe_dump(data, yaml_file)
        logging.info(f"Successfully wrote data to YAML file: {file_path}")
    except Exception as e:
        error_message = f"Error occurred while writing data to YAML file: {file_path}"
        logging.error(error_message)
        raise AppException(error_message, sys) from e
    
def encode_image_into_base64(cropped_image_path: str) -> str:
    """
    Encodes an image into base64 format.
    """
    try:
        with open(cropped_image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        logging.info(f"Successfully encoded image: {cropped_image_path}")
        return encoded_image
    except Exception as e:
        error_message = f"Error occurred while encoding image: {cropped_image_path}"
        logging.error(error_message)
        raise AppException(error_message, sys) from e
    
def decode_base64_image(image_data: str, image_path: str) -> None:
    """
    Decodes a base64 image and saves it to a file.
    """
    try:
        with open(image_path, 'wb') as image_file:
            image_file.write(base64.b64decode(image_data))
        logging.info(f"Successfully decoded base64 image and saved it to: {image_path}")
    except Exception as e:
        error_message = f"Error occurred while decoding base64 image and saving it to: {image_path}"
        logging.error(error_message)
        raise AppException(error_message, sys) from e
    
    
