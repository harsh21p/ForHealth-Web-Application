# ForHealth

Control Web Application

Tech : MySQL Database, Python Flask, HTML, CSS.

Steps to run :

Open the project directory.

First you have to run the file reqirements.txt to install all the requirements for the project

$ pip install -r requirements.txt

After the installation of all the requirements 

We have to setup sql database.

To create database we have to run the database.sql file

Note : You can run it by opening it into mysql workbench.

After creating the database change database config. in main.py file and run the file main.py

$ python main.py

Open http://127.0.0.1:3000 in browser on the same machine.

Access app from another device. 

Steps :

1) Turn on the hotspot of your machine (where the flask server is running ) 
2) Connect your device to the hotspot.
3) Run main.py file 
4) Open the link shown by flask server in browser of your device
