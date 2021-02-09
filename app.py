import os
from flask import Flask
from flask_pymongo import PyMongo
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
@app.route("/home",)
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

    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
            else:
                flash("The Username and/or Password doesnot match!!")
        else:
            flash("The Username and/or Password doesnot match!!")

    return render_template("login.html")


@app.route("/get_categories")
def get_categories():
    categories = mongo.db.categories.find()
    return render_template("", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
