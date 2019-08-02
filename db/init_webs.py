import os
import csv 
import sys


from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

config_dir =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/'
sys.path.append(config_dir) 
os.environ["FLASK_ENV"] = "development"
import config


DATABASE_URL = config.DATABASE_URL
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))
# Create 
db.execute("CREATE TABLE IF NOT EXISTS webs(github_id VARCHAR PRIMARY KEY NOT NULL,\
 name VARCHAR, link VARCHAR NOT NULL, num_of_votes INTEGER NOT NULL)")  


with open("links.csv") as f:
    links = csv.reader(f)
    for github_id, name, link in links:
        db.execute("INSERT INTO webs (github_id, name, link, num_of_votes) VALUES \
(:github_id, :name, :link, :num_of_votes)",
{"github_id": github_id, "name": name, "link": link, "num_of_votes":0})
    db.commit()
# Read
result_set = db.execute("SELECT * FROM webs")  
for r in result_set:  
    print(r)
