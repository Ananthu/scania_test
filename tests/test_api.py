import requests
from unittest.mock import patch

BASE_URL = "http://127.0.0.1:8000"  # Adjust this as necessary

def trigger_service_failure():
    """Function to simulate service failure."""
    raise Exception("Service Failure")

def test_food_costs_success():
    """Test successful retrieval of food costs."""
    response = requests.get(f"{BASE_URL}/zoo/food_costs")
    assert response.status_code == 200
    assert isinstance(response.json()["total_food_cost"], float)

def test_invalid_endpoint():
    """Test response for a non-existent endpoint."""
    response = requests.get(f"{BASE_URL}/zoo/invalid_endpoint")
    assert response.status_code == 404

# Mocking with requests approach is not directly feasible
# because requests makes real HTTP calls to your running application.
# To test failure, you would need to simulate the failure condition within the application itself,
# or adjust the application's state if possible before making the request.
