from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rendqgrljvlgid:9906c2c45fd1ea7cc41b98084b3a7cf650436fca86985ac15574075bc3728515@ec2-54-83-44-4.compute-1.amazonaws.com:5432/d1h0n2hj61u431"#Heroku URI goes here

heroku = Heroku(app)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = "books" #creating a table for all our information
    id = db.Column(db.Integer, primary_key=True) #each column has a different component from the info
    title = db.Column(db.String(120))
    author = db.Column(db.String)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return "<Title %r>" % self.title #the %r means that anything after the second % will get place there
        #a different way of doing f"Title {self.title}"


@app.route("/")
def home():
    return"<h1>Hi from Flask</h1>"

@app.route("/book/input", methods=["POST"])
def books_input():
    if request.content_type == "application/json":
        post_data = request.get_json()
        title = post_data.get("title")
        author = post_data.get("author")
        reg = Book(title, author)
        db.session.add(reg)
        db.session.commit()
        return jsonify("Data Posted")
    return jsonify("Something went wrong") #functions as an else

@app.route("/books", methods=["GET"])
def return_books():
    all_books = db.session.query(Book.id, Book.title, Book.author).all()
    return jsonify(all_books)

if __name__ == "__main__":
    app.debug = True
    app.run()

    # pipenv install
    # pipenv install flask
    # pipenv install gunicorn
    # pipenv install flask-heroku
    # pipenv install flask-cors  #turns off cors for this app
    # pipenv install psycopg2  
        #to work with a postgress database 
        #attach a cloudbase database to the app
    # pipenv install flask-SQLAlchemy 
        #help us work with databases and let us work with shortcuts


    # git init
    # git add .
    # git commit -m "pre heroku push"
    # git status
    # git remote
        # no remote locations yet
    # heroku create book-api-practice
        # if already taken then put initials in front

        #add Procfile and push up again(don't have to do it because I already created Procfile)

    #we have not pushed up to heroku
    # go to resorces in your pushed up app
    # hit add ons and find Heroku Postgres
        # it will open a window that will allow us to look at our site
    # copy the database URI(settings)
    # in the application add between the qotes on Line 9: app.config["SQLALCHEMY_DATABASE_URI"] = ""


    # in python you can write
        # >>>from app import db
        # >>>db.create_all()
    #exit python

    # python app.py

    # open postman
        # POST (URL)
        # body
        # JSON(Application/json)

        # {
        #    " title": "The Lord of the Rings",
        #    "author": "J.R.R. tolken"
        # }

        # click send and refresh