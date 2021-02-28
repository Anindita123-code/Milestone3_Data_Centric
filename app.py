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
# home page listing function
def home():
    categories = list(mongo.db.categories.find())
    featured_review = mongo.db.reviews.find({"is_featured": 1})

    if request.method == "POST":
        return redirect(url_for('get_books'))

    return render_template(
        "home.html", categories=categories,
        search_categories=categories,
        featured_review=featured_review)


@app.route("/register", methods=["GET", "POST"])
# New User Registration Page
def register():
    now = datetime.now()
    if request.method == "POST":
        # check if a matching username is found in the database
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if user_exists:
            flash("Username / Password Already Exists !")
        else:
            new_user = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email"),
                "password": generate_password_hash(
                    request.form.get("password")),
                "last_login": now.strftime("%m/%d/%Y, %H:%M:%S")
            }
            # if user if not already present in the database, create a new user
            mongo.db.users.insert_one(new_user)

            # store in session variable
            session["user"] = request.form.get("username").lower()
            flash("You have been registered successfully !!")
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
# Existing user login to the website
def login():
    if request.method == "POST":
        # check for matching username in database
        db_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        # if found, further check for matching password and
        # display appropriate message
        if db_user:
            if check_password_hash(
                    db_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()

                flash("Login Successful for {}".format(request.form.get(
                    "username").capitalize()))
            else:
                flash("Invalid Username / Password !!")
        else:
            flash("Invalid Username / Password!!")
    # if user has logged in as "admin" route to the
    # admin_profile else route to "user_profile" page
    if 'user' in session:
        if session["user"] == "admin":
            return redirect(url_for('admin_profile'))
        elif len(session["user"]) >= 5:
            return redirect(url_for('user_profile', username=session["user"]))

    return render_template('login.html')


@app.route('/forgot_password', methods=["GET", "POST"])
# called for changing password in Forgot_password.html
def forgot_password():
    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"$and": [{"username": request.form.get(
                        "username")}, {"email": request.form.get("email")}]})
        if user:
            user_id = mongo.db.users.find_one(
                {"username": request.form.get("username")})["_id"]
            if user_id:
                if request.form.get(
                    "new_password") == request.form.get(
                        "reenter_password"):
                    mongo.db.users.update(
                        {"_id": ObjectId(user_id)},
                        {"$set": {"password": generate_password_hash(
                            request.form.get("new_password"))}})
                    flash("New Password generated Successfully!")
                else:
                    flash("Passwords doesnot match, Please try again.")
        else:
            flash("Invalid User!")

    return render_template("forgot_password.html")


@app.route("/user_profile/<username>", methods=["GET", "POST"])
# user profile page display for normal user
def user_profile(username):
    now = datetime.now()
    last_login = now.strftime("%m/%d/%Y, %H:%M:%S")
    books = mongo.db.books.find()

    if session["user"]:
        userid = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]

        mongo.db.users.update(
            {"_id": userid},
            {"$set": {"last_login": last_login}})
    else:
        return redirect(url_for('login'))

    return render_template('user_profile.html', username=session["user"],
                           login_time=last_login, books=books)


@app.route("/admin_profile", methods=["GET", "POST"])
# admin profile page display for admin user
def admin_profile():
    now = datetime.now()
    last_login = now.strftime("%m/%d/%Y, %H:%M:%S")
    featured_review = mongo.db.reviews.find({"is_featured": 1})

    if session["user"]:
        userid = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]

        mongo.db.users.update(
                    {"_id": userid},
                    {"$set": {"last_login": last_login}})

    return render_template("admin_profile.html", username=session["user"],
                           last_login=last_login,
                           featured_review=featured_review)


@app.route("/logout")
# logout and remove the session variable
def logout():
    if 'user' in session:
        session.pop('user')
        # session.pop('last_login')
        flash("You have been logged out!")
        return redirect(url_for('home'))

    return render_template("home.html")


@app.route('/add_books', methods=["GET", "POST"])
# add new books in the database only if it doesnot already exist
# if a book already exists then give appropriate message and redirect user
def add_books():
    categories = mongo.db.categories.find()
    now = datetime.now()
    if request.method == "POST":
        db_book = mongo.db.books.find_one(
            {"book_name": request.form.get("book_name")},
            {"author_name": request.form.get("author")})
        if db_book:
            flash("This Book already exists in the database.")
            return redirect('add_books')
        else:
            newBook = {
                        "category_name": request.form.get("category"),
                        "book_name": request.form.get("book_name"),
                        "author_name": request.form.get("author"),
                        "image_url": request.form.get("image_url"),
                        "description": request.form.get("description"),
                        "added_by": session["user"],
                        "date_added": now.strftime(
                            "%m/%d/%Y")
                    }
            mongo.db.books.insert_one(newBook)
            flash("New Book Added Successfully!")
            if 'user' in session:
                if session["user"] == "admin":
                    return redirect(url_for('admin_profile'))
                elif len(session["user"]) >= 5:
                    return redirect(url_for(
                        'user_profile', username=session["user"]))

    return render_template("add_books.html", categories=categories)


@app.route("/edit_books/<book_id>", methods=["GET", "POST"])
# Edits and saves an existing book record already available in database
def edit_books(book_id):
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
# Remove a selected book from the database
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Deleted Successfully")
    books = mongo.db.books.find()
    return render_template("display_books.html", books=books)


@app.route("/add_reviews/<book>", methods=["GET", "POST"])
# Add review for a book by logged in normal user
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
# Remove a review from reviews collection by selecting individual reviewid
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
# edit a review by reviewid already stored in the reviews collection
# update the added_date to current date
def edit_review(review_id):
    today = datetime.now()
    book = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["book_name"]
    review = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id)})
    image_url = mongo.db.books.find_one({"book_name": book})["image_url"]
    author = mongo.db.books.find_one({"book_name": book})["author_name"]

    if request.method == "POST":
        mongo.db.reviews.update(
            {"_id": ObjectId(review_id)},
            {"$set": {"review_description": request.form.get(
                "review"), "added_date": today.strftime("%m/%d/%Y")}})

        flash("Review Edited Successfully!")

        reviews = mongo.db.reviews.find({"book_name": book})

        return redirect(url_for(
            'add_reviews', book=book, author=author,
            reviews=reviews, image_url=image_url))

    return render_template(
        "edit_reviews.html", book=book, author=author,
        review=review, image_url=image_url)


@app.route("/featured_review/<review_id>", methods=["GET", "POST"])
# Sets the is_featured flag for the reviewid only to 1, unsets all others
def featured_review(review_id):
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
# lists the books into display_books.html
def get_books():
    categories = list(mongo.db.categories.find())
    books = mongo.db.books.find()
    if session["user"] != "admin" and session["user"] != "":
        return redirect(url_for('user_profile', username=session["user"]))

    return render_template(
        "display_books.html", categories=categories,
        search_categories=categories, books=books)


@app.route("/search", methods=["GET", "POST"])
# Book search called from the search_include html file
def search():
    categories = mongo.db.categories.find()

    if request.method == "POST":
        return redirect(url_for('filtered_books'))

    return render_template("search.html", search_categories=categories)


@app.route("/filtered_books", methods=["GET", "POST"])
# filters book in accordance with the search results using search books option
def filtered_books():
    categories = mongo.db.categories.find()
    if request.method == "POST":
        category = request.form.get("category")
        keywords = request.form.get("keywords")

        if not category and keywords == "":
            books = mongo.db.books.find()
        else:
            if category:
                if keywords == "":
                    query = {"category_name": category}
                else:
                    query = {"$and": [{"category_name": category},
                                      {"book_name": keywords}]}
            else:
                if keywords != "":
                    query = {"book_name": keywords}
                    # query = {"$text": {"$search": keywords}}

            books = mongo.db.books.find(query)

        if books.count() == 0:
            flash("Your search did not return any matches")
        else:
            flash("Your search returned {} match(es)".format(books.count()))

    return render_template("find_books.html",
                           books=books, search_categories=categories)


@app.route('/category_list/<category>')
# Home page category list results display using display books.html
def category_list(category):
    books = mongo.db.books.find({"category_name": category})
    flash("{} Book(s) found under {} category".format(books.count(), category))

    categories = mongo.db.categories.find()
    return render_template(
        "display_books.html", books=books, search_categories=categories)


@app.route('/find', methods=["GET", "POST"])
# called from admins profile page to find reviews as per search
def find():
    if request.method == "POST":
        last_login = mongo.db.users.find_one(
            {"username": session["user"]})["last_login"]
        if request.form.get("book_name") and not request.form.get(
                                                    "review_date"):
            query = {"book_name": request.form.get("book_name")}
        elif not request.form.get("book_name") and request.form.get(
                                                    "review_date"):
            query = {"added_date": request.form.get('review_date')}
        else:
            query = {"$and": [{"book_name": request.form.get("book_name")},
                              {"added_date": request.form.get('review_date')}]}
        if not request.form.get('book_name') and not request.form.get(
                                                            'review_date'):
            flash("Please filter by Book name or Review Date to proceed")
            return redirect(url_for('admin_profile'))
        else:
            reviews = mongo.db.reviews.find(query)

            if reviews.count():
                flash("Your search returned {} Result(s)".format(
                                                    reviews.count()))
                return render_template(
                    "admin_profile.html", reviews=reviews,
                    last_login=last_login)
            else:
                flash("Your search returned 0 Result(s)")

    return render_template("admin_profile.html", last_login=last_login)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
