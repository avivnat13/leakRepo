import os
import base64
import json

# Hardcoded secrets (Vulnerability)
API_KEY = "sk_test_1234567890abcdef"  # Mock Stripe API Key
API_KEY1 = "sk_test_1234567890abcdef"  # Mock Stripe API Key
DB_PASSWORD = "SuperSecret123!"  # Mock Database Password
SECRET_KEY = "MyS3cr3tK3y"  # Mock Flask Secret Key
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # Mock AWS Access Key
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Mock AWS Secret Key
print("hello")
# Simulate storing secrets in an insecure JSON file
mock_secrets = {
    "api_key": API_KEY,
    "db_password": DB_PASSWORD,
    "secret_key": SECRET_KEY,
    "aws_access_key": AWS_ACCESS_KEY,
    "aws_secret_key": AWS_SECRET_KEY,
}

with open("config.json", "w") as f:
    json.dump(mock_secrets, f)

print("Sensitive config.json file created with mock secrets.")

# Function with insecure encoding
def encode_data(data):
    return base64.b64encode(data.encode()).decode()  # Encoding without encryption

# Store sensitive data in base64 (weak obfuscation)
encoded_db_password = encode_data(DB_PASSWORD)
print(f"Encoded DB Password (Base64): {encoded_db_password}")

# Function to retrieve secrets from environment variables (but with hardcoded fallback)
def get_secret(key, default=None):
    return os.getenv(key, default)

# Insecure use of fallback values
db_password = get_secret("DB_PASSWORD", "default_password123")
print(f"Retrieved DB Password: {db_password}")

# Simulated command injection vulnerability
def delete_user(user_id):
    os.system(f"rm -rf /home/users/{user_id}")  # No input sanitization (Dangerous)

# Simulated API endpoint with hardcoded API key
def access_protected_resource():
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # Hardcoded API key in headers
    }
    print(f"Accessing protected resource with headers: {headers}")

# Running functions for testing
delete_user("1234")  # Simulate a dangerous function call
access_protected_resource()
