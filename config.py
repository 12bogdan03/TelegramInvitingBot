import os
import logging
from decouple import config, Csv


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = config('DATABASE_URI')
TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
TELEGRAM_API_ID = config('TELEGRAM_API_ID', cast=int)
TELEGRAM_API_HASH = config('TELEGRAM_API_HASH')
TELETHON_SESSIONS_DIR = os.path.join(BASEDIR, 'telethon_sessions')
GETSMSCODE_USERNAME = config('GETSMSCODE_USERNAME')
GETSMSCODE_TOKEN = config('GETSMSCODE_TOKEN')
ADMIN_IDS = config('ADMIN_IDS', cast=Csv(int))
