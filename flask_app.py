from flask import Flask, url_for, request, render_template, redirect, g
import sqlite3

app = Flask(__name__)
db_location = 'var/books.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route("/")
def root():
    start = '<img src="'
    url = url_for('static', filename='book.png')
    end = '">'
    logo = start+url+end
    return logo + render_template('index.html')

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
    db = get_db()
    db.commit()
    page = []
    page.append('<ul>')

    if request.method == 'POST':
        print(request.form)
        search = request.form['search']
        search_term = "%s" % search
        sql = "SELECT * FROM books WHERE title = ? OR author = ?"
        for row in db.cursor().execute(sql, [search_term, search_term]):
            page.append('<li>')
            page.append(str(row))
            page.append('</li>')
        page.append('</ul>')
        formatting = ''.join(page)
        return render_template('welcome.html') + formatting
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
    return render_template('error.html') + image, 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
