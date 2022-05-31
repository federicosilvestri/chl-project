"""This file contains the loader for dataset"""
import pandas as pd
import typing as tp
from pathlib import Path
import logging as lg
import concurrent.futures


def load_datasets(ds_path: str, disease_colname: str = 'DISEASE') -> tp.List[pd.DataFrame]:
    """
    Load all datasets contained inside ds_path. The ds_path structure must be a directory
    that contains subdirectories. Each subdirectory must be named as the name of disease and
    should contain the dataset in '.csv' file format.
    :param ds_path: the path of dataset
    :param disease_colname: the column name of disease to add for each data frame
    :return: a list of DataFrame
    """

    # create the path
    dataset_path: Path = Path(ds_path)

    if not dataset_path.exists() or not dataset_path.is_dir():
        raise ValueError(f"The directory {dataset_path} does not exist or is not a directory.")

    # declaring the datasets list, represented by a DataFrame
    datasets: tp.List[pd.DataFrame] = []
    for dir_item in dataset_path.iterdir():
        if not dir_item.is_dir():
            # It's not a directory
            lg.info(f"Skipping file {dir_item}")
            continue
        lg.info(f"Inspecting directory {dir_item}")
        disease_name = dir_item.name
        lg.info(f"Setting disease as {disease_name}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for item in dir_item.iterdir():
                # iterating the "disease directory"
                if item.is_file() and item.suffix == '.csv':
                    # reading the file with pandas
                    executor.submit(pd.read_csv, kwargs={'filepath_or_buffer': item})
                    # adding disease column
                    data_frame[disease_colname] = disease_name
                    datasets.append(data_frame)

    return datasets
