import typing

import pandas as pd

from src.dataset_loader import load_dataset

DATASET_PATH: str = "../dataset/first_disease_sel/"

list_of_ds = load_dataset(DATASET_PATH)


def normalize_colname(colname: str) -> str:
    normalized = colname.replace(' ', '')
    return normalized.upper()


def intersect_ds(data_frames: typing.List[pd.DataFrame]) -> typing.Set[str]:
    list_of_cols: [str] = []
    for df in data_frames:
        col_name_list = df.columns.values.tolist()
        list_of_cols.append([normalize_colname(col) for col in col_name_list])

    # print(f"Length of dataset {len(set(list_of_cols))}")
    return set.intersection(*map(set, list_of_cols))


intersection = intersect_ds(list_of_ds)


print(f"Length of intersection {len(intersection)}")
