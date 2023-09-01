from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)


# Rendering LogIn paage

@app.route("/")
def login():
	return render_template("index.html")

# Rendering SignUp page

@app.route("/signUp")
def signUp():
     return render_template("signup.html")


# Function to authenticate login form 

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("./static/json/data.json") as json_file:
        users = json.load(json_file)
        print(users)
    
    authenticated_user = next((user for user in users if user["username"] == username and user["password"] == password), None)

    if authenticated_user:
        return render_template("dashboard.html", name=username)
    else:
        return render_template("error.html")


# Function to get and add Sign up details to database
@app.route('/register', methods=['POST'])
def register():
     username = request.form.get('username')
     email = request.form.get('email')
     password = request.form.get('password')
     confirmPassword = request.form.get('confirmPassword')
     
     newUser = dict()

     if (password == confirmPassword and len(password) > 0 and len(confirmPassword) > 0):
          with open("./static/json/data.json", 'r') as json_file:
                users = json.load(json_file)
                newUser["username"] = username
                newUser["password"] = password

                users.append(newUser)
          with open("./static/json/data.json", 'w') as json_file:
                    json.dump(users, json_file, indent=4)
          return redirect('/')
     else:
           return render_template("error.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
