from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'

@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

if __name__ == '__main__':
	app.run(debug=True)