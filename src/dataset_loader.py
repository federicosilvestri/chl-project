"""Load dataset"""
import typing
from pathlib import Path

import pandas


def load_dataset(dataset_path: str, disease_colname: str) -> typing.List[pandas.DataFrame]:
    """
    This function loads all datasets inside memory and returns the dataframe of pandas.
    TODO: update doc
    :param dataset_path: the string value of path
    :param disease_colname the name of column for disease
    :return: list of pandas data frame
    """

    dataset_path: Path = Path(dataset_path)
    if not dataset_path.is_dir():
        raise ValueError("You must pass a directory path!")

    data_frames: typing.List[pandas.DataFrame] = []
    for dir_item in dataset_path.iterdir():
        disease_name = dir_item.name
        if not dir_item.is_dir():
            # skip files inside directory
            continue
        for item in dir_item.iterdir():
            # iterating the directory
            if item.is_file() and item.suffix == '.csv':
                data_frame = pandas.read_csv(filepath_or_buffer=item)
                data_frame[disease_colname] = disease_name
                data_frames.append(data_frame)

    return data_frames
