
#DEPENDENCIES

from flask import Flask, render_template,request,redirect,session,url_for,make_response
from flask import Flask, render_template, request
import sqlite3
import json
from time import time
from random import random

#FLASK APP 

app=Flask(__name__)

app.secret_key="ForHealth"


db=sqlite3.connect("Database.db",check_same_thread=False)
db.row_factory = sqlite3.Row
cursor=db.cursor()

#Home

@app.route('/',methods=['GET','POST'])

def myhome():
    session['username']="null"
    return render_template("home.html")

#LOGIN

@app.route('/login',methods=['GET','POST'])

def login():
    session['username'] = ""
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username=request.form['username']
            password=request.form['password']
            session['username'] = username
            session['username1'] = username
            session['password'] = password
            cursor.execute("SELECT * FROM info1 WHERE name_user=(?) AND password_user=(?)",(username,password))
            
        info=cursor.fetchone()
        
        if info is not None:
            session["email"]=info['email_user']
            if info['name_user'] == username and info['password_user'] == password:
                return redirect(url_for("details"))
        else:
             return render_template("login.html",message1="Password or username didn't match")
    return render_template("login.html")

#SIGNUP

@app.route('/signup',methods=['GET','POST'])

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
  if session["username"]==session["username1"]:
    if request.method == 'POST':
        valuea = request.form["value1"]
        valueb = request.form["value2"]

        def addition(number):
            revs_number = 0
            while (number > 0):  
                remainder = number % 10  
                revs_number = (revs_number * 10) + remainder  
                number = number // 10  
            return revs_number   
        
        value1=addition(int(valuea))
        value2=addition(int(valueb))
        
       
        cursor.execute("INSERT INTO dataform(value1,value2) VALUES((?),(?))",(value1,value2))
        db.commit()
        cursor.execute("select * from dataform ORDER BY ID DESC LIMIT 1")

        dataform=cursor.fetchone()
        if dataform is not None:
                value1dbl=dataform['value1']
                value2dbl=dataform['value2']
                return render_template("dashboard.html",value1db=value1dbl,value2db=value2dbl,user=session["username"])
    else:
        return render_template("dashboard.html",user=session["username"])
  else:
    return redirect(url_for("login"))


# Select positions

@app.route('/select',methods=['GET','POST'])
def select():
    if session["username"] == session["username1"]:
        cursor.execute("select * from info1 WHERE name_user=(?)",(session['username'],))
        dataform=cursor.fetchone()
        if dataform['point1'] is None:
            if request.method == 'POST':
                point1 = request.form["point1"]
                point2 = request.form["point2"]
                cursor.execute("UPDATE info1 SET point1=(?),point2=(?) WHERE name_user=(?)",(point1,point2,dataform['name_user']))
                db.commit()
                return redirect(url_for("select"))
            else:
                return render_template("select.html")

        elif dataform['point1'] is not None:
                point1 = dataform['point1']
                point2 = dataform['point2']
                if request.method == 'POST':
                    point1 = request.form["point1"]
                    point2 = request.form["point2"]
                    cursor.execute("UPDATE info1 SET point1=(?),point2=(?) WHERE name_user=(?)",(point1,point2,dataform['name_user']))
                    db.commit()
                    return redirect(url_for("information"))
                    
                return render_template("select.html",point1=point1,point2=point2)
    else:
        return redirect(url_for("login"))

# Details of user form

@app.route('/details',methods=['GET','POST'])
def details():
    if session["username"] == session["username1"]:
        cursor.execute("select * from info1 WHERE name_user=(?)",(session['username'],))
        dataform=cursor.fetchone()
        if dataform['uname'] is None:
            if request.method == 'POST':
                name = request.form["uname"]
                age = request.form["uage"]
                weight = request.form["uweight"]
                height = request.form["uheight"]
                cursor.execute("UPDATE info1 SET uname=(?),uage=(?),uweight=(?),uheight=(?) WHERE name_user=(?)",(name,age,weight,height,dataform['name_user']))
                db.commit()
                return redirect(url_for("select"))
            
            else:
                return render_template("form.html")

        elif dataform['uname'] is not None:
                uname = dataform['uname']
                uage = dataform['uage']
                uweight = dataform['uweight']
                uheight = dataform['uheight']
                if request.method == 'POST':
                    name = request.form["uname"]
                    age = request.form["uage"]
                    weight = request.form["uweight"]
                    height = request.form["uheight"]
                    cursor.execute("UPDATE info1 SET uname=(?),uage=(?),uweight=(?),uheight=(?) WHERE name_user=(?)",(name,age,weight,height,dataform['name_user']))
                    db.commit()
                    return redirect(url_for("select"))
                    
                return render_template("form.html",uname=uname,uage=uage,uweight=uweight,uheight=uheight)
    else:
        return redirect(url_for("login"))

@app.route('/information',methods=['GET','POST'])
def information():
    if session["username"] == session["username1"]:
        return render_template("fourthpage.html")

# @/data route to send data from database to webpage

@app.route('/data')
def data():
    if session["username"]==session["username1"]:
        cursor.execute("select * from dataform ORDER BY ID DESC LIMIT 1")
        dataform=cursor.fetchone()
        if dataform is not None:
            data = [time() * 10000,dataform["value1"]]
            response = make_response(json.dumps(data))
            response.content_type = 'application/json'
            return response
    else:
       return redirect(url_for("login")) 


@app.route('/data1')
def data1():
    if session["username"]==session["username1"]:
        data = [time() * 100000,random()*100*time()]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
       return redirect(url_for("login")) 


@app.route('/data2')
def data2():
    if session["username"]==session["username1"]:
        data = [time() * 100000,random()*random()]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
       return redirect(url_for("login")) 



@app.route('/data3')
def data3():
    if session["username"]==session["username1"]:
        data = [time() * 10000,random()*100]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
       return redirect(url_for("login")) 

#FLASK APP

if __name__ == '__main__' :

    app.run(debug=True,host="0.0.0.0",port=3000)


