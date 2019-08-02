import os
import csv 
import sys

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#add path of config folder to the paths python looking for
print(os.path.dirname(__file__))
config_dir =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/'
print(config_dir)
sys.path.append(config_dir) 
print(sys.path)

#set up FLASK_ENV env variable
os.environ["FLASK_ENV"] = "development"

import config
print(dir(config))

#get DATABASE_URL defined in config folder
DATABASE_URL = config.DATABASE_URL
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))
db.execute("CREATE TABLE IF NOT EXISTS vote(id SERIAL PRIMARY KEY NOT NULL, net_id VARCHAR NOT NULL,\
voted BOOLEAN NOT NULL)")  


#insert values into the table
with open("net_ids.csv") as f:
    net_ids = csv.reader(f)
    for net_id in net_ids:
        db.execute("INSERT INTO vote(net_id, voted) VALUES \
(:net_id, :voted)",
{"net_id": net_id[0], "voted": False})
    db.commit()
# Read
result_set = db.execute("SELECT * FROM vote")  
for r in result_set:  
    print(r)


