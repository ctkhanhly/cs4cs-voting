import os
import csv 

from flask import Flask, render_template, session, request
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import DataError

DATABASE_URL = 'postgresql://lycao:1999@localhost/cs4cs'
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    print("Going home")
    return render_template("index.html", title="HOME")

@app.route('/vote', methods=['POST', 'GET'])
def vote():
    # net_id = session.get('net_id', None)
    links = db.execute("SELECT github_id,link FROM webs").fetchall()
    print(links)
    if request.method == 'POST':
        net_id = request.form.get("net_id")
        if net_id == None:
            render_template("error.html", title="ERROR PAGE", message= "Enter your Net Id, please ^^")
        try:
            voted = db.execute("SELECT voted FROM vote WHERE net_id = :net_id", {"net_id": net_id}).fetchone()
            # print(voted[0])
        except DataError:
            voted = None
    if voted is None:
        return render_template("error.html", title="ERROR PAGE", 
        message= "Your Net Id is Wrong")
    elif not voted[0]:
        db.execute("UPDATE vote SET voted = True WHERE net_id = :net_id", {"net_id": net_id})
        db.commit()
        return render_template("vote.html", title="GO VOTE", links=links)
    else:
        return render_template("error.html", title="ERROR PAGE", 
        message= "You aldready voted lahhh.  DON\'T CHEAT")
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        for chosen_link in request.form:
            if chosen_link:
                github_id = request.form.get("name")
                print("github_id", github_id)
                # votes = db.execute("SELECT num_of_votes FROM webs WHERE github_id = :github_id", {"github_id": github_id}).fetchone()
                db.execute("UPDATE webs SET num_of_votes = num_of_votes + 1 WHERE github_id = :github_id", {"github_id": github_id})
                db.commit()
    return render_template("result.html")

if __name__ == "__main__":
    app.run('127.0.0.1',debug=True)



