import pandas as pd
import typing as tp


def split_train_test(train: float, test: float, dataset: pd.DataFrame) -> tp.Dict[str, pd.DataFrame]:
    """
    Split the dataset into train and test set.
    :param train: the percentage of ds to be split into train data
    :param test: the percentage of ds to be split into test data
    :param dataset: the dataset to be splitted
    :return: a dictionary of dataframe, which keys are train, validation, test.
    """
    if sum([train, test]) != 100.0:
        raise ValueError("The sum of train, validation and test percentage must be 100!")


