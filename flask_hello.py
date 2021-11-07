from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def root():
	return "TTTLE"

@app.route("/login/")
def hello():
    return "LOG IN"

@app.route('/static-example')
def static_example():
    start = '<img src="'
    url = url_for('static', filename='book.png')
    end = '">'
    return start+url+end, 200

@app.route("/welcome/")
def goodbye():
    return "WELCOME"

@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for('static', filename='alice.gif')
    end = '">'
    image = start+url+end
    return image + "Error 404: You've fallen down the rabbit hole.", 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
