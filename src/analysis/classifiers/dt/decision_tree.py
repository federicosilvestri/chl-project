import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier


def make_model(dataset: pd.DataFrame, disease_colname: str = "DISEASE") -> DecisionTreeClassifier:
    x_cols = [col_name for col_name in dataset.columns if col_name != disease_colname]
    # splitting dataset into train and validation
    train_cv, x_test, target_cv, y_test = train_test_split(dataset[x_cols], dataset[disease_colname], test_size=.25,
                                                           stratify=dataset[disease_colname])

    scoring = ['accuracy']
    params = [
        {
            "criterion": ["gini", "entropy", "log_loss"],
            "splitter": ["best", "random"],
            # add another...
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
    grid_search.fit(train_cv, target_cv)
    decision_tree: DecisionTreeClassifier = DecisionTreeClassifier(**grid_search.best_params_)

    return decision_tree
