from app import sockio,app
from flask_socketio import emit,send
from flask import Flask, render_template,Blueprint


@app.route('/',methods=["GET"])
def home():
    print('hi')
    return render_template('index.html')