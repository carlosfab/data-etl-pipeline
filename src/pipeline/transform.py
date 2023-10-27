"""This module contains functions for transforming data in a pipeline."""

# FILEPATH: /Users/carlos/Projects/data-project/src/pipeline/transform.py
# --- Imports ---
from typing import List

import pandas as pd


def transform_to_single_dataframe(
    data_frame_list: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    Transform a list with DataFrames into a single DataFrame.

    Parameters:
    - data_frame_list (List[pd.DataFrame]): List of DataFrames to concatenate.

    Returns:
    - pd.DataFrame: A single concatenated DataFrame.
    """
    single_dataframe = pd.concat(data_frame_list, ignore_index=True)
    return single_dataframe
