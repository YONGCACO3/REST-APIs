# Flask REST API

This project is a REST API developed using Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy. It is designed to allow users to interact with and manage stores, items, tags, and user accounts. Additionally, it features JWT token-based authentication for secure access.

## Deployment and Access

The API is containerized using Docker, ensuring easy deployment and scalability. It is currently deployed and accessible at:

- **API Endpoint**: [https://rest-api-jiayong.onrender.com](https://rest-api-jiayong.onrender.com)

- **Swagger UI**: [https://rest-api-jiayong.onrender.com/swagger-ui](https://rest-api-jiayong.onrender.com/swagger-ui)

  This UI provides an interactive way to explore and test the API's capabilities.
![Store API](/Store_API.jpg "Screenshot of the Swagger UI")
**Note**: The server may take up to 20 seconds to restart if no requests have been sent to the API for a while.


## Installation

Clone the repository and navigate into the directory:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Install the required packages:
pip install -r requirements.txt

