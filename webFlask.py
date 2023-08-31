from flask import Flask, render_template, request
import json


app = Flask(__name__)



@app.route("/")
def login():
	return render_template("index.html")

@app.route("/signUp")
def signUp():
     return render_template("signup.html")

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("./static/json/data.json") as json_file:
        users = json.load(json_file)
    
    authenticated_user = next((user for user in users if user["username"] == username and user["password"] == password), None)

    if authenticated_user:
        return render_template("dashboard.html", name=username)
    else:
        return render_template("error.html")



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
