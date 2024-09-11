Getting Started
Prerequisites
Docker (make sure Docker is installed on your machine)
Docker Compose
Python 3.9 or higher (for local development)
Installation
Clone the repository:

bash

git clone https://github.com/your-repo/task-management-microservices.git
cd task-management-microservices
Install dependencies:

For Python services (UserService, TaskService):
bash

cd UserService
pip install -r requirements.txt
For the UI Microservice:
bash

cd UIMicroservice/frontend
pip install -r requirements.txt
Running the Project
You can run the entire application using Docker Compose.

Build and start the services:

bash

docker-compose up --build
To shut down the services:

bash

docker-compose down
All the services (UserService, TaskService, NotificationService, UI Microservice, Prometheus, Loki) will be running, and you can access the UI on http://localhost:8000.

Prometheus Metrics
Prometheus is set up to scrape metrics from the Django services. Each service has custom metrics exposed via the /metrics endpoint.
