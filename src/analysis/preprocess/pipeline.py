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
        self._ds_ = split_train_test(
            test=self.split_ds_test, dataset=self.dataset
        )
        lg.info("Pipeline executed")

        lg.info("Storing ds")
        self._store_ds_()
        lg.info(f"Dataset saved into {self.output_dir}")

    def _store_ds_(self):
        lg.info("Storing dataset")
        output_dir: pathlib.Path = pathlib.Path(self.output_dir)
        if not output_dir.exists():
            lg.info(f"Creating directory {output_dir}")
            output_dir.mkdir()

        # saving the entire dataset
        lg.info("Saving entire dataset")
        self.dataset.to_csv(path_or_buf=pathlib.Path(output_dir / 'full.csv'))

        # saving all pieces of datasets
        for key, value in self._ds_.items():
            lg.info(f"Saving dataset {key}")
            self._ds_[key].to_csv(path_or_buf=pathlib.Path(output_dir / f"{key}.csv"))

    def _load_ds_(self) -> bool:
        output_dir: pathlib.Path = pathlib.Path(self.output_dir)
        if output_dir.exists():
            try:
                self._dataset_ = pd.read_csv(output_dir / 'full.csv')
                self._ds_['test'] = pd.read_csv(output_dir / 'test.csv')
                self._ds_['train'] = pd.read_csv(output_dir / 'train.csv')
                return True
            except FileNotFoundError:
                return False
        return False

    @property
    def dataset(self):
        return self._dataset_

    @property
    def test_set(self):
        return self._ds_['test']

    @property
    def train_set(self):
        return self._ds_['train']
