from .services.file_reader import FileReaderService
from .services.cost_calculator import CostCalculatorService


def get_file_reader_service() -> FileReaderService:
    """
    Creates and returns an instance of FileReaderService.

    This function serves as a factory for creating FileReaderService instances,
    allowing for centralized configuration and instantiation of the file reader service
    used throughout the application.

    Returns:
        An instance of FileReaderService.
    """
    return FileReaderService()

def get_cost_calculator_service() -> CostCalculatorService:
    """
    Creates and returns an instance of CostCalculatorService with a FileReaderService dependency.

    This function first creates an instance of FileReaderService, then uses it to instantiate
    and return a CostCalculatorService. This pattern of dependency injection simplifies testing
    and changing dependencies of the CostCalculatorService.

    Returns:
        An instance of CostCalculatorService configured with a FileReaderService.
    """
    file_reader_service = get_file_reader_service()  # Instantiate the FileReaderService
    return CostCalculatorService(file_reader_service)  # Return CostCalculatorService with the dependency injected
