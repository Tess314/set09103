from flask import Flask, url_for, request
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
        return "Hello, %s" % username
    else:
        page = '''
        <html><body>
        <form action="" method="post" name="form">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username"/><br><br>
        <label for="password">Password:</label>
        <input type="text" name="password" id="password"/><br><br>
        <label for="branch">Branch:</label>
        <select name="branch" id="branch">
            <option value="piershill">Piershill</option>
            <option value="central">Central Library</option>
            <option value="portobello">Portobello</option>
        </select><br><br>
        <input type="submit" name="login" id="submit"/>
        </form>
        </body></html>'''

        return page

@app.route('/static-example')
def static_example():
    start = '<img src="'
    url = url_for('static', filename='book.png')
    end = '">'
    return start+url+end, 200

@app.route("/welcome/", methods=['POST','GET'])
def welcome():
    if request.method == 'POST':
        print(request.form)
        search = request.form['search']
        return "You searched for: %s" % search
    else:
        page = '''
        <html><body>
        <form action="" method="post" name="form">
        <input type="text" name="search" id="search"/>
        <input type="submit" name="search" id="submit"/>
        </form>
        </body></html>'''

        return page

@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for('static', filename='alice.gif')
    end = '">'
    image = start+url+end
    return image + "Error 404: You've fallen down the rabbit hole.", 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
