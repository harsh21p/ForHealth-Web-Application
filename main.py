
#DEPENDENCIES

from os import name
from flask import Flask, render_template,request,redirect,session,url_for,current_app
import MySQLdb 
from flask_mysqldb import MySQL
from flask import Flask, render_template, request
import sqlite3
#FLASK APP 

app=Flask(__name__)

app.secret_key="ebcqaeyzfqtgtai"

#DATABASE CONFIG

# app.config["MYSQL_HOST"]="localhost"
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="root"
# app.config["MYSQL_DB"]="data"  
# db=MySQL(app)

db=sqlite3.connect("auth.db",check_same_thread=False)
db.row_factory = sqlite3.Row
cursor=db.cursor()

#Home

@app.route('/',methods=['GET','POST'])

def myhome():
    return render_template("home.html")

#LOGIN

@app.route('/login.html',methods=['GET','POST'])

def index():
    session['username'] = ""
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username=request.form['username']
            password=request.form['password']
            session['username'] = username
            session['username1'] = username
            #cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM info1 WHERE name_user=(?) AND password_user=(?)",(username,password))
            
        info=cursor.fetchone()
        
        if info is not None:
            session["email"]=info['email_user']
            if info['name_user'] == username and info['password_user'] == password:
                return redirect(url_for("successful"))
        else:
             return render_template("index.html",message1="Password or username didn't match")
    return render_template("index.html")

#SIGNUP

@app.route('/signup.html',methods=['GET','POST'])

def register():
    if request.method == 'POST':

        if 'username' in request.form and 'password' in request.form and 'email' in request.form and 'phone' in request.form and 'password1' in request.form and 'address' in request.form:

            username=request.form['username']
            password1=request.form['password1']
            password=request.form['password']
            email=request.form['email']
            phone=request.form['phone']
            address=request.form['address']
            if password==password1:
                # cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("INSERT INTO info1(name_user,password_user,email_user,phone_user,address_user) VALUES((?),(?),(?),(?),(?))",(username,password1,email,phone,address))
                db.commit()
                return redirect(url_for("index"))
            else:
                return render_template("signup.html",message="Password didn't match")
        else:
            return "Enter all values"

    return render_template("signup.html")

#Login successful

@app.route('/successful',methods=['GET','POST'])

def successful():
    if request.method == 'POST':
        return redirect(url_for("myhome"))
    if session["username"]==session["username1"]:
        user=session["username"]
        return render_template("successful.html",user=user)
    else:
        return redirect(url_for("index"))
    

#FLASK APP

if __name__ == '__main__' :
    app.run(debug=True,host="0.0.0.0",port=3000)


