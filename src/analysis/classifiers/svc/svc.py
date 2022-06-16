import typing as tp
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold, GridSearchCV
import logging as lg
import numpy as np
from sklearn.svm import SVC

from analysis.classifiers.utils import grid_search_report


def build_parameters(train_x: pd.DataFrame, train_y: pd.DataFrame, scoring: tp.List[str] = ['accuracy']) -> tp.Dict:
    param_grid = [
        {'kernel': ['poly'],
         'gamma': ['scale'],
         'C': list(np.arange(1, 10, 0.2)),
         'degree': list(np.arange(1, 4, 1)),
         'coef0': list(np.arange(2, 3, 0.1)),
         'shrinking': [True],
         'class_weight': ['balanced']
         }
    ]

    lg.info("Building hyper parameters for CV classifier")
    cv = StratifiedKFold(n_splits=5)
    grid_search = GridSearchCV(
        estimator=SVC(),
        param_grid=param_grid,
        cv=cv,
        scoring=scoring,
        refit=False,
        n_jobs=-1,
        return_train_score=True
    )
    grid_search.fit(train_x, train_y)
    best_params = grid_search_report(grid_search.cv_results_).iloc[0]['params']

    return best_params


def build_model(train_x: pd.DataFrame, train_y: pd.DataFrame, best_params: tp.Dict) -> SVC:
    # Building the model
    svc: SVC = SVC(**best_params)
    svc.fit(train_x, train_y)
    return svc


def evaluate_model(svc: SVC, test_x: pd.DataFrame, test_y: pd.DataFrame):
    pred_y = svc.predict(test_x)

    return classification_report(
        y_true=test_y,
        y_pred=pred_y
    )
