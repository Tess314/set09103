from flask import Flask, url_for, request, render_template, redirect, g
import sqlite3

app = Flask(__name__)
db_location = 'var/books.db'

# DB setup and config
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

# Loads in schema file and initialises DB
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Start page - loads up logo and redirect to welcome page
@app.route("/", methods=['POST','GET'])
def root():
    if request.method == 'POST':
        print(request.form)
        start = request.form['start']
        return redirect('/welcome/')
    else:
        start = '<img src="'
        url = url_for('static', filename='book.png')
        end = '">'
        logo = start+url+end
        return logo + render_template('index.html')

# Welcome page - executes search query on DB
@app.route("/welcome/", methods=['POST','GET'])
def welcome():
    db = get_db()
    db.commit()
    page = []
    page.append('<table>')

    if request.method == 'POST':
        if request.form['search']:
            print(request.form)
            search = request.form['search']
            search_term = "%s" % search
            sql = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR synopsis LIKE ?"
            for row in db.cursor().execute(sql, ['%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%',]):
                page.append('<td>')
                page.append(str(row))
                page.append('<td>')
            page.append('</table>')
            formatting = ''.join(page)
            message = "Here's what we found:"
            return render_template('welcome.html', message=message) + formatting
        elif request.form['action'] == "ADD BOOK":
            print(request.form)
            return redirect('/add/')
    else:
        return render_template('welcome.html')

# Add page - executes insert on DB
@app.route("/add/", methods=['POST','GET'])
def add():
    db = get_db()
    db.commit()

    if request.method == 'POST':
        if request.form['add2']:
            print(request.form)
            title = request.form['title']
            title_entered = "%s" % title
            print(request.form)
            author = request.form['author']
            author_entered = "%s" % author
            print(request.form)
            synopsis = request.form['synopsis']
            synopsis_entered = "%s" % synopsis
            sql = "INSERT INTO books (title, author, synopsis) VALUES (?,?,?)"
            db.cursor().execute(sql, [title_entered, author_entered, synopsis_entered])
            db.commit()
        return render_template('add.html')
    else:
        return render_template('add.html')

# Custom 404 page - returns error message and image
@app.errorhandler(404)
def page_not_found(error):
    start = '<img src="'
    url = url_for('static', filename='alice.gif')
    end = '">'
    image = start+url+end
    return render_template('error.html') + image, 404

if __name__ == "main":
    app.run(host='0.0.0.0', debug=True)
