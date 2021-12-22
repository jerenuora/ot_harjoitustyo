import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DB_FILE = os.getenv("DB_FILE") or "scores.db"
DB_FILE_PATH = os.path.join(
    dirname,  "assets", DB_FILE)

JSON_FILE = os.getenv("JSON_FILE") or "shapefile_directions.json"
JSON_FILE_PATH = os.path.join(dirname, "assets",
                           "JSON_FILE")
