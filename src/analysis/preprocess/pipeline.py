import logging as lg

import pandas as pd
import typing as tp

from analysis.dataset import load_datasets, compute_ds_col_intersection, clean_datasets, build_dataset, scale_minmax, \
    compute_outlier, split_train_test


class PreprocessPipeline:
    """Pipeline for preprocessing"""

    def __init__(self, datasets_path: str, disease_col_name: str = 'DISEASE'):
        self._dataset_path_: str = datasets_path
        self._disease_col_name: str = disease_col_name
        self._dataset_: tp.Optional[pd.DataFrame] = None
        self._ds_: tp.Dict[str, pd.DataFrame] = {}
        self.split_ds_train: float = .75
        self.split_ds_test: float = .25

    def execute_pipeline(self):
        lg.info("Starting pipeline")
        lg.info("Loading datasets")
        datasets = load_datasets(self._dataset_path_, disease_colname=self._disease_col_name)
        lg.info("Computing column intersection")
        colname_intersection = compute_ds_col_intersection(datasets)
        lg.info("Cleaning datasets from not-shared data")
        datasets = clean_datasets(datasets, colname_intersection)
        lg.info("Computing outlier detection")
        compute_outlier(datasets, disease_col_name=self._disease_col_name)
        lg.info("Compute the scaling of data")
        scale_minmax(datasets, disease_colname=self._disease_col_name)
        lg.info("Building unique dataset")
        self._dataset_ = build_dataset(datasets)
        lg.info("Splitting dataset into test and train")
        self._ds_ = split_train_test(
            train=self.split_ds_train, test=self.split_ds_test, dataset=self.dataset
        )
        lg.info("Pipeline executed")

    @property
    def dataset(self):
        return self._dataset_

    @property
    def test_set(self):
        return self._ds_['test']

    @property
    def train_set(self):
        return self._ds_['train']
