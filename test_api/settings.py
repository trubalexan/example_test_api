import os
from dotenv import load_dotenv

load_dotenv()

# BASE_URL = "http://localhost:8000"
# загрузка базового адреса страницы тестирования и дополнения для страницы документации
BASE_URL = os.getenv('BASE_URL')
DOCS_URL_EXTENSION_v2 = os.getenv('DOCS_URL_v2')
SCHEMA_URL_v2 = os.getenv('SCHEMA_URL_v2')

DOCS_URL_EXTENSION_v3 = os.getenv('DOCS_URL_v3')
SCHEMA_URL_v3 = os.getenv('SCHEMA_URL_V3')





