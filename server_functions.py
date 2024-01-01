import logging
from pathlib import Path

import server_properties
import shutil


# Checks for valid file extensions
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


# Removes previously created directories, and re-creates them for the current instance
def create_directories():
    # Delete (if exists) previous directories to start over
    shutil.rmtree(server_properties.images_to_segment_directory_path, ignore_errors=True)
    shutil.rmtree(server_properties.images_after_segment_directory_path, ignore_errors=True)
    shutil.rmtree(server_properties.segmented_images_archive_path, ignore_errors=True)

    # Create directory for images before segmentation
    Path(server_properties.images_to_segment_directory_path).mkdir(parents=True, exist_ok=True)

    # Create directory for images after segmentation
    Path(server_properties.images_after_segment_directory_path).mkdir(parents=True, exist_ok=True)

    # Create directory for archives
    Path(server_properties.segmented_images_archive_path).mkdir(parents=True, exist_ok=True)


# Creates and sets up a new logger with handler
def setup_server_logger() -> logging.Logger:
    # Create the logger
    new_logger = logging.getLogger('server-logger')
    new_logger.setLevel(logging.DEBUG)

    # Configure logging handlers
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Set a logging formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    new_logger.addHandler(handler)

    # Adjust the logging level of the Werkzeug server
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    return new_logger


def setup_request_logger() -> logging.Logger:
    # Create the logger
    new_logger = logging.getLogger('request-logger')
    new_logger.setLevel(logging.INFO)

    # Configure logging handlers
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # Set a logging formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - Received request: %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    new_logger.addHandler(handler)

    return new_logger
