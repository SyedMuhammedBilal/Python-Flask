from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from app import db
from flask_pymongo import PyMongo
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)   # object
#print(__name__)

app.config["MONGO_URI"] = "mongodb+srv://SyedMuhammed:rb26dettrb30@cluster0-0glm6.gcp.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
#print(mongo)


#client = MongoClient("localhost",27017)
#database = client["my_database"]
#print("Connection Successful")
#client.close()
#db = client.test

#a = list(range(11))

@app.route("/")         # .com/ ("/") will return same
def index():            # decorater for the page
	return """
	<h1>Welcome to my first page</h1>
	<p>what else can we help you?</p>
	<a href="/signup">Signup</a>
	<a href="/login">Login</a>
	"""

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#@app.route("/login/<name>")
#def login(name):                     # ("{}") in html to show in website
	#return "Hello login page "+ name

@app.route('/signupAuth', methods=["POST"])
def signupAuth():
    data = dict(request.form)
    print(data)
    usersData = mongo.db.usersData
    result = usersData.find_one({"email": data['email']})
    print(result)
    if(result):
        return redirect('/signup')
    # for i in result:
    #     print(i)
    bcrypt_password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt(12))
    data['password'] = bcrypt_password
    usersData.insert_one(data)
    return redirect('/login')

@app.route("/index")
def html_index():
	return render_template("index.html")

@app.route("/home")
def home():
	return """
    <font size="5">
    	<body bgcolor="#183620">
	<center><font color="blue">WELCOME TO HOME PAGE</font></center>
	"""

@app.route('/loginAuth', methods=["POST"])
def loginAuth():
    data = dict(request.form)
    usersData = mongo.db.usersData
    findEmail = usersData.find_one({"email": data['email']})
    if(findEmail):
        checkPassword = bcrypt.checkpw(data['password'].encode('utf8'), findEmail['password'])
        if(checkPassword):
            return redirect('/home')
        return redirect('/login')
    return redirect('/login')

users = [
{
	"Email":"bilal",
	"password":"123"
},
{
	"Email":"mani",
	"password":"456"
},
{
	"Email":"abdulrehman",
	"password":"246"
},
{
	"Email":"fatima",
	"password":"26"
},
{
	"Email":"ayesha",
	"password":"000"
},
{
	"Email":"rumaisa",
	"password":"666"
},
{
	"Email":"areeb",
	"password":"789"
},
{
	"Email":"ahmed",
	"password":"ahmx"
},
{
	"Email":"junaid",
	"password":"777"
},
{
	"Email":"shayan",
	"password":"999"
},
{
	"Email":"ahsan",
	"password":"444"
}]

@app.route("/auth", methods=["POST"])  # adding method in app.route so, you should write (methods=["POST"]) in python
def auth():                            # and write (method=["POST"]) in HTML.
	print("===========")
	print(request.form)
	print("===========")
	data = request.form
	for i, v in enumerate(users):
		if (data["Email"] == v["Email"] and data["password"] == v["password"]):
			return redirect("/home")
	else:
		return redirect("/login")

if __name__ == "__main__":
	app.run(debug=True, port=5001)   # to run a localhost
	                                    # 27017 MongoDB port
