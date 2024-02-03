# Flask REST API

This project is a REST API developed using Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy. It is designed to allow users to interact with and manage stores, items, tags, and user accounts. Additionally, it features JWT token-based authentication for secure access.

## Deployment and Access

The API is containerized using Docker, ensuring easy deployment and scalability. The Dockerized API is hosted on Render.com and it is currently deployed and accessible at:

- **API Endpoint**: [https://rest-api-jiayong.onrender.com](https://rest-api-jiayong.onrender.com)

- **Swagger UI**: [https://rest-api-jiayong.onrender.com/swagger-ui](https://rest-api-jiayong.onrender.com/swagger-ui)

  This UI provides an interactive way to explore and test the API's capabilities.
![Store API](/Store_API.jpg "Screenshot of the Swagger UI")
**Note**: The server may take up to 50 seconds to restart if no requests have been sent to the API for a while.
  

## User Guide

1. ### Registration

**Send a POST request to the registration endpoint**

   The registration endpoint is `https://rest-api-jiayong.onrender.com/register`.
   The request body should be a JSON object that includes the new user's details. For example:

   ```json
   {
       "username": "Your_user_name",
       "email": "Your_email",
       "password": "Your_password"
   }
   ```
   If the registration is successful, you'll receive a response "User created successfully."
   
2. ### Login and get tokens 
**Send a POST request to the registration endpoint**

The login endpoint is t `https://rest-api-jiayong.onrender.com/login`.
The request body is the same as in the registration endpoint.
   ```json
   {
       "username": "Your_user_name",
       "email": "Your_email",
       "password": "Your_password"
   }
   ```
   If the authentication is successful, you will receive a response containing two JWT tokens: an access token for authorizing subsequent API requests and a refresh token for renewing authentication when needed.

3. ### Use the token to interact with the Store, Item, and Tag endpoints..
**Include the JWT token in the Authorization header**
   
   For subsequent requests to the API, include the JWT token in the Authorization header. The header should look something like this:
   ``` bash
   Authorization: Bearer your-jwt-token
   ```
   Replace your-jwt-token with the actual token you received from the authentication endpoint.
   

## Database

The API initially used a local SQLite database for development, but it was later migrated to ElephantSQL, a fully managed PostgreSQL database hosting service that operates on AWS, for more robust and scalable performance. 

## Future Work

In the future, my goal is to develop a frontend UI for users to interact with the API. This will make the API more accessible to non-technical users and allow them to take advantage of the functionality it provides.

Additionnaly, I plan to add more features to the API, such as advanced filtering and sorting options, and to improve the API's performance and scalability.



## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


```
2. **Set up a virtual environment (optional)**
   
   It's recommended to use a virtual environment to isolate the project dependencies. You can create a virtual environment using the following command:
   ```bash
   python3 -m venv env
   ```
  
4. **Install the dependencies**

   Use the following command to install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. **Set up the database**
   
   Update the DATABASE_URL in the .env file with your database credentials.

6. **Build the Docker image**
   Build the Docker image using the Dockerfile provided in the repository:
   ```bash
   docker build -t your-image-name .
   ```
   Replace your-image-name with the name you want to give to your Docker image.

7. **Run the Docker container**

   Run the Docker container from the image you just built:
   ```bash
   docker run -p 5000:5000 your-image-name
   ```
   The application will start running at http://127.0.0.1:5000.
   

Please note that these instructions are for a basic setup. Depending on your environment and the configuration of your machine, you might need to adjust these instructions.
   

