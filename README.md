# Health Calculator Service

This repository contains a Flask-based service for calculating Body Mass Index (BMI) and Basal Metabolic Rate (BMR). The application is structured to follow DevOps best practices, providing a foundation for local development, testing, and deployment in a production-ready environment.

## Project Structure

The repository is organized as follows:

```plaintext
HEALTH-CALCULATOR-SERVICE/
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

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd health-calculator-service
   ```

2. **Set Up the Environment**:
   - Create and activate a virtual environment (recommended for managing dependencies).
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   - Install the dependencies:
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

## Additional Configuration

- **Environment Variables**:
  - Use the `.env` file to store any environment-specific configurations or sensitive information. Be sure to keep this file out of version control by listing it in `.gitignore`.

## Deployment Instructions

For deployment, configure CI/CD pipelines according to your preferred platform (e.g., GitHub Actions, Azure Pipelines). This template can be used with cloud deployment platforms like AWS, Azure, or Heroku for easy scalability.
  - Use `pipeline.yaml` as a template for a pipeline to build and deploy an application on Azure

## Author

This template was copied and updated by **Abdelillah Hemaz** and is intended as an educational resource for DevOps projects involving Flask applications.
