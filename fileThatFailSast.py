import os
import sqlite3
import hashlib

# 🚨 Hardcoded credentials (Bad Practice)
USERNAME = "admin"
PASSWORD = "password123"  # Hardcoded password

def insecure_sql_query(user_input):
    """🚨 SQL Injection vulnerability"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 🚨 Directly injecting user input into SQL (Unsafe)
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

def insecure_command_execution(user_input):
    """🚨 Command Injection vulnerability"""
    os.system("echo " + user_input)  # 🚨 User input is not sanitized

def insecure_hashing(password):
    """🚨 Weak hashing method (MD5)"""
    return hashlib.md5(password.encode()).hexdigest()  # 🚨 MD5 is weak and outdated

if __name__ == "__main__":
    # Example usage
    print("Insecure script running...")

    user = input("Enter username: ")
    print(insecure_sql_query(user))

    command = input("Enter a command to execute: ")
    insecure_command_execution(command)

    weak_hash = insecure_hashing(PASSWORD)
    print("Weak password hash:", weak_hash)
