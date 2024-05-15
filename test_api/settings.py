import os
from dotenv import load_dotenv

load_dotenv()

# BASE_URL = "http://localhost:8000"
# загрузка базового адреса страницы тестирования и дополнения для страницы документации
BASE_URL = os.getenv('BASE_URL')
DOCS_URL_EXTENSION = os.getenv('DOCS_URL')
SCHEMA_URL = os.getenv('SCHEMA_URL')





