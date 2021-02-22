import os
from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime
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
@app.route("/home", methods=["GET", "POST"])
def home():
    categories = mongo.db.categories.find()
    home_search_cat = mongo.db.categories.find()
    featured_review = mongo.db.reviews.find({"is_featured": 1})

    if request.method == "POST":
        return redirect(url_for('get_books'))

    return render_template(
        "home.html", categories=categories,
        search_categories=home_search_cat,
        featured_review=featured_review)


@app.route("/register", methods=["GET", "POST"])
def register():
    now = datetime.now()
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username / Password Already Exists !")
            return redirect(url_for('register'))

        new_user = {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "last_login": now.strftime("%m/%d/%Y, %H:%M:%S")
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
    now = datetime.now()
    books = mongo.db.books.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    password = mongo.db.users.find_one(
        {"username": session["user"]})["password"]
    last_login = mongo.db.users.find_one(
        {"username": session["user"]})["last_login"]

    # add the current login date time in the users collection
    login_time = {
        "username": session["user"].lower(),
        "password": password,
        "last_login": now.strftime("%m/%d/%Y, %H:%M:%S")}
    mongo.db.users.update({"username": session["user"].lower()}, login_time)

    return render_template(
        "user_profile.html", username=username,
        login_time=last_login, books=books)


@app.route("/admin_profile", methods=["GET", "POST"])
def admin_profile():
    now = datetime.now()
    featured_review = mongo.db.reviews.find({"is_featured": 1})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    password = mongo.db.users.find_one(
        {"username": session["user"]})["password"]
    last_login = mongo.db.users.find_one(
        {"username": session["user"]})["last_login"]

    # add the current login date time in the users collection
    login_time = {
        "username": session["user"].lower(),
        "password": password,
        "last_login": now.strftime("%m/%d/%Y, %H:%M:%S")}
    mongo.db.users.update({"username": session["user"].lower()}, login_time)

    return render_template("admin_profile.html", username=username,
                           login_time=last_login, 
                           featured_review=featured_review)


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
    now = datetime.now()
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
                        "added_by": session["user"].lower(),
                        "date_added": now.strftime(
                            "%m/%d/%Y")
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
    books = mongo.db.books.find()
    return render_template("display_books.html", books=books)


@app.route("/add_reviews/<book>", methods=["GET", "POST"])
def add_reviews(book):
    today = datetime.now()
    reviews = mongo.db.reviews.find({"book_name": book})
    image_url = mongo.db.books.find_one({"book_name": book})["image_url"]
    author = mongo.db.books.find_one({"book_name": book})["author_name"]

    if request.method == "POST":
        new_review = {"book_name": book,
                        "author_name": author,
                        "review_description": request.form.get(
                            "review_description"),
                        "added_by": session["user"],
                        "added_date": today.strftime("%m/%d/%Y"),
                        "is_featured": 0}

        mongo.db.reviews.insert_one(new_review)
        flash("Review added successfully!")

    return render_template(
        "add_reviews.html", reviews=reviews, image_url=image_url,
        book=book, author=author)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    book = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["book_name"]
    image_url = mongo.db.books.find_one({"book_name": book})["image_url"]
    author = mongo.db.books.find_one({"book_name": book})["author_name"]

    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Removed Successfully!")

    reviews = mongo.db.reviews.find({"book_name": book})

    return render_template(
        "add_reviews.html", book=book, author=author,
        reviews=reviews, image_url=image_url)


@app.route('/edit_review/<review_id>', methods=["GET", "POST"])
def edit_review(review_id):
    today = datetime.now()
    book = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["book_name"]
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    is_featured = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["is_featured"]
    image_url = mongo.db.books.find_one({"book_name": book})["image_url"]
    author = mongo.db.books.find_one({"book_name": book})["author_name"]

    if request.method == "POST":
        edited = {
                    "book_name": book,
                    "author_name": author,
                    "review_description": request.form.get(
                        "review"),
                    "added_by": session["user"],
                    "added_date": today.strftime("%m/%d/%Y"),
                    "is_featured": is_featured}

        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edited)
        flash("Review Edited Successfully!")

        reviews = mongo.db.reviews.find({"book_name": book})

        return redirect(url_for(
            'add_reviews', book=book, author=author,
            reviews=reviews, image_url=image_url))

    return render_template(
        "edit_reviews.html", book=book, author=author,
        review=review, image_url=image_url)


@app.route("/featured_review/<review_id>", methods=["GET", "POST"])
def featured_review(review_id):

    book = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["book_name"]
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["review_description"]
    author = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["author_name"]
    added_by = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["added_by"]
    added_date = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})["added_date"]

    featured_review = {
                "book_name": book,
                "author_name": author,
                "review_description": review,
                "added_by": added_by,
                "added_date": added_date,
                "is_featured": 1}

    # reset all featured review
    mongo.db.reviews.update(
        {"is_featured": 1},
        {"$set": {"is_featured": 0}}

    )
    # set the new featured review
    mongo.db.reviews.update(
        {"_id": ObjectId(review_id)},
        {"$set": {"is_featured": 1}})

    flash("Review Featured Successfully!")

    return redirect(url_for('admin_profile'))


@app.route("/get_books", methods=["GET", "POST"])
def get_books():
    categories = list(mongo.db.categories.find())
    # home_search_cat = mongo.db.categories.find()
    books = mongo.db.books.find()
    return render_template(
        "display_books.html", categories=categories,
        search_categories=categories, books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    categories = mongo.db.categories.find()

    if request.method == "POST":
        return redirect(url_for('filtered_books'))

    return render_template("search.html", search_categories=categories)


@app.route("/filtered_books", methods=["GET", "POST"])
def filtered_books():
    categories = mongo.db.categories.find()
    if request.method == "POST":
        category = request.form.get("category")
        keywords = request.form.get("keywords")

        if not category and keywords == "":
            books = mongo.db.books.find()
        else:
            if category and keywords == "":
                query = {"category_name": category}

            if category and keywords != "":
                query = {{'category_name': category}, '$or:' [
                    {'book_name': keywords, 'author_name': keywords}]}

            if not category and keywords != "":
                query = {'$or:' [{'book_name': keywords,
                                  'author_name': keywords}]}

            books = mongo.db.books.find(query)
        if books.count() == 0:
            flash("Your search did not find any matching records")
        else:
            flash("Your search returned {} Record(s)".format(books.count()))

    return render_template("display_books.html",
                           books=books, search_categories=categories)


@app.route('/category_list/<category>')
def category_list(category):
    books = mongo.db.books.find({"category_name": category})
    flash("{} Book(s) found under {} category".format(books.count(), category))
    return render_template("display_books.html", books=books)


@app.route('/find', methods=["GET", "POST"])
def find():
    if request.method == "POST":
        reviews = mongo.db.reviews.find({
            "added_date": request.form.get('review_date')
        })
        if reviews.count():
            flash("Your search returned {} Result(s)".format(reviews.count()))
            return render_template("admin_profile.html", reviews=reviews)
        else:
            flash("Your search returned 0 Result(s)")

    return render_template("admin_profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
