
#DEPENDENCIES

from datetime import time
from os import name
from flask import Flask, render_template,request,redirect,session,url_for,current_app
import MySQLdb 
from flask_mysqldb import MySQL
from flask import Flask, render_template, request
import sqlite3
import math
import time
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
    session['username']="null"
    return render_template("home.html")

#LOGIN

@app.route('/login.html',methods=['GET','POST'])

def login():
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
                return redirect(url_for("dashboard"))
        else:
             return render_template("login.html",message1="Password or username didn't match")
    return render_template("login.html")

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
                return redirect(url_for("login"))
            else:
                return render_template("signup.html",message="Password didn't match")
        else:
            return "Enter all values"

    return render_template("signup.html")

#Login successful to dashboard




@app.route('/dashboard',methods=['GET','POST'])

def dashboard():
#   if session["username"]==session["username1"]:
    # if request.method == 'POST':
        # valuea = request.form["value1"]
        # valueb = request.form["value2"]

        # def addition(number):
        #     revs_number = 0
        #     while (number > 0):  
        #         remainder = number % 10  
        #         revs_number = (revs_number * 10) + remainder  
        #         number = number // 10  
        #     return revs_number   
        num=1
        while num<100:
            value1=num
            value2=num+1
            num=num+1
            time.sleep(1)
            cursor.execute("INSERT INTO dataform(value1,value2) VALUES((?),(?))",(value1,value2))
            db.commit()
            cursor.execute("SELECT * FROM dataform WHERE value1=(?) AND value2=(?)",(value1,value2))

            dataform=cursor.fetchone()
        
            if dataform is not None:
                value1dbl=dataform['value1']
                value2dbl=dataform['value2']
                return render_template("dashboard.html",value1db=value1dbl,value2db=value2dbl)
    

        
#   user=session["username"]
#   return render_template("dashboard.html",user=user)
    
#   else:
#     return redirect(url_for("login"))


#FLASK APP

if __name__ == '__main__' :
    app.run(debug=True,host="0.0.0.0",port=3000)


