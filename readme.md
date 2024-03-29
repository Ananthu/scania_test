# FastAPI Zoo Food Cost Calculator Service

## Overview

This FastAPI service provides an API to calculate the total food cost for animals in a zoo. It reads animal data and food prices from files, performs calculations based on dietary needs and current prices, and offers endpoints to retrieve calculated costs.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- FastAPI
- Uvicorn

### Installation

Clone the repository

```bash
git clone https://github.com/Ananthu/scania_test.git
cd scania_test
```

### Install dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt

```

### Project Structure

```
├── app
│   ├── __init__.py
│   ├── dependencies.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   └── zoo_api.py
│   ├── models
│   │   ├── __init__.py
│   │   └── entities.py
│   └── services
│       ├── __init__.py
│       ├── cost_calculator.py
│       └── file_reader.py
├── input_files
│   ├── animals.csv
│   ├── prices.txt
│   └── zoo.xml
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_services.py
└── requirements.txt

```
This structure is designed to separate concerns, making the application modular and maintainable. The app directory contains the application code, including endpoints (api), business logic (services), and data models (models). The input_files directory contains static files that the application uses for data, and the tests directory contains tests for ensuring the application works as expected.

# Running the Application
To run the application on your local development server, use Uvicorn with the following command:

```
uvicorn app.main:app --reload

```
The --reload option enables auto-reload so the server will restart after code changes. This is useful during development.

The application will be available at http://127.0.0.1:8000. You can access the automatic API documentation provided by FastAPI at http://127.0.0.1:8000/docs.

# Testing
This project includes tests to ensure the functionality works as expected. To run the tests, execute the following command:

```
pytest

```
Make sure you're in the project root directory when you run this command. pytest will automatically find and run all tests within the tests directory.