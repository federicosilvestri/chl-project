import pandas as pd
import typing as tp

from sklearn.model_selection import train_test_split


def split_train_test(test: float, dataset: pd.DataFrame) -> tp.Dict[str, pd.DataFrame]:
    """
    Split the dataset into train and test set.
    :param test: the percentage of ds to be split into test data [0,1]
    :param dataset: the dataset to be splitted
    :return: a dictionary of dataframe, which keys are train, validation, test.
    """

    # sklearn call
    train_ds_skl, test_ds_skl = train_test_split(dataset, test_size=test, random_state=42, stratify=dataset['DISEASE'])

    return {
        'test': test_ds_skl,
        'train': train_ds_skl
    }
