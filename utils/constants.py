"""
Python file to declare all constants used throughout the project
"""
import os

PROJECT_ROOT = os.environ["PYTHONPATH"]
CONFIG_FOLDER_NAME = "config"
QUERY_CONFIG_NAME = "query_config.json"

CONFIG_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, CONFIG_FOLDER_NAME))
QUERY_CONFIG_FILE = os.path.abspath(os.path.join(CONFIG_PATH, QUERY_CONFIG_NAME))
