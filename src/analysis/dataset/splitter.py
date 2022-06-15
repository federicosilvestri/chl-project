import pandas as pd
import typing as tp

from sklearn.model_selection import train_test_split


def split_train_test(test: float, dataset: pd.DataFrame, disease_colname: str = 'DISEASE') -> tp.Dict[str, pd.DataFrame]:
    """
    Split the dataset into train and test set.
    :param test: the percentage of ds to be split into test data [0,1]
    :param dataset: the dataset to be splitted
    :param disease_colname the column of y
    :return: a dictionary of dataframe, which keys are train, validation, test.
    """
    data_cols = [col_name for col_name in dataset.columns if col_name != disease_colname]

    # sklearn call
    x_train, x_test, y_train, y_test = train_test_split(dataset[data_cols], dataset[disease_colname],
                                                        test_size=test,
                                                        random_state=42,
                                                        stratify=dataset[disease_colname]
                                                        )
    return {
        'x_train': x_train,
        'y_train': y_train,
        'x_test': x_test,
        'y_test': y_test,
    }
