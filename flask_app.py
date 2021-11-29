from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

@app.route("/")
def root():
	return "TTTLE"

@app.route("/login/", methods=['POST','GET'])
def log_in():
    if request.method == 'POST':
        print(request.form)
        username = request.form['username']
        print(request.form)
        password = request.form['password']
        print(request.form)
        branch = request.form['branch']
        return redirect('/welcome/')
    else:
        return render_template('login.html')

@app.route("/welcome/", methods=['POST','GET'])
def welcome():
    if request.method == 'POST':
        print(request.form)
        search = request.form['search']
        return "You searched for: %s" % search
    else:
        return render_template('welcome.html')

@app.route("/add/")
def add():
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for('static', filename='alice.gif')
    end = '">'
    image = start+url+end
    return image + render_template("error.html"), 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
