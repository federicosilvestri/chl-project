import logging as lg
from pathlib import Path

import pandas as pd
import typing as tp
from analysis.dataset import load_datasets, compute_ds_col_intersection, clean_datasets, build_dataset, scale_minmax, \
    compute_outlier


class PreprocessPipeline:
    """Pipeline for preprocessing"""

    def __init__(self, datasets_path: str, disease_col_name: str = 'DISEASE'):
        self._dataset_path_: str = datasets_path
        self._disease_col_name: str = disease_col_name
        self._datasets_: tp.List[pd.DataFrame] = []
        self._dataset_: tp.Optional[pd.DataFrame] = None

    def execute_pipeline(self):
        lg.info("Starting pipeline")
        lg.info("Loading datasets")
        self._datasets_ = load_datasets(self._dataset_path_, disease_colname=self._disease_col_name)
        lg.info("Computing column intersection")
        colname_intersection = compute_ds_col_intersection(self._datasets_)
        lg.info("Cleaning datasets from not-shared data")
        self._datasets_ = clean_datasets(self._datasets_, colname_intersection)
        lg.info("Computing outlier detection")
        compute_outlier(self._datasets_, disease_col_name=self._disease_col_name)
        lg.info("Compute the scaling of data")
        scale_minmax(self._datasets_, disease_colname=self._disease_col_name)
        lg.info("Building unique dataset")
        self._dataset_ = build_dataset(self._datasets_)
        lg.info("Pipeline executed")
        # cleaning memory
        del self._datasets_

    def save_dataset_to_csv(self, file_path: str):
        if not self._dataset_:
            raise RuntimeError("Pipeline is not executed yet")

        self._dataset_.to_csv(Path(file_path))

    @property
    def dataset(self):
        return self._dataset_
