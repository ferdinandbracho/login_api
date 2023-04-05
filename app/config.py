import os
from pathlib import Path

from dotenv import load_dotenv

# Config env variable
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# Project
PROJECT_NAME = os.getenv('PROJECT_NAME')

# Database
DATABASE_URL = os.getenv('DATABASE_URL')
