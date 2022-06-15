import typing as tp
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import logging as lg
import numpy as np


def _grid_search_report(results) -> pd.DataFrame:
    results_df = pd.DataFrame(results)
    rank = ['rank_test_accuracy']
    columns = ['rank_test_accuracy',
               'mean_test_accuracy', 'mean_train_accuracy', 'std_test_accuracy', 'std_train_accuracy',
               'mean_fit_time', 'params']
    results_df = results_df.sort_values(by=rank)
    results_df = results_df[columns]
    return results_df


def build_parameters(train_x: pd.DataFrame, train_y: pd.DataFrame) -> tp.Dict:
    """
    Build the best parameters for Decision Tree.
    :param train_x: the train X
    :param train_y: the train Y
    :return: Decision Tree classifier instance
    """

    scoring = ['accuracy']
    params = [
        {
            "criterion": ["gini", "entropy", "log_loss"],
            "splitter": ["best", "random"],
            "min_samples_split": list(np.arange(2, 10, 1)),
            "min_samples_leaf": list(np.arange(0, 5, 1)),
            "max_features": ["sqrt", "log2"],
            # "ccp_alpha": list(np.arange(0.1, 1, .1))
        }
    ]

    cv = StratifiedKFold(n_splits=5)
    grid_search = GridSearchCV(
        estimator=DecisionTreeClassifier(),
        param_grid=params,
        cv=cv,
        scoring=scoring,
        refit=False,
        n_jobs=-1,
        return_train_score=True
    )
    lg.info("Executing Grid Search for Decision Tree")
    grid_search.fit(train_x, train_y)
    lg.info("Grid search terminated")

    report = _grid_search_report(grid_search.cv_results_)
    lg.info("Report of GridSearch")
    lg.info(report)

    # Fetching best parameters found
    best_params = report.iloc[0]['params']

    return best_params


def build_model(train_x: pd.DataFrame, train_y: pd.DataFrame, best_params: tp.Dict) -> DecisionTreeClassifier:
    # Building the model
    decision_tree: DecisionTreeClassifier = DecisionTreeClassifier(**best_params)
    # fitting the data
    decision_tree.fit(train_x, train_y)

    return decision_tree


def evaluate_model(decision_tree: DecisionTreeClassifier, test_x: pd.DataFrame, test_y: pd.DataFrame):
    """
    Evaluate the model.
    :param decision_tree:
    :param test_x: the test X
    :param test_y: the test y
    :return:
    """
    pred_y = decision_tree.predict(test_x)

    return classification_report(
        y_true=test_y,
        y_pred=pred_y
    )


