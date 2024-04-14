import os
from dotenv import load_dotenv

dotenv_path = '/weather/.env'
load_dotenv(dotenv_path)

api_key = os.getenv("API_KEY")
