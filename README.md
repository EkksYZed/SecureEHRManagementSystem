To run this project/web application, follow these steps:

### Prerequisites:
1. **Python:** Ensure Python is installed on your system.
2. **Dependencies:** Install the required Python libraries, such as Flask and Cryptography.

### Steps to Run the Application:

1. **Clone or Download the Project:**
   - Place the project files (e.g., `Login.py`, `Query.py`, `Audit.py`, and any HTML templates) into a directory on your system.

2. **Generate Cryptographic Keys:**
   - Run the key generation scripts to generate RSA and AES keys.
   - Store the keys securely in the designated files and directories within your project.

3. **Start the Authentication Server:**
   - Execute the `Login.py` script to start the Flask web server. This will handle user authentication and session management.

4. **Start the Query Server:**
   - Run the `Query.py` script in a separate terminal to handle EHR queries.

5. **Start the Audit Server:**
   - Run the `Audit.py` script in another terminal to manage audit logs.

6. **Access the Application:**
   - Open a web browser and navigate to the local server's address (e.g., `http://localhost:5000/`) to access the login page.
   - Log in with your credentials, and based on your role, you will be redirected to the appropriate dashboard.

7. **Perform Operations:**
   - Use the application to query EHR records, view audit logs, add comments, or delete comments as per your role.

8. **Logout:**
   - After completing your tasks, log out to end the session and secure your access.

### Notes:
- Ensure all servers (`Login.py`, `Query.py`, `Audit.py`) are running concurrently for the application to function correctly.
- Modify the configuration files or scripts as needed to fit your specific environment or use case.
