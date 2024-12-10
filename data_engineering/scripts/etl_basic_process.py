import pandas as pd
from typing import Any


def extract(file_path: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file to be extracted.

    Returns:
        pd.DataFrame: The data extracted from the CSV file.
    """
    return pd.read_csv(file_path)


def transform(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the extracted data by performing necessary operations
    (e.g., removing missing values, renaming columns, etc.).

    Args:
        data (pd.DataFrame): The data to be transformed.

    Returns:
        pd.DataFrame: The transformed data.
    """
    # Example transformation: removing rows with any missing values
    transformed_data = data.dropna()
    return transformed_data


def load(data: pd.DataFrame, destination_path: str) -> None:
    """
    Loads the transformed data into a destination CSV file.

    Args:
        data (pd.DataFrame): The data to be loaded into the destination.
        destination_path (str): The path where the transformed data should be saved.

    Returns:
        None
    """
    data.to_csv(destination_path, index=False)


def run_etl(file_path: str, destination_path: str) -> None:
    """
    Runs the full ETL process (Extract, Transform, Load).

    Args:
        file_path (str): The source file path for extraction.
        destination_path (str): The destination file path to load transformed data.

    Returns:
        None
    """
    # Extract
    extracted_data = extract(file_path)

    # Transform
    transformed_data = transform(extracted_data)

    # Load
    load(transformed_data, destination_path)


if __name__ == "__main__":
    source_file = "source_data.csv"  # Replace with your source file path
    destination_file = "transformed_data.csv"  # Replace with your desired destination file path

    # Run the ETL process
    run_etl(source_file, destination_file)
