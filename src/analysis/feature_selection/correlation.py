import pandas as pd
import numpy as np


def compute_correlation(df: pd.DataFrame) -> None:
    """
    This function is a utility function that uses correlation to perform feature selection.
    It's an experimental method.
    :parameter df: dataset
    """
    corr = df.corr()

    columns = np.full((corr.shape[0],), True, dtype=bool)
    for i in range(corr.shape[0]):
        for j in range(i + 1, corr.shape[0]):
            if corr.iloc[i, j] >= 0.9:
                if columns[j]:
                    columns[j] = False
    selected_columns = df.columns[columns]

    return selected_columns
