# --- Imports ---
import os
import glob
from typing import List
import pandas as pd


# --- Constants ---
# TODO

# --- Functions ---
def extract_from_excel(
        path: str
) -> List[pd.DataFrame]:
    """
    Extracts data from all Excel files in the specified directory.

    Parameters:
    - path (str): The directory path where the Excel files are located.

    Returns:
    - List[pd.DataFrame]: A list of dataframes extracted from the Excel files.
    """

    # Get all excel files
    excel_files = glob.glob(os.path.join(path, "*.xlsx"))

    # Read excel files
    dataframes = [pd.read_excel(file) for file in excel_files]

    return dataframes


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path="data/input")
