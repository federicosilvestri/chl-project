import typing as tp
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def scale_minmax(datasets: tp.List[pd.DataFrame]) -> tp.List[pd.DataFrame]:
    """Scale dataset using minmax.
    :param datasets the dataset to be scaled
    """
    datasets_scaled: tp.List[pd.DataFrame] = []
    for dataset in datasets:
        mm_scaler = MinMaxScaler()
        df = dataset.copy(deep=True)
        # Dropping non-numeric column
        disease_col = df['DISEASE']
        df.drop(columns=['DISEASE'], axis=1, inplace=True)

        df_scaled: pd.DataFrame = pd.DataFrame(mm_scaler.fit_transform(df), columns=df.columns)
        df_scaled.join(disease_col)
        datasets_scaled.append(df_scaled)

    return datasets_scaled




