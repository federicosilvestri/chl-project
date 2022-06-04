import pandas as pd
import typing as tp
import logging as lg


def split_train_test(train: float, test: float, dataset: pd.DataFrame) -> tp.Dict[str, pd.DataFrame]:
    """
    Split the dataset into train and test set.
    :param train: the percentage of ds to be split into train data [0,1]
    :param test: the percentage of ds to be split into test data [0,1]
    :param dataset: the dataset to be splitted
    :return: a dictionary of dataframe, which keys are train, validation, test.
    """
    if sum([train, test]) != 1.0:
        raise ValueError("The sum of train, validation and test percentage must be 100!")

    # first make a copy of ds
    test_ds: pd.DataFrame = dataset.sample(frac=test)
    train_ds: pd.DataFrame = dataset.drop(test_ds.index)

    # calculating size
    lg.info(f"Train DS size = {train_ds.shape[0]}, Test DS size={test_ds.shape[0]}")

    # assertion
    assert (test_ds.shape[0] + train_ds.shape[0]) == dataset.shape[0]

    return {
        'test': test_ds,
        'train': train_ds
    }



