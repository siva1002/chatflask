from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
import os


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
sockio = SocketIO(app,cors_allowed_origins="*")
# if os.environ.get('ENV') == 'TEST':
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI_TEST')
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI_DEV')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Mail settings:
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'admin@cryomate.in'
# app.config['MAIL_PASSWORD'] = 'gswibbgzdhpoklwa'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
app.config['DEBUG'] = True
# from cryo.mqtt.fetchdata import fetch_data
# app.register_blueprint(fetch_data, url_prefix='/getread')