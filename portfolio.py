import pandas as pd
import utils as u
import numpy as np
import visualization as v
import matplotlib.pyplot as plt

class Portfolio():

    def __init__(self, d_weights, pf_value):
        self.d_weights = d_weights
        self.pf_value = pf_value


    # parameters: from date to date
    def get_pf_returns(self, from_date, to_date):
        pf_return = u.get_portfolio_return_btw_dates(
            self.d_weights, from_date, to_date)
        return pf_return


    # parameters: from date to date
    def get_returns_of_etfs(self, from_date, to_date):
        filtered_df=u.get_joined_returns(self.d_weights, from_date, to_date)
        return filtered_df

    def calculate_var(
            self, vartype, l_conf_levels,
            from_date, to_date, window_in_days):
        df_result = u.calc_var_for_period(vartype,
            self.pf_value, self.d_weights,
             l_conf_levels,
            from_date, to_date, window_in_days)
        return df_result

    def plot_vars_for_conf_level(self, conf_level, from_date, to_date, window_in_days, show=True):
        v.plot_multiple_vars_for_one_conf(self.d_weights, self.pf_value, conf_level,
                                                    from_date, to_date, window_in_days, show)

    def plot_one_var_for_multiple_conf_level(
            self, vartype,
            l_conf_levels, from_date, to_date, window_in_days):
        v.plot_one_var_for_multiple_conf_level(
            self.d_weights, self.pf_value, vartype, l_conf_levels,
            from_date, to_date, window_in_days,
            show=True)

#pd.plotting.scatter_matrix(df, alpha=0.2)
    def scatter_returns_of_etfs(self, from_date, to_date):
        df = self.get_returns_of_etfs(from_date, to_date)
        pd.plotting.scatter_matrix(df, alpha=0.2)
        plt.show()
