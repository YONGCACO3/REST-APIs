# Flask REST API

This project is a REST API developed using Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy. It is designed to allow users to interact with and manage stores, items, tags, and user accounts. Additionally, it features JWT token-based authentication for secure access.

## Deployment and Access

The API is containerized using Docker, ensuring easy deployment and scalability. The Dockerized API is hosted on Render.com and it is currently deployed and accessible at:

- **API Endpoint**: [https://rest-api-jiayong.onrender.com](https://rest-api-jiayong.onrender.com)

- **Swagger UI**: [https://rest-api-jiayong.onrender.com/swagger-ui](https://rest-api-jiayong.onrender.com/swagger-ui)

  This UI provides an interactive way to explore and test the API's capabilities.
![Store API](/Store_API.jpg "Screenshot of the Swagger UI")
**Note**: The server may take up to 25 seconds to restart if no requests have been sent to the API for a while.

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
   

