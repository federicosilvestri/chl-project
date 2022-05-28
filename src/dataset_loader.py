"""Load dataset"""
import typing
from pathlib import Path

import pandas


def load_dataset(dataset_path: str) -> typing.List[pandas.DataFrame]:
    """
    This function loads all datasets inside memory and returns the dataframe of pandas
    :param dataset_path: the string value of path
    :return: list of pandas data frame
    """

    dataset_path: Path = Path(dataset_path)
    if not dataset_path.is_dir():
        raise ValueError("You must pass a directory path!")

    data_frames: typing.List[pandas.DataFrame] = []
    for item in dataset_path.iterdir():
        if item.is_file() and item.suffix == '.csv':
            data_frames.append(pandas.read_csv(filepath_or_buffer=item))

    return data_frames


