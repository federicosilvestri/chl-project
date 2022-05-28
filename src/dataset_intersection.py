import typing

import pandas as pd

from src.dataset_loader import load_dataset


def normalize_colname(colname: str) -> str:
    normalized = colname.replace(' ', '')
    return normalized.upper()


def intersect_ds_colnames(data_frames: typing.List[pd.DataFrame]) -> typing.Set[str]:
    list_of_cols: [str] = []
    for df in data_frames:
        col_name_list = df.columns.values.tolist()
        list_of_cols.append([normalize_colname(col) for col in col_name_list])

    return set.intersection(*map(set, list_of_cols))


def clean_datasets(data_frames: typing.List[pd.DataFrame], shared_columns: typing.List[str]) -> typing.List[pd.DataFrame]:
    """
    Remove columns that are not "shared between datasets".
    :param data_frames: the dataframes
    :return:
    """
    clean_dataset: typing.List[pd.DataFrame] = []
    for df in data_frames:
        df_cleaned = df[list(shared_columns)]
        clean_dataset.append(df_cleaned)
    return clean_dataset


def intersect_ds(data_frames: typing.List[pd.DataFrame]) -> pd.DataFrame:
    big_ds = pd.concat(data_frames)
    return big_ds



DATASET_PATH: str = "../dataset/first_disease_sel/"
# MUST BE UPPERCASE
DISEASE_COLNAME: str = 'DISEASE'

datasets = load_dataset(DATASET_PATH, DISEASE_COLNAME)
int_colnames = intersect_ds_colnames(datasets)
datasets = clean_datasets(datasets, int_colnames)
BIG_DS = intersect_ds(datasets)

