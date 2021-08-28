
#DEPENDENCIES

from flask import Flask, render_template,request,redirect,session,url_for,current_app
from flask import Flask, render_template, request
import sqlite3
import os
import sys
# from flask_mysqldb import MySQL

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
        cursor.execute("SELECT * FROM dataform WHERE value1=(?) AND value2=(?)",(value1,value2))

        dataform=cursor.fetchone()
        
        if dataform is not None:
            value1dbl=dataform['value1']
            value2dbl=dataform['value2']
            return render_template("dashboard.html",value1db=value1dbl,value2db=value2dbl)
    

        
    user=session["username"]
    return render_template("dashboard.html",user=user)
    
  else:
    return redirect(url_for("login"))


@app.route('/wifion',methods=['GET','POST'])

def dashboard():
#turn on wifi
    user=input("Enter Username of WIFI : ")
    password=input("Enter Password WIFI ")

    print("Connecting to wifi ...")

    code="""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN

network={
        ssid="{}"
        psk="{}"
        key_mgmt=WPA-PSK
}
""".format(user,password)

    os.system("cd ~")
    os.system("cd ForHealth")
    os.system("cd /etc/wpa_supplicant/")

    # open('wpa_supplicant.conf', 'w').close()
    with open("wpa_supplicant.conf", "w") as f:
        f.write(code)
        f.close()

    os.system("sudo /usr/bin/autohotspotN")


#FLASK APP

if __name__ == '__main__' :
    print("Creating Hotspot ...")

    code="""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN

network={
        ssid="nono"
        psk="99889900"
        key_mgmt=WPA-PSK
}
"""

    os.system("cd /etc/wpa_supplicant/")

    # open('wpa_supplicant.conf', 'w').close()
    with open("wpa_supplicant.conf", "w") as f:
        f.write(code)
        f.close()
    os.system("cd ~")
    os.system("cd ForHealth")
    os.system("sudo /usr/bin/autohotspotN")

    app.run(debug=True,host="0.0.0.0",port=3000)


