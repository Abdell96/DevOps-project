# Flask App - DevOps Project Template

This repository serves as a template for a simple Flask-based DevOps project. The app provides basic calculator functionalities (addition and subtraction) and includes all necessary files for setting up a local environment, running tests, and deploying to a cloud service with best practices in DevOps.

## Project Structure

The repository is organized as follows:

```plaintext
HEALTH-CALCULATOR-SERVICE/
├── app.py
├── health_utils.py
├── test.py
├── requirements.txt
├── Makefile
├── Dockerfile
├── templates/
│   └── home.html
├── .env
├── .gitignore
```

### File Descriptions

- **`app.py`**: The main application file for the Flask app. It sets up routes and connects them to functions in `utils.py` to provide API endpoints for app operations.

- **`utils.py`**: Contains utility functions for core operations like addition and subtraction. This file is designed to house the main logic for the app’s functionality.

- **`test.py`**: A unit test file that includes tests for the functions defined in `utils.py`. This file ensures that the core functionality behaves as expected.

- **`requirements.txt`**: Lists the Python dependencies needed to run the application. This file is used to install the necessary packages in the project environment.

- **`Makefile`**: A makefile to streamline project setup and operations. Includes commands for:
  - `make init`: Install project dependencies.
  - `make run`: Start the Flask app.
  - `make test`: Run all unit tests.

- **`templates/home.html`**: HTML template for the app's user interface. This file provides input fields and buttons for interacting with the calculator operations.

- **`.env`**: A configuration file for environment variables. It’s used to securely store sensitive information (like API keys, database credentials, or environment-specific settings). **Note**: This file should not be committed to version control for security reasons.

- **`.gitignore`**: Specifies files and directories that should be ignored by Git. It typically includes files such as `.env` and compiled Python files (`__pycache__`), as well as local environment and dependency caches.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd DEVOPS-PROJECT
   ```

2. **Set Up the Environment**:
   - Create and activate a virtual environment (recommended for managing dependencies).
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

This template was created by **Ali Mokh** and is intended as an educational resource for DevOps projects involving Flask applications.

## License and Usage

This project template is open to use by anyone and may be freely adapted for personal or professional projects. If you use this template as part of teaching materials or educational content, please cite **Ali Mokh** as the original author.

