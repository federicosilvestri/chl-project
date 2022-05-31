import typing as tp
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scale_minmax(datasets: tp.List[pd.DataFrame], disease_colname: str = "DISEASE"):
    """Scale dataset using minmax.
    :param datasets the dataset to be scaled
    :param disease_colname the disease field
    """

    for dataset in datasets:
        mm_scaler = MinMaxScaler()
        # compute columns
        columns = [col_name for col_name in dataset.columns if col_name != disease_colname]
        # execute scaling
        dataset[columns] = mm_scaler.fit_transform(dataset[columns])
