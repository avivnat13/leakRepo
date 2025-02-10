# Mock credentials for testing purposes

MOCK_CREDENTIALS = {
    "username": "test_user",
    "password": "P@ssw0rd123",
    "api_key": "12345678-ABCD-1234-ABCD-1234567890AB",
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "db_user",
        "password": "db_password",
        "database": "test_db"
    },
    "email": {
        "smtp_server": "smtp.example.com",
        "port": 587,
        "email": "test@example.com",
        "email_password": "emailP@ss123"
    }
}


def get_mock_credentials():
    """Returns mock credentials for testing."""
    return MOCK_CREDENTIALS


if __name__ == "__main__":
    creds = get_mock_credentials()
    print("Mock credentials loaded for testing:")
    for key, value in creds.items():
        print(f"{key}: {value}")
