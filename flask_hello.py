from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
	return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Hello Napier"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye World"

@app.errorhandler(404)
def page_not_found(error):
    return "Error 404: Couldn't find the page you requested.", 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
