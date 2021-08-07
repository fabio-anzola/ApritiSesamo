import os

from flask import Flask, send_from_directory, request, jsonify

from functools import wraps

from werkzeug.security import check_password_hash
import jwt
import datetime

from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

from gpiozero import LED
from gpiozero import DistanceSensor
from gpiozero import LineSensor

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

if os.environ['ENIRONMENT'] != 'dev':
  relay = LED(18)
  ready_led = LED(21)
  wait_led = LED(20)
  error_led = LED(16)
  distance_sensor = DistanceSensor(echo=23, trigger=24)
  env_sensor = LineSensor(12)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50), unique=True)
  name = db.Column(db.String(50))
  password = db.Column(db.String(80))
  admin = db.Column(db.Boolean)

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None

    if 'x-access-token' in request.headers:
      token = request.headers['x-access-token']

    if not token:
      return jsonify({'message': 'Token invalid or missing'}), 401

    try:
      data = jwt.decode(
        token, app.config['SECRET_KEY'], algorithms=["HS256"])

      current_user = User.query.filter_by(
        public_id=data['public_id']).first()

    except:
      return jsonify({'message': 'Token invalid or missing'}), 401

    return f(current_user, *args, **kwargs)

  return decorated

@app.route('/')
@token_required
def index():
	return 'Hello, Flask!'

@app.route("/robots.txt")
def robots():
  return send_from_directory("static", "robots.txt")

@app.route('/login')
def login():
  auth = request.authorization

  if not auth or not auth.username or not auth.password:
    return jsonify({'message':'Could not verify'}), 401

  user = User.query.filter_by(name=auth.username).first()

  if not user:
    return jsonify({'message':'Could not verify'}), 401

  if check_password_hash(user.password, auth.password):
    token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=99999)}, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token})

  return jsonify({'message':'Could not verify. This attempt has been logged. All browser- and userdata has been stored.'}), 401

@app.route('/whoami')
@token_required
def whoami(current_user=User(name='anonymous')):
  if current_user.name == 'anonymous':
    return jsonify({'user': 'anonymous'})
  else:
    return jsonify({
      'user': current_user.name,
      'uuid': current_user.public_id
    })

@app.route('/door/trigger', methods=['GET'])
@token_required
def trigger(current_user):
  if current_user.admin:
    return jsonify({'message': 'Admin cannot perform this action'}), 403

  # do stuff

  return jsonify({
    'message': "Door has been toggled"
  })

@app.route('/door/status', methods=['GET'])
@token_required
def doorstatus(current_user):
  if current_user.admin:
    return jsonify({'message': 'Admin cannot perform this action'}), 403

  if os.environ['ENIRONMENT'] == 'dev':
    return jsonify({
      'status': 'dev-enabled',
      'sensor_reading': (100)
    })
  elif (distance_sensor.distance * 100) < 15.0:
    return jsonify({
      'status': 'open',
      'sensor_reading': (distance_sensor.distance * 100)
    })
  else:
    return jsonify({
      'status': 'closed',
      'sensor_reading': (distance_sensor.distance * 100)
    })

def set_ready():
    """
    Sets ready led
    """
    ready_led.on()
    wait_led.off()
    error_led.off()
    sleep(1)
    ready_led.off()


def set_wait():
    """
    Sets wait led
    """
    ready_led.off()
    wait_led.on()
    error_led.off()


def set_error():
    """
    Sets error led
    """
    ready_led.off()
    wait_led.off()
    error_led.on()

if __name__ == '__main__':
	app.run(debug=True)