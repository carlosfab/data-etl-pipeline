# --- Imports ---
import pandas as pd


def load_to_excel(
        data_frame: pd.DataFrame,
        output_path: str,
        file_name: str
) -> None:
    """
    Load a DataFrame into an Excel file.

    Args:
        data_frame (pd.DataFrame): The DataFrame to be saved.
        output_path (str): Directory where the Excel file will be saved.
        file_name (str): Desired name for the Excel file (without extension).

    Returns:
        None: Just prints a confirmation message.
    """

    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    print(f'File saved successfully at {output_path}/{file_name}.xlsx')
    return None
