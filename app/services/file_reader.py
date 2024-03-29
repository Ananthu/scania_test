from fastapi import HTTPException
import csv
import xml.etree.ElementTree as ET

class FileReaderService:
    """
    Provides functionality for reading and parsing files used by the application.
    
    This service is responsible for abstracting away the file reading and XML parsing operations,
    providing a clean interface for other parts of the application to access file data.
    """

    @staticmethod
    def read_file_lines(filename: str) -> list:
        """
        Reads all lines from a specified file and returns them as a list.

        Args:
            filename (str): The path to the file to be read.

        Returns:
            list: A list of strings, each representing a line in the file.

        Raises:
            HTTPException: If the file is not found, or another error occurs during file reading.
        """
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"{filename} not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading {filename}: {str(e)}")

    @staticmethod
    def parse_xml_file(filename: str) -> ET.Element:
        """
        Parses an XML file and returns its root element.

        Args:
            filename (str): The path to the XML file to be parsed.

        Returns:
            ET.Element: The root element of the parsed XML tree.

        Raises:
            HTTPException: If the XML file cannot be found, cannot be parsed, or another error occurs.
        """
        try:
            tree = ET.parse(filename)
            return tree.getroot()
        except ET.ParseError:
            raise HTTPException(status_code=500, detail="Error parsing the XML file.")
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="XML file not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while parsing XML file: {str(e)}")
