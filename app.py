import os
# from config.config import Config
import config.config
import sys, os.path


from flask import Flask, render_template, session, request
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import DataError

config_dir = (os.path.abspath(os.path.dirname(__file__) + '/config/'))
sys.path.append(config_dir) 

DATABASE_URL = config.config.DATABASE_URL
print(DATABASE_URL)
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
    #print(links)
    voted = None
    if request.method == 'POST':
        net_id = request.form.get("net_id")
        session["net_id"] = net_id
        #if they did not enter net_id
        if net_id == None:
            render_template("error.html", title="ERROR PAGE", message= "Enter your Net Id, please ^^")
        #make sure the net_id is valid
        try:
            voted = db.execute("SELECT voted FROM vote WHERE net_id = :net_id", {"net_id": net_id.strip().lower()}).fetchone()
        except DataError:
            voted = None
    #voted is None when net_id is invalid
    #if the student has not voted, set the student's vote state to true 
    if voted is None:
        return render_template("error.html", title="ERROR PAGE", 
        message= "Your Net Id is Wrong")
    elif not voted[0]:
        return render_template("vote.html", title="GO VOTE", links=links)
    else:
        return render_template("error.html", title="ERROR PAGE", 
        message= "You aldready voted lahhh.  DON\'T CHEAT")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        #get all checked github_id
        #print(len(request.form))
        for github_id in request.form:
            #print(github_id.checked)
            print("github_id", github_id)
            # num_of_votes = db.execute("SELECT num_of_votes FROM webs WHERE  github_id = :github_id", {"github_id": github_id.lower()}).fetchone()[0]
            # num_of_votes +=1
            # print(num_of_votes)
            # db.execute("UPDATE webs SET num_of_votes = :num_of_votes WHERE github_id = :github_id", {"num_of_votes": num_of_votes+1, "github_id": github_id.lower()})
            db.execute("UPDATE webs SET num_of_votes = num_of_votes + 1 WHERE github_id = :github_id", {"github_id": github_id.strip().lower()})
            db.commit()
    net_id = session['net_id']
    db.execute("UPDATE vote SET voted = True WHERE net_id = :net_id", {"net_id": net_id})
    db.commit()
    return render_template("result.html")

if __name__ == "__main__":
    app.run('127.0.0.1',debug=True)



