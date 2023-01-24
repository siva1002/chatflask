from app import sockio,app
from flask_socketio import emit,send
@sockio.on('message')
def handlemessage(m):
    # l=['new',4,2,4,5]
    # for i in l:
    #     print(i)
    print(m)
    send(m,broadcast=True)
if __name__ == '__main__':
    sockio.run(app)