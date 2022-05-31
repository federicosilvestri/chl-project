import typing as tp
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def scale_minmax(datasets: tp.List[pd.DataFrame]):
    """Scale dataset using minmax.
    :param datasets the dataset to be scaled
    """
    for dataset in datasets:
        mm_scaler = MinMaxScaler()
        columns = [col_name for col_name in dataset.columns if col_name != 'DISEASE']
        dataset[columns] = mm_scaler.fit_transform(dataset[columns])





