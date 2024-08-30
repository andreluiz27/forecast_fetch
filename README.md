
# Forecast data collector

This is a basic FastAPI application containerized with Docker. This API gets weather data from multiple cities and store in a mongodb database.

## Notes
  * Tests were done but for some reason is not working
  * The code could improve with some dependency injection
  * requirements.txt does not specify versions, this is never a good idea
  * Commits were pushed with sensitive data, because this is not a serious projects it's okay but in a real project this must not be done
    
## Prerequisites

Before you begin, ensure you have:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/andreluiz27/forecast_fetch.git
cd repository-name
```

### 2. Build and Run the Docker Container

```bash
docker-compose up --build
```

### 3. Access the Application

Open your browser and go to:

```
http://localhost:8000
```

### 4. API Documentation

You can access the automatically generated API documentation at:

- Swagger UI: [http://localhost:8989/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8989/redoc](http://localhost:8000/redoc)

## Stopping the Application

To stop the running containers:

```bash
docker-compose down
```

## Contributing


