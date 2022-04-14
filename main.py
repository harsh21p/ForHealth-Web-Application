
# DEPENDENCIES

from flask import Flask,jsonify, render_template, request, redirect, session, url_for, make_response
from flask import Flask, render_template, request
import sqlite3
import json
from time import time
from random import randint, random
import Adafruit_ADS1x15
from flask.helpers import flash
import xlwt
from xlwt import Workbook
import numpy as np
from time import sleep
from gpiozero import PWMLED
from gpiozero import LED
from time import sleep
from gpiozero import RotaryEncoder
import angletest as angletest

# FLASK APP NEW

app = Flask(__name__)  

app.secret_key = "ForHealth"

db = sqlite3.connect("Database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

# Home
  

@app.route('/', methods=['GET', 'POST'])
def myhome():
    session['username'] = "null"
    return render_template("home.html")

# LOGIN

@app.route('/login', methods=['GET', 'POST'])
def login():
    session['username'] = "null"
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            session['username'] = username
            session['username1'] = username
            session['password'] = password
            cursor.execute(
                "SELECT * FROM info1 WHERE name_user=(?) AND password_user=(?)", (username, password))

        info = cursor.fetchone()

        if info is not None:
            session["email"] = info['email_user']
            if info['name_user'] == username and info['password_user'] == password:
                return redirect(url_for("details"))
        else:
            return render_template("login.html", message1="Password or username didn't match")
    return render_template("login.html")

# SIGNUP


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        if 'username' in request.form and 'password' in request.form and 'email' in request.form and 'phone' in request.form and 'password1' in request.form and 'address' in request.form:

            username = request.form['username']
            password1 = request.form['password1']
            password = request.form['password']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']
            if password == password1:
                cursor.execute("INSERT INTO info1(name_user,password_user,email_user,phone_user,address_user) VALUES((?),(?),(?),(?),(?))", (
                    username, password1, email, phone, address))
                db.commit()
                return redirect(url_for("login"))
            else:
                return render_template("signup.html", message="Password didn't match")
        else:
            return "404 NOT FOUND"
    return render_template("signup.html")
# Login successful to dashboard


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session["username"] == session["username1"]:
        return render_template("dashboard.html", user=session["username"])
    else:
        return redirect(url_for("login"))


# Select positions

@app.route('/select', methods=['GET', 'POST'])
def select():
    
    if session["username"] == session["username1"]:
        cursor.execute("select * from info1 WHERE name_user=(?)",
                       (session['username'],))
        dataform = cursor.fetchone()
        if dataform['point1'] is None:
            if request.method == 'POST':
                point1 = request.form["point1"]
                point2 = request.form["point2"] 
                Resistance = request.form["Resistance"]
                Rep = request.form["rep"]
                cursor.execute("UPDATE info1 SET point1=(?),point2=(?),Resistance=(?),Rep=(?) WHERE name_user=(?)", (
                    point1, point2, Resistance, Rep, dataform['name_user']))
                db.commit()
                if dataform['selectbtn']=="Freedrive":
                    return render_template("fourthpage.html",back="details")
                return render_template("fourthpage.html",back="select")
            else:
                return render_template("select.html",RSA="Resistance")

        elif dataform['point1'] is not None:
            point1 = dataform['point1']
            point2 = dataform['point2']
            Resistance = dataform['Resistance']
            Rep = dataform['Rep']
            if request.method == 'POST':
                point1 = request.form["point1"]
                point2 = request.form["point2"]
                Resistance = request.form["Resistance"]
                Rep = request.form["rep"]
                cursor.execute("UPDATE info1 SET point1=(?),point2=(?),Resistance=(?),Rep=(?) WHERE name_user=(?)", (
                    point1, point2, Resistance, Rep, dataform['name_user']))
                db.commit()
                return redirect(url_for("information"))
            
            if dataform['selectbtn']=="Freedrive":
                return redirect(url_for("information"))
            if dataform['selectbtn']=="Passive":
                return render_template("select.html",RSA="Assistance", point1=point1, point2=point2, Resistance=Resistance,rep=Rep)
            if dataform['selectbtn']=="Active isokinetic":
                return render_template("select.html",RSA="Speed",point1=point1, point2=point2, Resistance=Resistance,rep=Rep)

            return render_template("select.html", point1=point1, point2=point2, Resistance=Resistance,RSA="Resistance",rep=Rep)
    else:
        return redirect(url_for("login"))

# Details of user form

@app.route('/details', methods=['GET', 'POST'])
def details():
    if session["username"] == session["username1"]:
        cursor.execute("select * from info1 WHERE name_user=(?)",
                       (session['username'],))
        dataform = cursor.fetchone()
        if dataform['uname'] is None:
            if request.method == 'POST':
                name = request.form["uname"]
                age = request.form["uage"]
                weight = request.form["uweight"]
                height = request.form["uheight"]
                selectbtn = request.form["selectbtn"]
                cursor.execute("UPDATE info1 SET uname=(?),uage=(?),uweight=(?),uheight=(?),selectbtn=(?) WHERE name_user=(?)", (
                    name, age, weight, height, selectbtn, dataform['name_user']))
                db.commit()

                return redirect(url_for("select"))
            else:
                return render_template("form.html")

        elif dataform['uname'] is not None:
            uname = dataform['uname']
            uage = dataform['uage']
            uweight = dataform['uweight']
            uheight = dataform['uheight']
            selectbtn = dataform['selectbtn']
            if request.method == 'POST':
                name = request.form["uname"]
                age = request.form["uage"]
                weight = request.form["uweight"]
                height = request.form["uheight"]
                selectbtn = request.form["selectbtn"]
                cursor.execute("UPDATE info1 SET uname=(?),uage=(?),uweight=(?),uheight=(?),selectbtn=(?) WHERE name_user=(?)", (
                    name, age, weight, height, selectbtn, dataform['name_user']))
                db.commit()

                return redirect(url_for("select"))

            return render_template("form.html", uname=uname, uage=uage, uweight=uweight, uheight=uheight, selectbtn=selectbtn)
    else:
        return redirect(url_for("login"))


@app.route('/information', methods=['GET', 'POST'])
def information():
    cursor.execute("select * from info1 WHERE name_user=(?)",
                       (session['username'],))
    dataform = cursor.fetchone()
    if session["username"] == session["username1"]:
        if dataform['selectbtn']=="Freedrive":
            return render_template("fourthpage.html",back="details")
        return render_template("fourthpage.html",back="select")



@app.route('/torque')
def torque():   
     if session["username"] == session["username1"]:
       
            data = [time() * 10000, randint(1,30000)]
            response = make_response(json.dumps(data))
            response.content_type = 'application/json'
            return response
     else:
         return redirect(url_for("login"))


@app.route('/angle')
def angle():
    if session["username"] == session["username1"]:
        data = [randint(1,360)]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
        return redirect(url_for("login"))

@app.route('/repetition')
def repetition():
    if session["username"] == session["username1"]:
        data = [randint(1,25)]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
        return redirect(url_for("login"))

@app.route('/breakstate')
def breakstate():
    if session["username"] == session["username1"]:
        data = [randint(0,1)]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
        return redirect(url_for("login"))


@app.route('/speed')
def speed():
    if session["username"] == session["username1"]:
        data = [time() * 100000, randint(1,1000)]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response
    else:
        return redirect(url_for("login"))


@app.route('/play', methods=['GET'])
def play():
    if session["username"] == session["username1"]:
        cursor.execute("select * from info1 WHERE name_user=(?)", (session['username'],))
        dataform = cursor.fetchone()
        angle1 = dataform['point1']
        angle2 = dataform['point2']
        rep = dataform['Rep']
        angletest.Repitions(angle1,angle2,rep)
    else:
         return redirect(url_for("login"))
   

# @app.route('/pause', methods=['GET'])
# def pause():
   

# @app.route('/stop', methods=['GET'])
# def stop():


#useless



@app.route('/guest', methods=['GET', 'POST'])
def guest():
    if request.method == 'POST':
        # sql query to inser in database and run the rout for next page 
            # cursor.execute("select * from guest ORDER BY ID DESC LIMIT 1")
            # dataform = cursor.fetchone()

            if request.form['selectbtn']=="Freedrive":
                # fire query to add value accordingly and render to graphs
                cursor.execute("UPDATE guest SET treatment=(?) WHERE ID=(?)", ("Freedrive",1))
                return redirect(url_for("selectguest"))
            if request.form['selectbtn']=="Passive":
                # fire query to add value accordingly and render to select
                cursor.execute("UPDATE guest SET treatment=(?) WHERE ID=(?)", ("Passive",1))
                return redirect(url_for("selectguest"))
            if request.form['selectbtn']=="Active isotonic":
                # fire query to add value accordingly and render to select
                cursor.execute("UPDATE guest SET treatment=(?) WHERE ID=(?)", ("Active isotonic",1))
                return redirect(url_for("selectguest"))
            if request.form['selectbtn']=="Active isometric":
                # fire query to add value accordingly and render to select
                cursor.execute("UPDATE guest SET treatment=(?) WHERE ID=(?)", ("Active isometric",1))
                return redirect(url_for("selectguest"))
            if request.form['selectbtn']=="Active isokinetic":
                # fire query to add value accordingly and render to select
                cursor.execute("UPDATE guest SET treatment=(?) WHERE ID=(?)", ("Active isokinetic",1))
                return redirect(url_for("selectguest"))
    else:
        return render_template("guest.html")

@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    #  requesting data from sql and use if else loop to render accordingly only two if and else 
    cursor.execute("select * from guest ORDER BY ID DESC LIMIT 1")
    dataform = cursor.fetchone()
    if dataform is not None:
        if dataform['treatment']=="Freedrive":
            return render_template("graphs.html",back="guest")
    return render_template("graphs.html",back="selectguest")

@app.route('/selectguest', methods=['GET', 'POST'])
def selectguest():
    # requesting data from sql and use if else loop to render accordingly
    if request.method == 'POST':
        point1 = request.form["point1"]
        point2 = request.form["point2"] 
        Resistance = request.form["Resistance"]
        return redirect(url_for("graphs"))

    cursor.execute("select * from guest ORDER BY ID DESC LIMIT 1")
    dataform = cursor.fetchone()
    if dataform is not None:
        if dataform['treatment']=="Freedrive":
            return redirect(url_for("graphs"))
        if dataform['treatment']=="Passive":
            return render_template("selectguest.html",back="guest",point1="0",point2="0",RSA="Assistance",Resistance="50")
        if dataform['treatment']=="Active isokinetic":
            return render_template("selectguest.html",back="guest",point1="0",point2="0",RSA="Speed",Resistance="50")
        else:
            return render_template("selectguest.html",back="guest",point1="0",point2="0",RSA="Resistance",Resistance="50")

    else:
        return redirect(url_for("guest"))



# FLASK APP

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=80)

