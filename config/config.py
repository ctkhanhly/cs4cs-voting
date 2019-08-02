# from dotenv import load_dotenv
import os
import json

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)


DATABASE_URL =""
if os.getenv("FLASK_ENV") == "development":
    path_config_json = os.path.dirname(os.path.abspath(__file__)) + '/config.json'
    with open(path_config_json) as f:
        config_json = json.load(f)
        f.close()
    DATABASE_URL = config_json["development"]["DATABASE_URL"]
    #DATABASE_URL = os.getenv("DATABASE_URL")
else:
    #DATABASE_URL = config_json["production"]["DATABASE_URL"]
    DATABASE_URL = os.getenv("DATABASE_URL")