from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3
import os
import pickle

app = Flask(__name__)

# Database setup (Unsafe)
conn = sqlite3.connect('vuln.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

# Hardcoded credentials (Vulnerability)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

@app.route("/")
def index():
    return "Welcome to the Vulnerable Web App!"

# SQL Injection vulnerability
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            return "Login successful!"
        else:
            return "Invalid credentials"

    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# XSS vulnerability
@app.route("/comment", methods=["GET", "POST"])
def comment():
    if request.method == "POST":
        user_input = request.form.get("comment")
        return render_template_string(f"<h1>User Comment:</h1> <p>{user_input}</p>")  # No escaping

    return '''
        <form method="POST">
            Comment: <input type="text" name="comment"><br>
            <input type="submit" value="Submit">
        </form>
    '''

# Insecure File Upload vulnerability
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join("uploads", file.filename))  # No validation on file type
    return f"File {file.filename} uploaded successfully!"

# Insecure Deserialization vulnerability
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.form.get("data")
    obj = pickle.loads(bytes.fromhex(data))  # Accepts arbitrary serialized objects
    return f"Deserialized object: {obj}"

# Command Injection vulnerability
@app.route("/ping", methods=["GET"])
def ping():
    ip = request.args.get("ip")
    result = os.system(f"ping -c 4 {ip}")  # No sanitization
    return f"Ping result: {result}"

if __name__ == "__main__":
    app.run(debug=True)
