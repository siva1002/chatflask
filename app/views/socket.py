from app import sockio,app
from flask_socketio import emit,send
from flask import Flask, render_template
@sockio.on('message')
def handlemessage(m):
    # l=['new',4,2,4,5]
    # for i in l:
    #     print(i)
    print(m)
    send(m,broadcast=True)
@app.route('/',methods=["GET"])
def home():
    print('hi')
    return render_template('index.html')