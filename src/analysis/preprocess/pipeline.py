import logging as lg
import pathlib

import pandas as pd
import typing as tp

from analysis.dataset import load_datasets, compute_ds_col_intersection, clean_datasets, build_dataset, scale_minmax, \
    compute_outlier, split_train_test


class PreprocessPipeline:
    """Pipeline for preprocessing"""

    def __init__(self, datasets_path: str, disease_col_name: str = 'DISEASE', output_dir: str = '/tmp/chl'):
        self._dataset_path_: str = datasets_path
        self._disease_col_name: str = disease_col_name
        self._dataset_: tp.Optional[pd.DataFrame] = None
        self._ds_: tp.Dict[str, pd.DataFrame] = {}
        self.split_ds_train: float = .75
        self.split_ds_test: float = .25
        self.output_dir = output_dir

    def execute_pipeline(self, force_recompute: bool = False):
        if self._load_ds_() and not force_recompute:
            lg.info(f"Pipeline already executed, found dataset inside {self.output_dir}")
            self._split_ds_()
            lg.info("Pipeline executed")
            return

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
        self._store_ds_()
        lg.info(f"Dataset saved into {self.output_dir}")
        self._split_ds_()
        lg.info("Pipeline executed")

    def _split_ds_(self):
        lg.info("Splitting dataset")
        # split the ds
        self._ds_ = split_train_test(
            test=self.split_ds_test,
            dataset=self.dataset,
            disease_colname=self._disease_col_name
        )

    def _store_ds_(self):
        lg.info("Storing dataset")
        output_dir: pathlib.Path = pathlib.Path(self.output_dir)
        if not output_dir.exists():
            lg.info(f"Creating directory {output_dir}")
            output_dir.mkdir()

        # saving the entire dataset
        lg.info("Saving entire dataset")
        self._dataset_.to_csv(
            path_or_buf=pathlib.Path(output_dir / 'full.csv'),
            header=True,
            index=False
        )

    def _load_ds_(self) -> bool:
        output_dir: pathlib.Path = pathlib.Path(self.output_dir)
        if output_dir.exists():
            try:
                self._dataset_ = pd.read_csv(output_dir / 'full.csv')
                return True
            except FileNotFoundError:
                return False
        return False

    @property
    def dataset(self):
        return self._dataset_

    @property
    def test_set(self):
        return self._ds_['x_test'], self._ds_['y_test']

    @property
    def train_set(self):
        return self._ds_['x_train'], self._ds_['y_train']

    @property
    def train_x(self):
        return self._ds_['x_train']
    
    @property
    def train_y(self):
        return self._ds_['y_train']
    
    @property
    def test_x(self):
        return self._ds_['x_test']
    
    @property
    def test_y(self):
        return self._ds_['y_test']
