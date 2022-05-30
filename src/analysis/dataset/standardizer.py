"""Utility functions used to standardize the dataset."""


def standardize_colname(col_name: str) -> str:
    """
    Returns the standard column name given a non-standard column name.
    :param col_name: the column name to standardize.
    :return: a string object
    """
    # removing all spaces
    std_colname = col_name.replace(" ", "")
    return std_colname.upper()
