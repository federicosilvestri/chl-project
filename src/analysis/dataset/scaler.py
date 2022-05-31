import typing as tp
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import threading


def scale_minmax(datasets: tp.List[pd.DataFrame], disease_colname: str = "DISEASE"):
    """Scale dataset using minmax.
    :param datasets the dataset to be scaled
    :param disease_colname the disease field
    """
    mm_scaler = MinMaxScaler()
    _scaling(datasets, disease_colname, mm_scaler)


def scale_standard(datasets: tp.List[pd.DataFrame], disease_colname: str = "DISEASE"):
    """Scale dataset using standard.
    :param datasets the dataset to be scaled
    :param disease_colname the disease field
    """
    mm_scaler = StandardScaler()
    _scaling(datasets, disease_colname, mm_scaler)


def _scaling(datasets: tp.List[pd.DataFrame], disease_col_name: str, scaler: object):
    threads: tp.List[threading.Thread] = []
    for dataset in datasets:
        # create a thread
        thr = threading.Thread(
            group="chl-scaling",
            target=_execute_scaling,
            args=(dataset, disease_col_name, scaler)
        )
        threads.append(thr)

    # starting all threads
    for t in threads:
        t.start()

    # joining threads
    for t in threads:
        t.join()


def _execute_scaling(dataset: pd.DataFrame, disease_col_name: str, scaler: object):
    # compute columns
    columns = [col_name for col_name in dataset.columns if col_name != disease_col_name]
    # execute scaling
    dataset[columns] = scaler.fit_transform(dataset[columns])

