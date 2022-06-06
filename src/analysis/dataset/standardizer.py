"""Utility functions used to standardize the dataset."""
import pandas as pd


def standardize_colname(col_name: str) -> str:
    """
    Returns the standard column name given a non-standard column name.
    :param col_name: the column name to standardize.
    :return: a string object
    """
    # removing all spaces
    std_colname = col_name.replace(" ", "")
    return std_colname.upper()


def standardize_patients_name(df: pd.DataFrame, disease_col_name: str = 'DISEASE') -> None:
    """
    Standardize the name of the patients. The sample will be <DISEASE_NAME>_<INDEX>
    :param df: dataframe
    :param disease_col_name: the disease colname
    :return: None
    """
    new_index_names = []
    rows, _ = df.shape
    last_disease = df.loc[0, disease_col_name]
    j = 0

    for i in range(rows):
        disease = df.loc[i, disease_col_name]
        if last_disease != disease:
            last_disease = disease
            j = 0
        else:
            j += 1

        new_index_names.append(disease + '_' + str(j))

    df.set_axis(new_index_names, axis='rows', inplace=True)
