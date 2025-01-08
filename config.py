import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

SPEECH_SUBS_KEY = os.getenv("SPEECH_SUBS_KEY")
TRANSL_SUBS_KEY = os.getenv("TRANSL_SUBS_KEY")
REGION = os.getenv("REGION")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")