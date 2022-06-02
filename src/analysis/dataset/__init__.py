from .loader import load_datasets
from .merger import compute_ds_col_intersection, clean_datasets, build_dataset
from .scaler import scale_minmax
from .outliers import compute_outlier
import logging

logging.basicConfig(level=logging.INFO)


__all__ = [
    "load_datasets",
    "compute_ds_col_intersection",
    "scale_minmax",
    "clean_datasets",
    "build_dataset",
    "compute_outlier",
]
