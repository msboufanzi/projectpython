import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') # kanjibo env variable mn .env file 
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') # 
    SQLALCHEMY_TRACK_MODIFICATIONS = False # this remove the detection of changes in so we can improve performance