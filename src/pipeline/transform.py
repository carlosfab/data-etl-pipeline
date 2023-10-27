# --- Imports ---
import pandas as pd
from typing import List


def transform_to_single_dataframe(
    data_frame_list: List[pd.DataFrame]
) -> pd.DataFrame:
    """
    Transform a list with DataFrames into a single DataFrame.

    Parameters:
    - data_frame_list (List[pd.DataFrame]): List of DataFrames to be concatenated.

    Returns:
    - pd.DataFrame: A single concatenated DataFrame.
    """

    single_dataframe = pd.concat(data_frame_list, ignore_index=True)
    return single_dataframe
