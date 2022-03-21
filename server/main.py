import flask
from flask import Flask, render_template, request,jsonify, make_response
from flask_cors import CORS
#-------------------------------------------------------------------------------
from db_connection import dbConnect
#-------------------------------------------------------------------------------
#FOR RUNNING FIRST:
#>>set/export FLASK_APP=main.py
#>>python -m flask run
app=Flask(__name__)#initialisation
cors = CORS(app)#CORS for app
db_client=dbConnect()

@app.route("/insert",methods=["POST"])
def insert():
    data=request.json
    try:
        db_client.insert(data)
        return ({"message":"Succesful"},200)
    except:
        print("COULDNT")
        return ({"message":"Failure"})

@app.route("/view",methods=["GET"])
def view():
    try:
        a=db_client.read()
        print(a)
        return (jsonify(db_client.read()),200)
    except:
        return ({"message":"Failed to Read"},404)

@app.route("/delete",methods=["DELETE"])
def delete():
    data=request.json
    try:
        db_client.delete(data)
        return ({"message":"Succesful"},200)
    except:
        return ({"message":"Failed to Read"},404)  

app.run()