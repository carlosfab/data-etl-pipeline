# --- Import ---
import pandas as pd
import pytest
from src.pipeline.transform import transform_to_single_dataframe


def test_transform_to_single_dataframe():
    # --- Arrange ---
    df1 = pd.DataFrame({"A": [1, 2], "B": [10, 20]})
    df2 = pd.DataFrame({"A": [3, 4], "B": [30, 40]})
    df3 = pd.DataFrame({"A": [5, 6], "B": [50, 60]})
    data_frame_list = [df1, df2, df3]

    # --- Act ---
    result = transform_to_single_dataframe(data_frame_list)

    # --- Assert ---
    assert result.equals(
        pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 5, 6],
                "B": [10, 20, 30, 40, 50, 60],
            }
        )
    )
