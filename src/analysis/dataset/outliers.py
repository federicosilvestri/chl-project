"""This file contains function for outlier utility."""
import concurrent.futures
import typing as tp

import pandas as pd
from sklearn.preprocessing import RobustScaler
import logging as lg


def compute_outlier(datasets: tp.List[pd.DataFrame], disease_col_name: str = 'DISEASE') -> None:
    """
    Computes the outlier elements and remove them from datasets.
    :param disease_col_name: the disease column name
    :param datasets: the datasets to be used
    :return: the new dataset
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for df in datasets:
            future = executor.submit(_execute_outlier_detection, dataset=df, disease_col_name=disease_col_name)
        # waiting for futures
        executor.shutdown(wait=True)


def _execute_outlier_detection(dataset: pd.DataFrame, disease_col_name: str) -> None:
    lg.info(f"Computing outlier detection on dataset...")

    # removing column of disease
    columns = [col_name for col_name in dataset.columns if col_name != disease_col_name]

    scaler = RobustScaler(with_scaling=False)
    fit = scaler.fit(dataset[columns].values)
    features = fit.transform(dataset[columns].values)
    dataset[columns] = features
