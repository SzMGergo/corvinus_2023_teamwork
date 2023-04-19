import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from portfolio import Portfolio
from utils import calc_historical_var, calc_covar_var


def evaluate_var_model(model_func, portfolio, conf_level, train_start, train_end, test_start, test_end, window_in_days):
    train_returns = portfolio.get_pf_returns(train_start, train_end)
    test_returns = portfolio.get_pf_returns(test_start, test_end)

    _, var_amount = model_func(portfolio.pf_value, portfolio.d_weights, [conf_level], train_end, window_in_days)
    var_amount = var_amount.squeeze()

    test_losses = test_returns.loc[test_start:test_end]['pf']
    violations = (test_losses < var_amount).sum()

    return violations / len(test_losses)


def cross_validate_var_models(portfolio, conf_level, from_date, to_date, window_in_days, n_splits=5):
    tscv = TimeSeriesSplit(n_splits=n_splits)
    pf_returns = portfolio.get_pf_returns(from_date, to_date)

    hist_var_scores = []
    covar_var_scores = []

    for train_index, test_index in tscv.split(pf_returns):
        train_start, train_end = pf_returns.index[train_index[0]], pf_returns.index[train_index[-1]]
        test_start, test_end = pf_returns.index[test_index[0]], pf_returns.index[test_index[-1]]

        hist_var_score = evaluate_var_model(calc_historical_var, portfolio, conf_level, train_start, train_end,
                                            test_start, test_end, window_in_days)
        covar_var_score = evaluate_var_model(calc_covar_var, portfolio, conf_level, train_start, train_end, test_start,
                                             test_end, window_in_days)

        hist_var_scores.append(hist_var_score)
        covar_var_scores.append(covar_var_score)

    return np.mean(hist_var_scores), np.mean(covar_var_scores)


def choose_best_var_model(portfolio, conf_level, from_date, to_date, window_in_days, n_splits=5):
    hist_var_score, covar_var_score = cross_validate_var_models(portfolio, conf_level, from_date, to_date,
                                                           window_in_days, n_splits)
    print('hist_var_score', hist_var_score)
    print('covar_var_score', covar_var_score)
    if hist_var_score < covar_var_score:
        return 'hist', hist_var_score
    else:
        return 'covar', covar_var_score


# Example usage
d_weights = {'IEI': 0.6, 'VOO': 0.4}
pf_value = 10000
portfolio = Portfolio(d_weights, pf_value)
conf_level = 0.99
from_date = '2018-01-01'
to_date = '2020-12-31'
window_in_days = 250

best_model, best_score = choose_best_var_model(portfolio, conf_level, from_date, to_date, window_in_days)
print(f"Best VaR model: {best_model}, score: {best_score}")