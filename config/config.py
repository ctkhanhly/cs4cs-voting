# from dotenv import load_dotenv
import os
import json

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

path_config_json = os.path.dirname(os.path.abspath(__file__)) + '/config.json'
DATABASE_URL =""
with open(path_config_json) as f:
    config_json = json.load(f)
    f.close()
if os.getenv("FLASK_ENV") == "development":
    DATABASE_URL = config_json["development"]["DATABASE_URL"]
else:
    #DATABASE_URL = config_json["production"]["DATABASE_URL"]
    DATABASE_URL = os.getenv("DATABASE_URL")