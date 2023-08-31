from flask import Flask, render_template, request
import json
import variable1
import variable2

app = Flask(__name__)



@app.route("/")
def login():
	return render_template("index.html")


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("./static/data.json") as json_file:
        users = json.load(json_file)
    
    authenticated_user = next((user for user in users if user["username"] == username and user["password"] == password), None)

    if authenticated_user:
        return "Authentication successful!"
    else:
        return "Authentication failed. Please check your credentials."



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
