from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Demo username and password
USERNAME = "admin"
PASSWORD = "12345"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USERNAME and password == PASSWORD:
        return jsonify({
            "success": True,
            "message": "Login Successful!"
        })

    return jsonify({
        "success": False,
        "message": "Invalid Username or Password"
    })


if __name__ == "__main__":
    app.run(debug=True)