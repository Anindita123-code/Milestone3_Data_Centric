import os
from flask import Flask
from flask_pymongo import PyMongo
from datetime import date
from bson.objectid import ObjectId

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from werkzeug.security import (
    generate_password_hash, check_password_hash)

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DB"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    categories = mongo.db.categories.find()
    return render_template("home.html", categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username / Password Already Exists !")
            return redirect(url_for('register'))

        new_user = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)
        # store in session variable

        session["user"] = request.form.get("username").lower()
        flash("You have been registered successfully !!")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if db_user:
            if check_password_hash(
                    db_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get(
                    "username").capitalize()))
            else:
                flash("The Username and/or Password doesnot match!!")
        else:
            flash("The Username and/or Password doesnot match!!")

    if 'user' in session:
        if session["user"].lower() == "admin":
            return redirect(url_for('admin_profile'))
        elif len(session["user"]) >= 5:
            return redirect(url_for('user_profile', username=session["user"]))

    return render_template('login.html')


@app.route("/user_profile/<username>", methods=["GET", "POST"])
def user_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template("user_profile.html", username=username)


@app.route("/admin_profile", methods=["GET", "POST"])
def admin_profile():
    return render_template("admin_profile.html")


@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
        flash("You have been logged out!")

    categories = mongo.db.categories.find()
    return render_template("home.html", categories=categories)


@app.route('/add_books', methods=["GET", "POST"])
def add_books():
    categories = mongo.db.categories.find()
    today = date.today()
    if request.method == "POST":
        db_book = mongo.db.books.find_one(
            {"book_name": request.form.get("book_name").lower()},
            {"author_name": request.form.get("author").lower()})
        if db_book:
            flash("This Book already exists in the database.")
            return redirect('add_books')
        else:
            newBook = {
                        "category_name": request.form.get("category"),
                        "book_name": request.form.get("book_name").lower(),
                        "author_name": request.form.get("author").lower(),
                        "image_url": request.form.get("image_url").lower(),
                        "description": request.form.get("description").lower(),
                        "added_by": session["user"].lower()
                        #"date_added": today
                    }
            mongo.db.books.insert_one(newBook)
            flash("New Book Added Successfully!")
            if 'user' in session:
                if session["user"].lower() == "admin":
                    return redirect(url_for('admin_profile'))
                elif len(session["user"]) >= 5:
                    return redirect(url_for(
                        'user_profile', username=session["user"]))

    return render_template("add_books.html", categories=categories)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    if request.method == "POST":
        update = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "added_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, update)
        flash("Book Updated Successfully")
        return redirect(url_for('get_books'))

    return render_template("edit_books.html", categories=categories, book=book)


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Deleted Successfully")
    return render_template("display_books.html")


@app.route("/get_books", methods=["GET", "POST"])
def get_books():
    books = mongo.db.books.find()
    return render_template("display_books.html", books=books)


@app.route("/find_books/<category>", methods=["GET", "POST"])
def find_books(category):
    categories = mongo.db.categories.find()

    if request.method == "POST":
        books = mongo.db.books.find(
            {"category_name": request.form.get("category")})
        return redirect(url_for('get_books', books=books))

    return render_template("find_books.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
