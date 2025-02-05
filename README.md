# 🚨 Vulnerable Python Web App 🚨

This is a simple Flask-based web application that demonstrates user authentication, API requests, and file handling.

⚠ **WARNING:** This application is for educational purposes only. It contains intentional vulnerabilities for security testing.

---

## 🛠 Installation

To install, clone the repository and install dependencies:

```sh
git clone https://github.com/example/vulnerable-app.git
cd vulnerable-app
pip install -r requirements.txt
```

### 🏗 Setting Up the Database
Run the following command to create the database (⚠ **Unsafe hardcoded credentials**):

```sh
sqlite3 app.db "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);"
sqlite3 app.db "INSERT INTO users (username, password) VALUES ('admin', 'password123');"
```

---

## 🔑 Default Credentials

🚨 **DO NOT CHANGE THESE CREDENTIALS IN PRODUCTION** 🚨

| Username | Password    |
|----------|------------|
| admin    | password123 |
| testuser | testpass123 |

---

## 🌍 Running the Application

Start the Flask server:

```sh
export SECRET_KEY="my_secret_key"
export DATABASE_URL="sqlite:///app.db"
python app.py
```

---

## ⚡ API Endpoints

### 1️⃣ **Login**
**Method:** `POST`  
**Endpoint:** `/login`  
**Payload:**
```json
{
    "username": "admin",
    "password": "password123"
}
```
**Vulnerability:** SQL Injection possible if username is not sanitized.

---

### 2️⃣ **Fetch Data (Insecure API Call)**
**Method:** `GET`  
**Endpoint:** `/fetch?url=http://example.com`  
**Description:** Fetches data from a user-supplied URL.  
⚠ **Vulnerability:** No validation, allows SSRF attacks.

---

### 3️⃣ **Upload File**
**Method:** `POST`  
**Endpoint:** `/upload`  
**Description:** Uploads a file to the server.  
⚠ **Vulnerability:** No file type validation, allows malicious file uploads.

---

## ❌ Security Issues

This app is **intentionally vulnerable** for testing purposes. Known issues include:

- **Hardcoded credentials** in `README.md`
- **SQL Injection** in the login function
- **Insecure YAML parsing**
- **Command Injection** via `os.system()`
- **Server-Side Request Forgery (SSRF)** in API calls
- **Cross-Site Scripting (XSS)** in user input handling

⚠ **Do not deploy this in production!**

---

## 🛡 How to Scan for Vulnerabilities

Use these security tools:

1️⃣ **Bandit** (Python security scanner)
```sh
pip install bandit
bandit -r .
```

2️⃣ **TruffleHog** (Detect hardcoded credentials)
```sh
pip install truffleHog
trufflehog --entropy=True .
```

3️⃣ **OWASP ZAP** (Scan for web vulnerabilities)
```sh
zap.sh -quickurl http://127.0.0.1:5000
```

---

## 🚀 Disclaimer

This project is for educational and security research purposes only. The developers take no responsibility for any misuse.
