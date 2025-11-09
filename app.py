from flask import Flask, jsonify, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = "bookstore_secret_key"

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password'
app.config['MYSQL_DB'] = 'bookstore'

mysql = MySQL(app)


@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template("index.html", books=books)


@app.route("/api/books")
def books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    result = cur.fetchall()

    books = []
    for row in result:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "price": float(row[3])
        })

    return jsonify(books)



# payment

@app.route('/checkout/<int:book_id>')
def checkout(book_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()
    return render_template("checkout.html", book=book)


@app.route('/place_order', methods=['POST'])
def place_order():
    return "<h1>Payment Done Successfully (Simulated) ✅</h1>"




# ---------------- LOGIN ----------------
@app.route("/login", methods=['GET', 'POST'])
def login():
    msg = ''
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        account = cur.fetchone()

        if account:
            session['logged_in'] = True
            session['username'] = username
            return redirect("/admin")
        else:
            msg = "Incorrect username/password!"

    return render_template("login.html", msg=msg)


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()

        return redirect("/login")
    
    return render_template("register.html")


# ---------------- ADMIN PANEL ----------------
@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect("/login")

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    return render_template("admin.html", books=books)


@app.route("/addbook", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    price = request.form["price"]

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (title, author, price) VALUES (%s, %s, %s)", (title, author, float(price)))
    mysql.connection.commit()

    return redirect("/admin")


@app.route("/delete/<int:id>")
def delete_book(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (id,))
    mysql.connection.commit()

    return redirect("/admin")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
