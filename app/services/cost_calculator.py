from typing import Dict
from .file_reader import FileReaderService  # Ensure relative import matches your project structure
from functools import lru_cache
import csv

class CostCalculatorService:
    """
    A service class for calculating the total cost of food required for animals in a zoo.

    This service utilizes a FileReaderService to read animal dietary requirements and current food prices
    from external files and then calculates the total cost based on these inputs.

    Attributes:
        file_reader (FileReaderService): An instance of FileReaderService for accessing file data.
    """

    def __init__(self, file_reader: FileReaderService):
        """
        Initializes the CostCalculatorService with a FileReaderService instance.

        Args:
            file_reader (FileReaderService): The file reader service used to access dietary and price data.
        """
        self.file_reader = file_reader

    @lru_cache(maxsize=32)
    def get_prices(self) -> Dict[str, float]:
        """
        Retrieves and caches the current prices of food items from an external file.

        Returns:
            A dictionary mapping food items (str) to their prices (float).
        """
        lines = self.file_reader.read_file_lines('./input_files/prices.txt')
        return {line.split('=')[0]: float(line.split('=')[1].strip()) for line in lines}

    @lru_cache(maxsize=32)
    def get_animal_rates(self) -> Dict[str, dict]:
        """
        Retrieves and caches the dietary requirements of animals from an external file.

        Returns:
            A dictionary where each key is an animal species (str) and each value is another
            dictionary containing 'rate' (float), 'type' (str), and 'meat_percentage' (float, optional).
        """
        lines = self.file_reader.read_file_lines('./input_files/animals.csv')
        animals = {}
        for line in csv.reader(lines, delimiter=';'):
            if len(line) < 3:  # Basic validation to skip malformed lines
                continue
            animals[line[0]] = {
                'rate': float(line[1]),
                'type': line[2],
                'meat_percentage': float(line[3].replace('%', ''))/100 if len(line) > 3 and line[2] == 'both' else None
            }
        return animals

    def calculate_food_costs(self) -> float:
        """
        Calculates the total cost of food required for all animals in the zoo.

        This calculation uses the dietary requirements of each animal species, their weight,
        and the current prices of meat and fruit to compute the total cost.

        Returns:
            The total cost (float) of feeding all animals.
        """
        prices = self.get_prices()
        animals = self.get_animal_rates()
        root = self.file_reader.parse_xml_file('./input_files/zoo.xml')

        total_cost = 0
        for animal_group in root:
            for animal in animal_group:
                species = animal.tag
                if species not in animals:
                    continue
                weight = float(animal.attrib['kg'])
                rate = animals[species]['rate']
                food_type = animals[species]['type']
                meat_percentage = animals[species].get('meat_percentage', 0)

                if food_type == 'meat':
                    cost = weight * rate * prices['Meat']
                elif food_type == 'fruit':
                    cost = weight * rate * prices['Fruit']
                else:  # for omnivores
                    cost = weight * rate * (meat_percentage * prices['Meat'] + (1 - meat_percentage) * prices['Fruit'])
                
                total_cost += cost

        return total_cost
