# Health Calculator Service

This repository contains a Flask-based service for calculating Body Mass Index (BMI) and Basal Metabolic Rate (BMR). The application is structured to follow DevOps best practices, providing a foundation for local development, testing, and deployment in a production-ready environment.

## Project Structure

The repository is organized as follows:

```plaintext
HEALTH-CALCULATOR-SERVICE/
├── .github/
│   └── workflows/
│       ├── ci.yaml               # GitHub Actions CI pipeline
│       └── main_app-python25.yml # Azure deployment workflow
├── app.py              # Flask REST API for BMI and BMR calculations
├── health_utils.py     # Utility functions for BMI and BMR logic
├── test.py             # Unit tests for the service
├── requirements.txt    # Python dependencies
├── Makefile            # Commands for managing the project
├── Dockerfile          # Docker configuration for containerizing the app
├── templates/
│   └── home.html       # HTML template for the web interface
├── .env                # Environment variables (excluded from version control)
├── .gitignore          # Files and directories ignored by Git

```

### File Descriptions

- **`app.py`**: Main Flask application file. It defines the REST API endpoints for calculating BMI and BMR, rendering templates, and handling requests.
- **`health_utils.py`**: Implements the core BMI and BMR calculation logic.
- **`test.py`**: Unit tests to verify the correctness of the BMI and BMR calculations.
- **`requirements.txt`**: Contains Python libraries needed to run the application.
- **`Makefile`**: Simplifies common development tasks:
    - `make init`: Install dependencies.
    - `make run`: Start the Flask server.
    - `make test`: Run unit tests.
**`Dockerfile`**: Specifies the environment for building and running the app in a Docker container.
- **`templates/home.html`**: Web interface for interacting with the BMI and BMR calculator.
- **`.env`**:  Stores environment variables (e.g., FLASK_DEBUG, PORT) for development and production settings.
- **`.gitignore`**: Lists files and directories to exclude from version control, such as .env and Python caches.

 Specifies files and directories that should be ignored by Git. It typically includes files such as `.env` and compiled Python files (`__pycache__`), as well as local environment and dependency caches.

## Makefile Commands
The Makefile provides the following commands for convenience:
| Command         | Description                                                              |
|-----------------|--------------------------------------------------------------------------|
| `make help`     | Display a list of available commands.                                    |
| `make init`     | Set up the environment and install dependencies.                         |
| `make install`  | Install Python dependencies from `requirements.txt`.                     |
| `make build`    | Build the Docker image.                                                  |
| `make rn`       | Run the Flask app locally.                                               |
| `make test`     | Run unit tests with `pytest`.                                            |
| `make test-api` | Test the API endpoints using `curl`. Requires the app to be running.     |
| `make clean`    | Remove Python cache files.                                               |
| `make docker-run` | Run the application in a Docker container.                            |
| `make docker-test` | Run unit tests inside the Docker container.                          |


## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abdell96/HEALTH-CALCULATOR-SERVICE.git
   cd health-calculator-service
   ```

2. **Set Up the Environment**:
   - Create and activate a virtual environment (recommended for managing dependencies).
   ```bash
   make init
   ```

3. **Run the Application**:
   - Start the Flask app locally:
     ```bash
     make run
     ```

4. **Run Tests**:
   - Execute unit tests to verify functionality:
     ```bash
     make test
     ```

##  Docker Setup

1. **Build the Docker Image**:

 ```bash
 make build
 ```

2. **Run the Application in Docker**:

```bash
make docker-run
```
3. **Test the Application in Docker**:

```bash
make docker-test
```

## Testing the API Endpoints
To test the API endpoints, you can use the following make test-api command, which will automatically run the tests for the BMI and BMR calculation endpoints. Ensure the app is running before running this command.

```bash
make test-api
```
This will run the following tests for the API endpoints:

  - Test BMI Calculation:

```bash
curl -X POST http://localhost:5000/bmi \
  -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70}'
```

  - Test BMR Calculation:

```bash
curl -X POST http://localhost:5000/bmr \
  -H "Content-Type: application/json" \
  -d '{"height": 175, "weight": 70, "age": 30, "gender": "male"}'
```

## Additional Notes

- Ensure the .env file contains any necessary environment-specific configurations.
- Use make clean to remove Python cache files to avoid conflicts during development.
- For deployment, adapt the Dockerfile and CI/CD pipeline configuration as needed.


## Deployment Instructions

## Continuous Integration and Deployment
GitHub Actions CI Pipeline
The project uses GitHub Actions for continuous integration, defined in .github/workflows/ci.yaml. The pipeline:

- Runs automated tests
- Performs code quality checks
- Builds the Docker container
- Ensures the application meets quality standards before deployment

## Azure Cloud Deployment
The application is deployed to Azure Cloud using the workflow defined in .github/workflows/main_app-python25.yml. This workflow:

- Automatically deploys to Azure App Service
- Manages the build and deployment process
- Ensures consistent deployment across environments

link to the app : [My-App-python25](https://app-python25-ehcpcchabwfkhzdx.francecentral-01.azurewebsites.net/)

## Author

This template was copied and updated by **Abdelillah Hemaz** and is intended as an educational resource for DevOps projects involving Flask applications.
