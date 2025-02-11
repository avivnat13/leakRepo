public class InsecureSecrets {
    
    // 🚨 Hardcoded API Keys (Security Risk)
    private static final String AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE";
    private static final String AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

    // 🚨 Hardcoded Database Credentials (Security Risk)
    private static final String DB_USERNAME = "admin";
    private static final String DB_PASSWORD = "SuperSecret123";

    // 🚨 Hardcoded JWT Secret Key
    private static final String JWT_SECRET = "mySuperSecretJWTKeyDontShare";

    public static void main(String[] args) {
        System.out.println("WARNING: This file contains hardcoded secrets!");
        
        // Simulating the use of insecure secrets
        connectToDatabase(DB_USERNAME, DB_PASSWORD);
        authenticateAWS(AWS_ACCESS_KEY, AWS_SECRET_KEY);
    }

    private static void connectToDatabase(String username, String password) {
        System.out.println("Connecting to DB with username: " + username);
        // 🚨 Fake connection logic (imagine an actual database connection here)
    }

    private static void authenticateAWS(String accessKey, String secretKey) {
        System.out.println("Authenticating with AWS using Access Key: " + accessKey);
        // 🚨 Fake authentication logic
    }
}
