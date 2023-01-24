from app import sockio,app
from flask_socketio import emit,send

if __name__ == '__main__':
    sockio.run(app)