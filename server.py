from flask import Flask, send_from_directory, request, jsonify

from functools import wraps

app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)