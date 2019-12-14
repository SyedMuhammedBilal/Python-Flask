from flask import Flask, render_template, redirect, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://SyedBilal:rb26dettrb30@mydatabase-9uq4l.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def index():
	return jsonify({"message": "Hello from 5001", "users": users})

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

#@app.route("/home")
#def home():
	#return """
    #<font size="5">
    	#<body bgcolor="#183620">
	#<center><font color="blue">WELCOME TO HOME PAGE</font></center>
	#"""

@app.route('/test', methods=["POST"])
def test():
    data = request.form
    data = dict(data)
    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            # login = mongo.db.login
            # result = login.insert_one(data)
            # print(result.inserted_id)
            return redirect('http://127.0.0.1:5000/home')
    return redirect('http://127.0.0.1:5000/login')

if __name__ == "__main__":
	app.run(debug=True, port=5001)