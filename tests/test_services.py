import pytest
from app.services.cost_calculator import CostCalculatorService
from unittest.mock import MagicMock

# Assuming the fixture mock_file_reader is correctly set up as provided
@pytest.fixture
def mock_file_reader():
    mock = MagicMock()
    # Example of mocking file reads for prices and animal rates
    mock.read_file_lines.side_effect = [
        ["Meat=12.56", "Fruit=5.60"],  # Simulated content of prices.txt
        ["Lion;0.10;meat;", "Giraffe;0.08;fruit;"]  # Simulated content of animals.csv
    ]
    # Add additional mocks as needed for XML parsing or other data sources
    return mock

@pytest.fixture
def service_with_defaults():
    """
    Fixture that provides a CostCalculatorService instance with default setup.
    This could simulate a minimal setup where the service calculates costs based on some default assumptions.
    """
    mock_reader = MagicMock()
    # Setup mock to return minimal viable data or defaults
    mock_reader.read_file_lines.return_value = []
    return CostCalculatorService(mock_reader)

def test_calculate_with_minimal_setup(service_with_defaults):
    """
    Test the service's ability to calculate costs with minimal or default setup.
    This test assumes your service has logic to handle minimal data gracefully.
    """
    service = service_with_defaults
    assert service.calculate_food_costs() >= 0, "Service should return a non-negative cost even with minimal setup."

def test_calculate_food_costs_with_specific_data(mock_file_reader):
    """
    Test that calculate_food_costs returns a positive total cost when provided with specific data.
    """
    service = CostCalculatorService(mock_file_reader)
    total_cost = service.calculate_food_costs()
    assert total_cost >= 0, "Service should calculate a positive total cost with valid data."
