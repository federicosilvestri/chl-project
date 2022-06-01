"""This file contains all the merging functions."""
import typing as tp
import pandas as pd
from .standardizer import standardize_colname


def compute_ds_col_intersection(datasets: tp.List[pd.DataFrame]) -> tp.List[str]:
    """
    This function computes the intersection of columns between all datasets.
    :param datasets: a list of dataframe
    :return: a list of colum name that are "shared" between all datasets.
    """
    list_of_cols: tp.List[str] = []

    for ds in datasets:
        col_name_list = ds.columns.values.tolist()
        list_of_cols.append([
            standardize_colname(col_name) for col_name in col_name_list
        ])

    intersection: tp.Set[str] = set.intersection(*map(set, list_of_cols))
    return list(intersection)


def clean_datasets(datasets: tp.List[pd.DataFrame], col_name: tp.List[str]) -> tp.List[pd.DataFrame]:
    """
    Clean the datasets by removing the columns that are not shared between all datasets.
    :param datasets: a list of dataframes
    :param col_name: a list of shared colnames
    :return: the cleaned datasets
    """
    cleaned_datasets: tp.List[pd.DataFrame] = []
    for ds in datasets:
        cleaned = ds[col_name]
        cleaned_datasets.append(cleaned)

    return cleaned_datasets


def build_dataset(datasets: tp.List[pd.DataFrame]) -> pd.DataFrame:
    """
    Create unique dataset by concatenating all datasets.
    :param datasets: the datasets to concatenate.
    :return: a unique dataset, represented by a DataFrame
    """
    unique_ds = pd.concat(datasets, ignore_index=True)
    return unique_ds
