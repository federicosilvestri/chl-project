import pandas as pd


def grid_search_report(results) -> pd.DataFrame:
    results_df = pd.DataFrame(results)
    rank = ['rank_test_accuracy']
    columns = ['rank_test_accuracy',
               'mean_test_accuracy', 'mean_train_accuracy', 'std_test_accuracy', 'std_train_accuracy',
               'mean_fit_time', 'params']
    results_df = results_df.sort_values(by=rank)
    results_df = results_df[columns]
    return results_df


__all__ = [
    "grid_search_report",
]
