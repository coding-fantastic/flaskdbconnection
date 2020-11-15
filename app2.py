from flask import  Flask  , render_template , request 

from flask_mysqldb import MySQL 
from dbconnect import connection 

app = Flask(__name__)

@app.route('/register/', methods=["GET","POST"])
def register_page():
    try:
        c, conn = connection()
        return("okay")
    except Exception as e:
        return(str(e))


app.run()