The web application is designed to securely access and manage Electronic Health Records (EHR) using a robust security framework. Authentication is based on hash functions, implemented through a secure login page. Role-Based Access Control (RBAC) is enforced, following the principle of least privilege upon successful authentication. All access to and modifications of EHR data are logged, ensuring transparency and traceability. Integrity checks on both EHR data and audit logs are conducted using SHA-256 hashes, guaranteeing the data remains unaltered. The application employs a combination of AES-256 and RSA encryption for secure data transmission between components and for data storage. Additionally, comprehensive documentation detailing the system's architecture and functionality is provided.

The 3 main programs are:
1. Login.py:
This program serves as the authentication server for the web application. It is the first program that runs when the application is accessed, managing user authentication and session control. Upon accessing the application, users are presented with a login page where they enter their credentials. The program hashes passwords using SHA-256 to ensure secure storage and comparison. It verifies user credentials against stored hashes, and upon successful authentication, it directs users to the appropriate dashboard (admin, doctor, or patient) based on their role. It also handles session management, ensuring that authenticated users can navigate through the application securely. Additionally, it logs users out by clearing their session cookies and redirects them to the login page.

2. Query.py:
This program operates as the query server, responsible for handling user requests after they have been authenticated by the Login.py program. It allows users to perform various operations based on their roles, such as querying EHR records, viewing audit logs, adding comments to EHR data, or deleting comments from EHR data. The program ensures secure communication with the audit server by using RSA and AES encryption for data transmission. It also logs each query and modification to ensure accountability and maintain the integrity of the audit trail.

3. Audit.py:
This program functions as the audit server, responsible for maintaining and securing the audit logs of the application. It records every access, modification, addition, or deletion made to the EHR data. The program uses cryptographic methods to ensure the integrity of the audit records, including hashing with SHA-256 and encrypting the audit files. It verifies the integrity of audit records by comparing hashes and re-encrypts the audit files after logging events. This ensures that any unauthorized tampering with the audit records is detected and prevented, thereby maintaining a secure and trustworthy audit trail.
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
